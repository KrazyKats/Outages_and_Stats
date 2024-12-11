################################################################################
# Functions used in Project
################################################################################
import numpy as np
import pandas as pd
from plotly import express as px

def time_date_to_timestamp(data:pd.DataFrame) -> pd.DataFrame:
    data = data.copy()
    data["OUTAGE.START.TIME"] = pd.to_timedelta(data["OUTAGE.START.TIME"],)
    data["OUTAGE.RESTORATION.TIME"] = pd.to_timedelta(data["OUTAGE.RESTORATION.TIME"])
    return data

def time_to_datetime(data:pd.DataFrame) -> pd.DataFrame:
    data = time_date_to_timestamp(data)
    data["OUTAGE.START.DATE"] = data["OUTAGE.START.DATE"] + data["OUTAGE.START.TIME"]
    data["OUTAGE.RESTORATION.DATE"] = data["OUTAGE.RESTORATION.DATE"] + data["OUTAGE.RESTORATION.TIME"]
    return data

def diff_medians(data:pd.DataFrame, val_col: str, label_col :str) -> float:
    return data.groupby(label_col)[val_col].median().diff().iloc[-1]
