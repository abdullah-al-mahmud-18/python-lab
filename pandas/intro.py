import pandas as pd
import numpy as np

N = 10
LINE = "=" * 100
PRINT_INFO = False

series = pd.Series([1,2,4,3,np.nan, 10], dtype=np.float32)
print(series)

# TODO
# https://pandas.pydata.org/docs/user_guide/10min.html