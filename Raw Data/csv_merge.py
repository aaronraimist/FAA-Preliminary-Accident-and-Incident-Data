import glob
import os

import pandas as pd

all_files = glob.glob(os.path.join(os.getcwd(), "faa_ai_prelim*.csv"))
df_from_each_file = [
    pd.read_csv(
        f,
        keep_date_col=True,
        infer_datetime_format=True,
        encoding="utf-8",
        #encoding_errors="backslashreplace",

        # doesn't work well since some data is invalid
        #parse_dates=[['EVENT_LCL_DATE', 'EVENT_LCL_TIME']],
        #date_parser=lambda self, col: pd.to_datetime(col, utc=True, errors="coerce"),
    )
    for f in all_files
]

df_merged = pd.concat(df_from_each_file, ignore_index=True)

# drop duplicate rows which have same EVENT_LCL_DATE and REGIST_NBR
df_merged.drop_duplicates(
    subset=["EVENT_LCL_DATE", "REGIST_NBR"], keep="last", inplace=True
)

# sort based on EVENT_LCL_DATE and EVENT_LCL_TIME
df_merged["EVENT_LCL_DATE_pddatetime"] = pd.to_datetime(df_merged["EVENT_LCL_DATE"])
df_merged["EVENT_LCL_TIME_pddatetime"] = pd.to_datetime(
    "1900-01-01 " + df_merged["EVENT_LCL_TIME"], errors="ignore"  # handle invalid times
)
df_merged.sort_values(
    by=["EVENT_LCL_DATE_pddatetime", "EVENT_LCL_TIME_pddatetime"], inplace=True
)
df_merged.drop(
    columns=["EVENT_LCL_DATE_pddatetime", "EVENT_LCL_TIME_pddatetime"], inplace=True
)

df_merged = df_merged.convert_dtypes()

df_merged.to_csv("../FAA-Accident-Incident-Data.csv", index=False)