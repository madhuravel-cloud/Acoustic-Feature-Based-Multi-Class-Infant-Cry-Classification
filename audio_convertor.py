import opensmile
import pandas as pd
import os
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)
data = []

for root, dirs, files in os.walk(r"C:\Users\user\Downloads\inf dataset\Baby Cry Dataset"):
    for file in files:
        if file.endswith(".wav"):
            path = os.path.join(root, file)

            label = os.path.basename(root)

            features = smile.process_file(path)

            row = features.iloc[0].to_dict()
            row["file"] = file
            row["label"] = label

            data.append(row)

df = pd.DataFrame(data)
df.to_csv("dataset_features.csv", index=False)