# Citrus Fruit Prediction AI Competition
**감귤착과량 예측 AI 경진대회 &nbsp; | &nbsp; Ranking: 79/257 (top 30.7%)**

### The Goal
Development of an AI model for predicting citrus yield

<br/>

### My approach
I created derived variables and used machine learning.

<br/>

### Data
- **Significant:** All given features can be used during model training, but only a limited number of features can be used during diagnostic testing.

- Train data
  - ID
  - Target: Yield
  - Tree growth status (unit: cm): height, crown width1(min), crown width2(max), average crown width(average of crown width 1 and crown width 2)
  - Sprout Features: Sprout data is measured daily from September 01, 2022 to November 28, 2022
  - Chlorophyll Features: Chlorophyll data is measured daily from September 01, 2022 to November 28, 2022

- Test data: Same as training data except Target

<br/>

### Information
- Evaluation metric: NMAE
- Competition period: 2022.12.12 ~ 2022.12.14 10:00
- Hosted: Jeju Techno-Park(제주 테크노파크)
- Organized: DACON
- Site: https://dacon.io/competitions/official/236038/overview/description
