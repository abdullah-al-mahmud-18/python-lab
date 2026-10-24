import pandas as pd
import numpy as np

URL = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"
chipo = pd.read_csv(URL, sep="\t")

print(chipo.head())
