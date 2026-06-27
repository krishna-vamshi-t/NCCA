## Netflix Customer Churn Analysis (NCCA) ##
*** Business Intelligence & Retention Analytics Project ***

## Project Overview
This project analyzes customer churn behavior in a Netflix-like streaming platform using SQL, Python, and Power BI.
The goal is to identify when users are at risk of churning, why they disengage, and what interventions can improve retention.
The focus is not just on analysis, but on **actionable business decisions driven by user behavior signals.**

## Business Problem
Streaming platforms lose revenue when users silently disengage before cancelling subscriptions.

## This project addresses:
- When churn risk becomes critical in the customer lifecycle
- Which behavioral signals predict churn early
- Which customer segments are most vulnerable
- What actions can reduce churn probability

## Dataset
- 10,000 simulated customer records (portfolio dataset)
- Includes subscription, engagement, payment, and behavioral data
- Target variable: **Churn**
> Note: This dataset is synthetic and created for educational and portfolio purposes.

## Key Insights
- Users on the **Basic plan** churn significantly faster within the first 90 days
- Early inactivity (low watch time + low logins) is the strongest churn indicator
- The first 3 months represent the highest-risk churn window
- Payment failures strongly increase churn probability
- High engagement reduces churn risk significantly

## Business Recommendations
- Improve onboarding experience in the first 7–30 days
- Trigger re-engagement campaigns for inactive users
- Strengthen payment failure recovery system
- Prioritize support for high-risk users
- Improve recommendation system visibility

## Tools Used
- SQL
- Python (Pandas, NumPy)
- Matplotlib, Seaborn
- Power BI
- Business Intelligence & Data Analysis

## Workflow
1. Business Understanding  
2. Data Extraction (SQL)  
3. Data Cleaning (Python)  
4. Feature Engineering  
5. Churn Metrics Calculation  
6. Exploratory Data Analysis  
7. Power BI Dashboard  
8. Business Insights & Recommendations  

## Project Structure
Netflix-Churn-Analysis/
│
├── data/
├── sql/
├── python/
├── dashboard/
├── images/
├── report/
├── requirements.txt
└── README.md

## Portfolio Impact
This project demonstrates:
- End-to-end analytics pipeline design
- Customer churn analysis & segmentation
- SQL + Python + BI integration
- Business-focused data storytelling
- Real-world retention strategy thinking