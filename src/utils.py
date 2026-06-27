import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("assets", exist_ok=True)


def plot_retention_curve(df: pd.DataFrame) -> None:
    retention = df.groupby("tenuremonths")["churn"].mean() * 100
    retention = 100 - retention

    plt.figure(figsize=(12, 5))
    plt.plot(retention.index, retention.values, color="#e50914", linewidth=2)
    plt.fill_between(retention.index, retention.values, alpha=0.1, color="#e50914")
    plt.title("Customer Retention Curve by Tenure", fontsize=14)
    plt.xlabel("Tenure (Months)")
    plt.ylabel("Retention Rate (%)")
    plt.tight_layout()
    plt.savefig("assets/netflix_retention_curve.png", dpi=150)
    plt.close()
    print("[INFO] Saved netflix_retention_curve.png")


def plot_churn_heatmap(df: pd.DataFrame) -> None:
    pivot = df.pivot_table(
        values="churn",
        index="country",
        columns="subscriptionplan",
        aggfunc="mean"
    ) * 100

    plt.figure(figsize=(10, 7))
    sns.heatmap(pivot, annot=True, fmt=".1f", cmap="Reds", linewidths=0.5)
    plt.title("Churn Rate Heatmap: Country vs Subscription Plan", fontsize=14)
    plt.tight_layout()
    plt.savefig("assets/netflix_churn_heatmap.png", dpi=150)
    plt.close()
    print("[INFO] Saved netflix_churn_heatmap.png")


def plot_cohort_analysis(df: pd.DataFrame) -> None:
    df = df.copy()
    cohort_churn = df.groupby(["tenure_group", "subscriptionplan"])["churn"].mean() * 100
    cohort_churn = cohort_churn.reset_index()

    plt.figure(figsize=(12, 5))
    for plan in cohort_churn["subscriptionplan"].unique():
        subset = cohort_churn[cohort_churn["subscriptionplan"] == plan]
        plt.plot(subset["tenure_group"].astype(str), subset["churn"], marker="o", label=plan)

    plt.title("Cohort Churn Analysis by Tenure Group and Plan", fontsize=14)
    plt.xlabel("Tenure Group")
    plt.ylabel("Churn Rate (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("assets/netflix_cohort_analysis.png", dpi=150)
    plt.close()
    print("[INFO] Saved netflix_cohort_analysis.png")


def plot_segment_dashboard(df: pd.DataFrame) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.suptitle("Netflix Churn Dashboard Preview", fontsize=15)

    # Churn by segment
    seg = df.groupby("segment")["churn"].mean().sort_values() * 100
    axes[0].barh(seg.index, seg.values, color="#e50914")
    axes[0].set_title("Churn by Segment")
    axes[0].set_xlabel("Churn Rate (%)")

    # Churn by plan
    plan = df.groupby("subscriptionplan")["churn"].mean().sort_values() * 100
    axes[1].bar(plan.index, plan.values, color="#221f1f")
    axes[1].set_title("Churn by Plan")
    axes[1].set_ylabel("Churn Rate (%)")

    # Engagement vs churn
    eng = df.groupby("churn")["engagement_score"].mean()
    axes[2].bar(["Retained", "Churned"], eng.values, color=["#2ecc71", "#e50914"])
    axes[2].set_title("Avg Engagement Score")
    axes[2].set_ylabel("Score")

    plt.tight_layout()
    plt.savefig("assets/netflix_dashboard_preview.png", dpi=150)
    plt.close()
    print("[INFO] Saved netflix_dashboard_preview.png")


def generate_all_assets(df: pd.DataFrame) -> None:
    print("\n[INFO] Generating assets...\n")
    plot_retention_curve(df)
    plot_churn_heatmap(df)
    plot_cohort_analysis(df)
    plot_segment_dashboard(df)
    print("\n[INFO] All assets saved to assets/\n")