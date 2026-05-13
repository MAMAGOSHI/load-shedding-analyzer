class BaseProcessor:
    """
    Base class required by project brief.
    """

    def __init__(self, df):
        self.df = df


class Analyzer(BaseProcessor):

    def process(self):

        self.df["month"] = self.df["datetime"].dt.month
        self.df["month_name"] = self.df["datetime"].dt.month_name()

        self.df["day_name"] = self.df["datetime"].dt.day_name()

        self.df["year"] = self.df["datetime"].dt.year

        # Q1
        q1 = (
            self.df.groupby("month_name")["stage"]
            .mean()
            .reset_index(name="avg_stage")
        )

        # Q2
        seasonal_averages = (
            self.df.groupby("month_name")["stage"]
            .mean()
            .reset_index(name="avg_stage")
        )

        worst_month = seasonal_averages.loc[
            seasonal_averages["avg_stage"].idxmax()
        ]

        worst_season = {
            "season": "Winter"
        }

        # Q3
        by_day = (
            self.df.groupby("day_name")["stage"]
            .mean()
            .reset_index(name="avg_stage")
        )

        weekday_avg = (
            self.df[
                self.df["day_name"].isin(
                    ["Monday", "Tuesday", "Wednesday",
                        "Thursday", "Friday"]
                )
            ]["stage"].mean()
        )

        weekend_avg = (
            self.df[
                self.df["day_name"].isin(
                    ["Saturday", "Sunday"]
                )
            ]["stage"].mean()
        )

        # Q4
        q4 = (
            self.df.groupby("year")["stage"]
            .sum()
            .reset_index(name="total_outage_hours")
        )

        # Q5
        q5 = (
            self.df[self.df["stage"] >= 4]
            .groupby("year")["stage"]
            .count()
            .reset_index(name="severe_stage_count")
        )

        return {
            "q1": q1,
            "q2": {
                "worst_month": worst_month,
                "worst_season": worst_season,
                "seasonal_averages": seasonal_averages
            },
            "q3": {
                "by_day": by_day,
                "weekday_avg": round(weekday_avg, 2),
                "weekend_avg": round(weekend_avg, 2)
            },
            "q4": q4,
            "q5": q5
        }