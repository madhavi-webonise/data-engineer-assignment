from dateutil.parser import parse

import numpy as np
import pandas as pd

ser = pd.Series(
    [
        "01 Jan 2010",
        "02-02-2011",
        "20120303",
        "2013/04/04",
        "2014-05-05",
        "2015-06-06T12:20",
    ]
)

ser_ts = ser.map(lambda x: parse(x))

print("Date: ", ser_ts.dt.day.tolist())
print("Week number: ", ser_ts.dt.isocalendar().week.tolist())
print("Day num of year: ", ser_ts.dt.dayofyear.tolist())
print("Day of week: ", ser_ts.dt.day_name().tolist())
