"""
Preprocessing module for Football ML Project
Author: Merey Mizangul
"""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from CSV file
    """
    df = pd.read_csv(path)
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Fill missing values using median strategy
    """
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    return df


def handle_outliers(df: pd.DataFrame, features: list) -> pd.DataFrame:
    """
    Handle outliers using IQR method
    """
    Q1 = df[features].quantile(0.25)
    Q3 = df[features].quantile(0.75)
    IQR = Q3 - Q1

    df[features] = df[features].clip(
        lower=Q1 - 1.5 * IQR,
        upper=Q3 + 1.5 * IQR,
        axis=1
    )
    return df


def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create new aggregated features
    """
    df["attack_score"] = (
        df["chanceCreationPassing"] +
        df["chanceCreationCrossing"] +
        df["chanceCreationShooting"]
    ) / 3

    df["defence_score"] = (
        df["defencePressure"] +
        df["defenceAggression"] +
        df["defenceTeamWidth"]
    ) / 3

    df["overall_custom"] = (
        df["attack_score"] + df["defence_score"]
    ) / 2

    return df


def preprocess_pipeline(path: str, features: list) -> pd.DataFrame:
    """
    Full preprocessing pipeline
    """
    df = load_data(path)
    df = handle_missing_values(df)
    df = handle_outliers(df, features)
    df = feature_engineering(df)
    return df

