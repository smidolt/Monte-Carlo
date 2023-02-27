import pandas as pd
import numpy as np
from tqdm import tqdm
days = pd.Series(range(365))
def birthday(n_people=10):
    return any(days.sample(n_people, replace=True).value_counts()>1)
n = 100000 #amount of cases
res = []
for _ in tqdm(range(n)):
    res.append(birthday())
print(np.mean(res))