import datacompy
import pandas as pd
import logging

# setup logging
logging.basicConfig(
    filename="logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

try:
    # reading in the data
    yesterday_deals_df = pd.read_csv("data\deals_2024-02-26.csv")
    today_deals_df = pd.read_csv("data\deals_2024-02-27.csv")

    # creating report object
    compare = datacompy.Compare(
        yesterday_deals_df,
        today_deals_df,
        on_index=True,
        df1_name="yesterday_deals",
        df2_name="today_deals",
    )

    # Generate the HTML report comparing all columns
    html_report = compare.report()

    # Save the HTML report to a file
    with open("reports/deals_comparison_report.html", "w") as f:
        f.write(html_report)

except Exception as e:
    logging.INFO(f"an error occurred {e}")
    raise e
