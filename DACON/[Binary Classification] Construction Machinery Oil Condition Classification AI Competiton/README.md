# Construction Machinery Oil Condition Classification AI Competiton
**건설기계 오일 상태 분류 AI 경진대회 &nbsp; | &nbsp; Ranking: 23/517 (top 4%)**

### The Goal
Development of an oil condition judgment model to monitor the condition of operating oil in construction equipment in real time (binary classification: normal, abnormal)

<br/>

### My approach
I combined the concept of knowledge distillation with machine learning methods.

<br/>

### Data
- **Significant:** All given features can be used during model training, but only a limited number of features can be used during diagnostic testing.

- Train data
  - ID
  - 52 features
  - Y_LABEL: Oil condition (0: normal, 1: abnormal)

- Test data
  - ID
  - 18 features

<br/>

### Information
- Evaluation metric: Macro F1 Score
- Competition period: 2022.11.07 ~ 2022.12.12 10:00
- Hosted: Hyundai Genuine(현대제뉴인)
- Support: AWS
- Organized: DACON
- Site: https://dacon.io/competitions/official/236013/overview/description
