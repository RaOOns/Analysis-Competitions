import pandas as pd
import numpy as np

from datetime import datetime, timedelta
from tqdm.notebook import tqdm
import time 
import geopy.distance
import random

from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost import XGBRegressor


def road_(data) : 
    
    kd = [s for s in list(data["road_name"]) if "일반국도" in s]
    ro = [s for s in list(data["road_name"]) if "로" in s[-1]]
    kyo = [s for s in list(data["road_name"]) if "교" in s]
    jbd = [s for s in list(data["road_name"]) if "지방도" in s]
    gil = [s for s in list(data["road_name"]) if "길" in s]
    _ = [s for s in list(data["road_name"]) if "-" in s]
    
    x = data["road_name"]
    cond = [x.isin(kd), x.isin(ro), x.isin(kyo), x.isin(jbd), x.isin(gil), x.isin(_)]
    ans = [1, 2, 3, 4, 5, 6]
    data["road_name_"] = np.select(cond, ans)
    
    return data


def cat_onehot(data, var = ["day_of_week", "road_rating", "weight_restricted", "road_type", "road_name_", "start_turn_restricted", "end_turn_restricted"]) :
    print("Cat_Onehot")
    
    if "day_of_week" in var : 
        x = data["day_of_week"]
        cond = [x.isin(["금", "토", "일"]), x.isin(["월", "화", "수", "목"])]
        ans = [1, 2]
        data["day_of_week"] = np.select(cond, ans)
    
    temp = pd.DataFrame()
    for i in tqdm(range(len(var))):
        temp = pd.concat([temp, pd.get_dummies(data[var[i]], prefix = var[i])], axis = 1)
    data = pd.concat([data.drop(columns = var), temp], axis = 1)
    
    return data    


def cat_label(data, var = ["day_of_week", "road_rating", "weight_restricted", "road_type", "road_name_", "start_turn_restricted", "end_turn_restricted"]) :
    print("Cat_Label")
    for i in tqdm(var):
        le = LabelEncoder()
        le = le.fit(data[i])
        data[i]=le.transform(data[i])

    return data


def std_(train, test, var = ['base_hour', 'lane_count', 'maximum_speed_limit']) :
    std = StandardScaler().fit(train[var])
    std_train = pd.DataFrame(std.transform(train[var]), columns = var)
    train[var] = std_train
    
    std_test = pd.DataFrame(std.transform(test[var]), columns = var)
    test[var] = std_test
    
    return train, test


def dist_(data) :
    print("Distance")
    start = data[["start_latitude", "start_longitude"]]
    end = data[["end_latitude", "end_longitude"]]
    jeju = (33.500770, 126.522761)
    seoqui = (33.259429, 126.558217)
    airport = (33.511111, 126.492778)
    
    dist = [geopy.distance.geodesic(end.iloc[i,:], start.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_jeju_start = [geopy.distance.geodesic(jeju, start.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_jeju_end = [geopy.distance.geodesic(jeju, end.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_seoqui_start = [geopy.distance.geodesic(seoqui, start.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_seoqui_end = [geopy.distance.geodesic(seoqui, end.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_airport_start = [geopy.distance.geodesic(airport, start.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    dist_airport_end = [geopy.distance.geodesic(airport, end.iloc[i,:]).km for i in tqdm(range(data.shape[0]))]
    
    data["dist"] = dist
    data["dist_jeju_start"] = dist_jeju_start
    data["dist_jeju_end"] = dist_jeju_end
    data["dist_seoqui_start"] = dist_seoqui_start
    data["dist_seoqui_end"] = dist_seoqui_end
    data["dist_airport_start"] = dist_airport_start
    data["dist_airport_end"] = dist_airport_end
    
    return data    


def weather_(data, weather) :
    data["base_date"] = pd.to_datetime(data["base_date"].astype(str))
    weather["일시+1"] = pd.to_datetime(weather["일시"]) + timedelta(days = 1) 
    data = pd.merge(data, weather, left_on = "base_date", right_on = "일시+1", how = "left")
    data.drop(columns = ["일시+1"], inplace = True)
    
    return data    



def covid_(data, covid) :
    data["base_date"] = pd.to_datetime(data["base_date"].astype(str))
    covid["일자+1"] = pd.to_datetime(covid["일자"]) + timedelta(days = 1)
    data = pd.merge(data, covid, left_on = "base_date", right_on = "일자+1", how = "left")
    data.drop(columns = ["일자+1"], inplace = True)
    
    return data   


def fit_pred_(train_X, train_y, valid_X, valid_y, models) :
    model_dict, pred_dict, mae_dict = {}, {}, {}
    for model_name, model in tqdm(models.items()) :
        model = model.fit(train_X, train_y)
        pred = model.predict(valid_X)
        mae = mean_absolute_error(valid_y, pred)
    
        model_dict[model_name] = model
        pred_dict[model_name] = pred
        mae_dict[model_name] = mae
    
    return model_dict, pred_dict, mae_dict
        
        
def cv_fit_(train_X, train_y, cv_model = XGBRegressor(tree_method = 'gpu_hist', gpu_id = 0), kfold = KFold(n_splits = 10)) :
    cv_model_list, cv_mae = [], []
    n_iter = 0

    for tr_idx, val_idx in kfold.split(train_X) :
        cv_train_X, cv_valid_X = train_X.iloc[tr_idx], train_X.iloc[val_idx]
        cv_train_y, cv_valid_y = train_y[tr_idx], train_y[val_idx]

        start_time = time.time()
        cv_model = cv_model
        cv_model.fit(cv_train_X, cv_train_y)
        cv_model_list.append(cv_model)
        cv_pred = cv_model.predict(cv_valid_X)
        n_iter += 1

        mae = np.round(mean_absolute_error(cv_valid_y, cv_pred), 4) # 소수점 4자리 반올림
        train_size = cv_train_X.shape[0]
        test_size = cv_valid_X.shape[0]

        print('\n#{0} 교차 검증 MAE : {1},  학습 데이터 크기 : {2},  검증 데이터 크기 : {3},  소요 시간 : {4}sec'
              .format(n_iter, mae, train_size, test_size, np.round(time.time() - start_time, 3)))
        print('#{0} 검증 세트 인덱스 : {1}'.format(n_iter, val_idx))
        cv_mae.append(mae)

    print('\n## 평균 검증 정확도:', np.mean(cv_mae))
    
    return cv_model_list, cv_mae