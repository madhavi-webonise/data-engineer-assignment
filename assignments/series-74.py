import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns=list("abcd"))

print(pd.Series(df.values.ravel()).value_counts())
