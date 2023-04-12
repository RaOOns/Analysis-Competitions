# Jeju Island Road Traffic Volume Prediction AI Competition
**제주도 도로 교통량 예측 AI 경진대회 &nbsp; | &nbsp; Ranking: 113/712 (top 15.8%)**

### The Goal
Development of an AI model for predicting Jeju Island Road Traffic Volume

<br/>

### My approach
- I created derived variables and used machine learning.
- **Jeju.py**: It is a function file created for the analysis competition.

<br/>

### Data
- Train data
  - Only data before August 2022 exists (However, the dates are not all consecutive, total 4,701,217 samples)
  - ID
  - Target(unit: km): Average speed of vehicles on the road
  - Information such as date, time, traffic and road section

- Test data
  - Only August 2022 data exists (However, the dates are not all consecutive, total 291,241 samples)
  - Same as training data except Target

<br/>

### Information
- Evaluation metric: MAE
- Competition period: 2022.10.03 ~ 2022.11.14 10:00
- Hosted: Jeju Techno-Park(제주 테크노파크) and Jeju Special Self-Governing Province(제주특별자치도)
- Organized: DACON
- Site: https://dacon.io/competitions/official/235985/overview/description
