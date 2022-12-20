import pandas as pd

from src.distribution import compute_distribution_1_week


def test_compute_distribution_1_week():
    """Test compute 1 week distribution

    In this test case:
    - We have 1 brand that is sold by 1 bar -> distribution is 100% every week
    when this bar sells
    - We have 1 brand sold by 2 bars. bar_A makes 75% of market share.
    Distribution is 100% when both bars sell. It's 75% when only bar 1 sells

    Tests are composed of 4 steps:
    - "Setup": when we create variables & conditions to run the code
    - "Act": when we run the code
    - "Assert": when we check that the code had the right result
    - "Tear down": (optional) doing the cleaning

    The code will be comment to show the various steps
    """
    # --- Set up ---
    # Creating variables "input sales" and "output expected"
    df_sales = pd.read_csv("tests/assets/sales.csv")
    df_distribution_expected = pd.read_csv("tests/assets/result_compute_distribution.csv")

    # --- Act ---
    # Compute distribution with the input sales
    df_res = compute_distribution_1_week(df_sales)

    # --- Assert ---
    # Checking that our result is what we wanted
    pd.testing.assert_frame_equal(df_distribution_expected, df_res)

    # --- Tear down ---
    # No teardown is needed here
