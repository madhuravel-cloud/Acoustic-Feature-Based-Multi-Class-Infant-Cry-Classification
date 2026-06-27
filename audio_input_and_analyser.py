import pandas as pd 
import opensmile
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier()
data=pd.read_csv(r"C:\Users\user\dataset_features.csv")
X=data.drop(columns=["file","label"])
y=data["label"]
model.fit(X,y) 
smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.eGeMAPSv02,
    feature_level=opensmile.FeatureLevel.Functionals,
)
path=r"C:\Users\user\Downloads\inf dataset\Baby Cry Dataset\hungry\ad7fd28b-3e85-4e9b-9e18-af4bda64c60f-1430756389867-1.7-m-72-hu.wav"
features = smile.process_file(path)
print(model.predict(features)[0])