import pandas as pd
data = {
    "Name": ["Amit", "Priya", "Rahul"],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
df["Grade"] = ["A", "A+", "B"]
print(df)