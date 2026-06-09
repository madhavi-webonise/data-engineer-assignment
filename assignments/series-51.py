import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10, -1), columns=list("abc"))

n = 5
print(df["a"].argsort()[::-1].iloc[n])
