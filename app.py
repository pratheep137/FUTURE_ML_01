import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/kaggle/input/superstore-dataset-final/Sample - Superstore.csv", encoding='latin1')

print("Setup Complete") 

df.head(5)
df.isnull().sum()
df["State"].unique()
df.shape
df.info()

sales_stuation = df.groupby("State")["Sales"].sum().reset_index()
top15 = sales_stuation.sort_values('Sales', ascending=False).head(15)

plt.figure(figsize=(12,6))
sns.barplot(x='State', y='Sales', data=top15, palette='viridis')
plt.xticks(rotation=45, ha='right')  
plt.title('sales_stuation')
plt.tight_layout()
plt.savefig("sales_stuation.png")
plt.show()