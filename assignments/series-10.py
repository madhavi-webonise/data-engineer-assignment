import numpy as np
import pandas as pd

np.random.seed(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

top2 = ser.value_counts().index[:2]
print("Top 2 Freq:", ser.value_counts())
ser = ser.where(ser.isin(top2), other="Other")
print(ser)
