import numpy as np
import pandas as pd

df = pd.DataFrame(
    [
        "STD, City State",
        "33, Kolkata West Bengal",
        "44, Chennai Tamil Nadu",
        "40, Hyderabad Telengana",
        "80, Bangalore Karnataka",
    ],
    columns=["row"],
)

print(df)

df_out = df.row.str.split(r",\s+", expand=True)

new_header = df_out.iloc[0]
df_out = df_out[1:]
df_out.columns = new_header
print(df_out)
