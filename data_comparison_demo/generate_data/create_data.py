import pandas as pd
import pyarrow
from faker import Faker
import numpy as np
import random
from datetime import datetime

# timestamp used to create a dataset.
CURRENT_DATE = datetime.now().date()


def create_data(size=None):
    # init faker
    faker = Faker()

    # Initialize an empty DataFrame
    df = pd.DataFrame()

    # Generate fake data for each record
    for _ in range(size):
        # Create a dictionary for each record
        record = {
            "deal_id": faker.uuid4(),
            "deal_start_ts": faker.date_time_this_decade(),
            "applicant_name": faker.name(),
            "applicant_email": faker.email(),
            "applicant_address": faker.address(),
            "applicant_phone_number": faker.phone_number(),
            "deal_amount": random.randint(1000, 100000),
            "status": random.choice(["complete", "pending", "cancelled"]),
            "deal_end_ts": random.choice(["9999-12-31", ""]),
        }
        # Append the record to the DataFrame
        df = df._append(record, ignore_index=True)

        # save as a parquet file
        df.to_csv(f"../data/deals_{CURRENT_DATE}.csv")

    return df


deals_df = create_data(100)
print(deals_df)
