import os
import matplotlib.pyplot as plt

CHARTS_DIR = "charts"

os.makedirs(CHARTS_DIR, exist_ok=True)


def plot_stage_over_time(df):

    plt.figure(figsize=(10, 5))

    plt.plot(df["datetime"], df["stage"])

    plt.title("Load Shedding Stage Over Time")
    plt.xlabel("Date")
    plt.ylabel("Stage")

    plt.tight_layout()

    plt.savefig(f"{CHARTS_DIR}/stage_over_time.png")

    plt.close()


def plot_avg_stage_by_month(df):

    plt.figure(figsize=(10, 5))

    plt.bar(df["month_name"], df["avg_stage"])

    plt.title("Average Stage By Month")
    plt.xlabel("Month")
    plt.ylabel("Average Stage")

    plt.xticks(rotation=45)

    plt.tight_layout()

    plt.savefig(f"{CHARTS_DIR}/avg_stage_by_month.png")

    plt.close()


def plot_stage_by_day_of_week(df):

    plt.figure(figsize=(10, 5))

    plt.bar(df["day_name"], df["avg_stage"])

    plt.title("Average Stage By Day")
    plt.xlabel("Day")
    plt.ylabel("Average Stage")

    plt.tight_layout()

    plt.savefig(f"{CHARTS_DIR}/stage_by_day.png")

    plt.close()