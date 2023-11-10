import pytest
import pandas as pd
import os

def compare_dataframes(df1, df2):
    """
    Compare two dataframes are exactly the same
    """
    assert df1.columns.tolist() == df2.columns.tolist()
    assert df1.shape == df2.shape
    if df1.shape[0] > 0:
        assert df1.equals(df2)

def evaluate_result(path_to_csv, path_to_expected_csv):
    """
    Compare the result of the query with the expected result
    """
    if not os.path.exists(path_to_csv):
        assert False
    df = pd.read_csv(path_to_csv)
    df_expected = pd.read_csv(path_to_expected_csv)
    compare_dataframes(df, df_expected)
