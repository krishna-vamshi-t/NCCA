# Netflix Customer Churn — Case Study

**Analyst:** Krishna Vamshi T | **Tools:** Python, SQL, Power BI | **Dataset:** 10,000 customers

## Background
This project analyzes churn behavior across 10,000 Netflix subscribers
to identify retention opportunities and high-risk customer segments.

## Problem Statement
Netflix loses 14.44% of its customers annually. The goal of this analysis
is to understand who is churning, why they are churning, and what actions
can reduce churn rate.

## Data Overview
- 10,000 raw records, 8,940 after cleaning
- 20 original features, 25 after feature engineering
- Key columns: SubscriptionPlan, TenureMonths, WatchHoursPerMonth,
  PaymentFailures, DaysSinceLastLogin, CustomerSupportTickets

## Key Findings

### Churn by Plan
| Plan | Churn Rate |
|------|------------|
| Basic | 17.1% |
| Standard | 14.1% |
| Premium | 9.8% |

### Churn by Segment
| Segment | Churn Rate |
|---------|------------|
| High Risk | 27.3% |
| Casual | 18.4% |
| New | 16.9% |
| Mid-Tier | 10.9% |
| Loyal | 6.1% |

### Churn by Country
Brazil and Mexico have the highest churn rates at 15.7% and 15.1%.
Japan and Australia have the lowest at 12.2% and 12.7%.

### Behavioral Signals
- Churned users watch 2 fewer hours per month
- Churned users log in less frequently
- Higher payment failures strongly correlate with churn
- Auto-renew disabled users churn at nearly double the rate

## Recommendations
1. Prioritize Basic plan users with payment failures for retention campaigns
2. Introduce loyalty rewards at 6, 12, and 24 month milestones
3. Re-engage users inactive for 15+ days with personalized content
4. Run auto-renew enablement campaigns in Brazil and Mexico
5. Improve new customer onboarding in first 90 days

## Tools Used
- Python (pandas, matplotlib, seaborn)
- SQL (SQLite)
- Power BI
- Git/GitHub