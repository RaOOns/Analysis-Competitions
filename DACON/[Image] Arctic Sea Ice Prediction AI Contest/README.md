# Arctic Sea Ice Prediction AI Contest (북극 해빙예측 AI 경진대회)

### The Goal
Prediction of weekly sea ice extent change using changes in Arctic sea ice observed since 1978

<br/>

### My approach
I wanted to use time series analysis to solve image data.

This approach was interesting, but it took a lot of time, and I was immature.

<br/>

### Data

> Common
  - 각 파일(*.npy)은 해빙 농도(0~250), 북극점(위성 관측 불가 영역), 해안선 마스크, 육지 마스크, 결측값 5개의 채널로 구성
  - date : 해빙 농도 관측일 | file_nm : 데이터 파일명
  - weekly_start : 주별 해빙농도의 해당주 시작일 | week_file_nm : 데이터 파일명 | data_list : 주별 해빙 농도에 사용된 일별 해빙 농도 데이터

> Train
  - daily_train.csv(date, file_nm): 학습용 일별 해빙 농도 데이터 정보
  - daily_train: 일별 해빙 농도 데이터
  - weekly_train.csv(weekly_start, week_file_nm, data_list): 학습용 주별 해빙 농도 데이터 정보
  - weekly_train : 주별 해빙 농도 데이터 / 월~일 일별 해빙농도의 평균

> Test
  - public_daily_test.csv(date, file_nm): public 기간 추론시 사용 가능한 일별 데이터 정보
  - public_weekly_test.csv(weekly_start, week_file_nm, data_list): public 기간 추론시 사용 가능한 주별 데이터 정보

<br/>

### Introduction
- Evaluation metric: MAE/F1-score, MAE, F1-score
- Competition period: 2021.05.10 ~ 2021.06.30 17:59
- Organized: DACON
- Hosted: Korea Polar Research Institute(KOPRI, 극지 연구소)


https://dacon.io/competitions/official/235731/overview/description
