import pandas as pd
data = pd.read_csv("data.csv")
print(data)
data['quantity'] = data['quantity'].fillna(data['quantity'].mean())
print(data)
data['price'] = data['price'].fillna(data['price'].median())
print(data)
data['bought'] = data['bought'].fillna(data['bought'].std())
print(data)
data['forenoon'] = data['forenoon'].fillna(data['forenoon'].min())
print(data)
data['afternoon'] = data['afternoon'].fillna(data['afternoon'].max())
print(data)



"""
Step-1: Upload the file

Step-2: In "Preprocess" tab Click on the "Choose" button under the "Filter" section.

Step-3: Navigate to filters -> unsupervised -> attribute -> ReplaceMissingValues.

Step-4: After selecting the ReplaceMissingValues filter, click on the "Apply" button.

"""