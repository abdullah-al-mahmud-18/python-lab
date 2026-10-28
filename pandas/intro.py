import pandas as pd
import numpy as np

ROWS = 32
COLS = 8
LINE = "=" * 100
PRINT_INFO = False
COLS_LIST = [chr(c) for c in range(65, 65 + COLS)]


def write_to_console(anything):
    print(anything)
    print(LINE)

series = pd.Series([1,2,4,3,np.nan, ROWS], dtype=np.float32)
write_to_console(series)

dates = pd.date_range("2026-10-28", periods=ROWS)
write_to_console(dates)

data_frame = pd.DataFrame(np.random.randn(ROWS, COLS), index=dates, columns=COLS_LIST)
write_to_console(data_frame)

write_to_console(data_frame.to_numpy())

# TODO
# https://pandas.pydata.org/docs/user_guide/10min.html