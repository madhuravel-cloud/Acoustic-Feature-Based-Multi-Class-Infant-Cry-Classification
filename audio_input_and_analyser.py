import pandas as pd 
import opensmile
from sklearn.ensemble import RandomForestClassifier
def predict_audio(audio):
    model=RandomForestClassifier()
    audio.save("in.wav")
    data=pd.read_csv(r"C:\Users\user\dataset_features.csv")
    X=data.drop(columns=["file","label"])
    y=data["label"]
    model.fit(X,y) 
    smile = opensmile.Smile(
        feature_set=opensmile.FeatureSet.eGeMAPSv02,
        feature_level=opensmile.FeatureLevel.Functionals,
    )
    features = smile.process_file("in.wav")
    return model.predict(features)[0]
