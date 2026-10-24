import pandas as pd
import numpy as np

N = 10
LINE = "=" * 100
PRINT_INFO = False

URL = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(URL, sep="\t")

if PRINT_INFO:
    print(f"First {N} rows\n{chipo.head(N)}")
    print(f"Shape: {chipo.shape}")
    print(f"Info:\n{chipo.info}")
    print(f"Columns: {chipo.columns}")
    print(f"Index: {chipo.index}")
    print(LINE)


# TODO
# https://github.com/guipsamora/pandas_exercises/blob/master/01_Getting_%26_Knowing_Your_Data/Chipotle/Exercise_with_Solutions.ipynb
