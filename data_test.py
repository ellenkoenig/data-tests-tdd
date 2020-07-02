import pandas as pd
import pandas.api.types as ptypes


def test_length_of_df_should_not_be_zero():
    df = pd.read_csv("part-00000-4c8de288-2713-4e86-b5a5-a44ad4badba5-c000.csv", error_bad_lines=False)
    assert len(df) > 0


def test_lines_should_contain_numbers():
    df = pd.read_csv("part-00000-4c8de288-2713-4e86-b5a5-a44ad4badba5-c000.csv", error_bad_lines=False)
    assert all(ptypes.is_numeric_dtype(df[col]) for col in df)


