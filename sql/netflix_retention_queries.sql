-- Netflix Customer Churn Analysis SQL Queries

-- 1. Total customers and churn rate
SELECT
    COUNT(*) AS total_customers,
    SUM(CASE WHEN Churn = 1 THEN 1 ELSE 0 END) AS churned_customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn;

-- 2. Churn by subscription plan
SELECT
    SubscriptionPlan,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY SubscriptionPlan
ORDER BY churn_rate_pct DESC;

-- 3. Churn by country
SELECT
    Country,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY Country
ORDER BY churn_rate_pct DESC;

-- 4. Churn by gender
SELECT
    Gender,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY Gender;

-- 5. Churn by age group
SELECT
    CASE
        WHEN Age BETWEEN 18 AND 24 THEN '18-24'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END AS age_group,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY
    CASE
        WHEN Age BETWEEN 18 AND 24 THEN '18-24'
        WHEN Age BETWEEN 25 AND 34 THEN '25-34'
        WHEN Age BETWEEN 35 AND 44 THEN '35-44'
        WHEN Age BETWEEN 45 AND 54 THEN '45-54'
        ELSE '55+'
    END
ORDER BY churn_rate_pct DESC;

-- 6. Churn by tenure bucket
SELECT
    CASE
        WHEN TenureMonths BETWEEN 0 AND 3 THEN '0-3'
        WHEN TenureMonths BETWEEN 4 AND 12 THEN '4-12'
        WHEN TenureMonths BETWEEN 13 AND 24 THEN '13-24'
        WHEN TenureMonths BETWEEN 25 AND 48 THEN '25-48'
        ELSE '49+'
    END AS tenure_bucket,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY
    CASE
        WHEN TenureMonths BETWEEN 0 AND 3 THEN '0-3'
        WHEN TenureMonths BETWEEN 4 AND 12 THEN '4-12'
        WHEN TenureMonths BETWEEN 13 AND 24 THEN '13-24'
        WHEN TenureMonths BETWEEN 25 AND 48 THEN '25-48'
        ELSE '49+'
    END
ORDER BY churn_rate_pct DESC;

-- 7. Average watch hours by churn status
SELECT
    Churn,
    ROUND(AVG(WatchHoursPerMonth), 2) AS avg_watch_hours,
    COUNT(*) AS customers
FROM netflix_churn
GROUP BY Churn;

-- 8. Churn by inactivity bucket
SELECT
    CASE
        WHEN DaysSinceLastLogin BETWEEN 0 AND 3 THEN '0-3'
        WHEN DaysSinceLastLogin BETWEEN 4 AND 7 THEN '4-7'
        WHEN DaysSinceLastLogin BETWEEN 8 AND 14 THEN '8-14'
        WHEN DaysSinceLastLogin BETWEEN 15 AND 30 THEN '15-30'
        ELSE '31+'
    END AS inactivity_bucket,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY
    CASE
        WHEN DaysSinceLastLogin BETWEEN 0 AND 3 THEN '0-3'
        WHEN DaysSinceLastLogin BETWEEN 4 AND 7 THEN '4-7'
        WHEN DaysSinceLastLogin BETWEEN 8 AND 14 THEN '8-14'
        WHEN DaysSinceLastLogin BETWEEN 15 AND 30 THEN '15-30'
        ELSE '31+'
    END
ORDER BY churn_rate_pct DESC;

-- 9. Support tickets by churn status
SELECT
    Churn,
    ROUND(AVG(CustomerSupportTickets), 2) AS avg_tickets,
    COUNT(*) AS customers
FROM netflix_churn
GROUP BY Churn;

-- 10. Payment failures by churn status
SELECT
    Churn,
    ROUND(AVG(PaymentFailures), 2) AS avg_payment_failures,
    COUNT(*) AS customers
FROM netflix_churn
GROUP BY Churn;

-- 11. Auto-renew impact
SELECT
    AutoRenewEnabled,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY AutoRenewEnabled;

-- 12. Churn by number of devices used
SELECT
    DevicesUsed,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY DevicesUsed
ORDER BY DevicesUsed;

-- 13. Churn by number of profiles
SELECT
    NumberOfProfiles,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY NumberOfProfiles
ORDER BY NumberOfProfiles;

-- 14. Average recommendation clicks by churn status
SELECT
    Churn,
    ROUND(AVG(RecommendationClicks), 2) AS avg_recommendation_clicks
FROM netflix_churn
GROUP BY Churn;

-- 15. Average downloads by churn status
SELECT
    Churn,
    ROUND(AVG(DownloadsPerMonth), 2) AS avg_downloads
FROM netflix_churn
GROUP BY Churn;

-- 16. Monthly fee by churn status
SELECT
    Churn,
    ROUND(AVG(MonthlyFee), 2) AS avg_monthly_fee
FROM netflix_churn
GROUP BY Churn;

-- 17. Plan and country interaction
SELECT
    Country,
    SubscriptionPlan,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY Country, SubscriptionPlan
ORDER BY churn_rate_pct DESC;

-- 18. Top high-risk segments using CASE
SELECT
    CASE
        WHEN DaysSinceLastLogin >= 15 AND PaymentFailures >= 1 THEN 'Inactive + Payment Issues'
        WHEN DaysSinceLastLogin >= 15 THEN 'Inactive'
        WHEN CustomerSupportTickets >= 3 THEN 'High Support Friction'
        ELSE 'Lower Risk'
    END AS risk_segment,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY
    CASE
        WHEN DaysSinceLastLogin >= 15 AND PaymentFailures >= 1 THEN 'Inactive + Payment Issues'
        WHEN DaysSinceLastLogin >= 15 THEN 'Inactive'
        WHEN CustomerSupportTickets >= 3 THEN 'High Support Friction'
        ELSE 'Lower Risk'
    END
ORDER BY churn_rate_pct DESC;

-- 19. CTE for retention by tenure and engagement
WITH customer_summary AS (
    SELECT
        CustomerID,
        TenureMonths,
        WatchHoursPerMonth,
        DaysSinceLastLogin,
        Churn
    FROM netflix_churn
)
SELECT
    CASE
        WHEN TenureMonths <= 3 THEN 'Early'
        WHEN TenureMonths <= 12 THEN 'Growth'
        ELSE 'Mature'
    END AS lifecycle_stage,
    ROUND(AVG(WatchHoursPerMonth), 2) AS avg_watch_hours,
    ROUND(AVG(DaysSinceLastLogin), 2) AS avg_inactivity_days,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM customer_summary
GROUP BY
    CASE
        WHEN TenureMonths <= 3 THEN 'Early'
        WHEN TenureMonths <= 12 THEN 'Growth'
        ELSE 'Mature'
    END;

-- 20. Window function ranking countries by churn
WITH country_churn AS (
    SELECT
        Country,
        ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
    FROM netflix_churn
    GROUP BY Country
)
SELECT
    Country,
    churn_rate_pct,
    RANK() OVER (ORDER BY churn_rate_pct DESC) AS churn_rank
FROM country_churn
ORDER BY churn_rank;

-- 21. Window function segmenting customers into churn risk deciles
WITH risk_scores AS (
    SELECT
        CustomerID,
        Churn,
        DaysSinceLastLogin + PaymentFailures * 10 + CustomerSupportTickets * 4 AS risk_score
    FROM netflix_churn
)
SELECT
    CustomerID,
    risk_score,
    NTILE(10) OVER (ORDER BY risk_score DESC) AS risk_decile
FROM risk_scores;

-- 22. Average churn by plan and auto-renew
SELECT
    SubscriptionPlan,
    AutoRenewEnabled,
    COUNT(*) AS customers,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY SubscriptionPlan, AutoRenewEnabled
ORDER BY SubscriptionPlan, AutoRenewEnabled;

-- 23. Support tickets and churn by tenure bucket
SELECT
    CASE
        WHEN TenureMonths <= 3 THEN '0-3'
        WHEN TenureMonths <= 12 THEN '4-12'
        WHEN TenureMonths <= 24 THEN '13-24'
        ELSE '25+'
    END AS tenure_stage,
    ROUND(AVG(CustomerSupportTickets), 2) AS avg_support_tickets,
    ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
FROM netflix_churn
GROUP BY
    CASE
        WHEN TenureMonths <= 3 THEN '0-3'
        WHEN TenureMonths <= 12 THEN '4-12'
        WHEN TenureMonths <= 24 THEN '13-24'
        ELSE '25+'
    END;

-- 24. Top 20 highest-risk customers
SELECT
    CustomerID,
    SubscriptionPlan,
    Country,
    DaysSinceLastLogin,
    PaymentFailures,
    CustomerSupportTickets,
    CASE
        WHEN DaysSinceLastLogin >= 15 THEN 3
        WHEN DaysSinceLastLogin >= 7 THEN 2
        ELSE 1
    END
    + PaymentFailures
    + CustomerSupportTickets AS risk_score
FROM netflix_churn
ORDER BY risk_score DESC
LIMIT 20;

-- 25. Retention opportunity analysis
WITH segment_stats AS (
    SELECT
        SubscriptionPlan,
        ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS churn_rate_pct
    FROM netflix_churn
    GROUP BY SubscriptionPlan
),
overall AS (
    SELECT ROUND(100.0 * AVG(CAST(Churn AS FLOAT)), 2) AS overall_churn_pct
    FROM netflix_churn
)
SELECT
    s.SubscriptionPlan,
    s.churn_rate_pct,
    o.overall_churn_pct,
    ROUND(s.churn_rate_pct - o.overall_churn_pct, 2) AS churn_gap_pct
FROM segment_stats s
CROSS JOIN overall o
ORDER BY churn_gap_pct DESC;