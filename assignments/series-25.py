import re

import numpy as np
import pandas as pd

emails = pd.Series(
    [
        "buying books at amazom.com",
        "rameses@egypt.com",
        "matt@t.co",
        "narendra@modi.com",
        "invalid-email@.com",
        "madhavi@haptiq.com",
    ]
)
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}"

mask = emails.map(lambda x: bool(re.match(pattern, x)))
print(emails[mask].tolist())
