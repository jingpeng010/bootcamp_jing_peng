import numpy as np


def add_log_transactions(df):
    df = df.copy()
    df["log_transactions"] = np.log1p(df["transactions"])
    return df


def add_spend_per_transaction(df):
    df = df.copy()
    df["spend_per_transaction"] = (
        df["spend"] / df["transactions"].replace(0, np.nan)
    )
    return df


def add_spend_7d_mean(df):
    df = df.copy()
    df["spend_7d_mean"] = (
        df["spend"]
        .rolling(window=7, min_periods=1)
        .mean()
    )
    return df


def add_region_frequency(df):
    df = df.copy()
    region_freq = df["region"].value_counts(normalize=True)
    df["region_freq"] = df["region"].map(region_freq)
    return df