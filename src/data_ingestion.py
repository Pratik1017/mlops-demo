import numpy as np
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/ApnaClassroom/Dataset/main/Customer%20Purchase.csv")

mapping = {
    "UG":"Under Graduate",
    "PG":"Post Graduate",
    "School":"School"
}

df['Education'] = df['Education'].map(mapping)

df.to_csv("data/version_one.csv")