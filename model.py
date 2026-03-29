import pandas as pd
import numpy as np
import pickle

from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split as tts

df = pd.read_csv("weather_classification_data.csv")

x = df.iloc[:,:-1]
y = df.iloc[:,-1]

x_train,x_test,y_train,y_test = tts(x,y,test_size=0.2,random_state=42)

cat_cols = ["Cloud Cover","Season","Location"]
num_cols = ["Temperature","Humidity","Wind Speed","Precipitation (%)","Atmospheric Pressure","UV Index","Visibility (km)"]

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), cat_cols),
        ('num', StandardScaler(),num_cols )
    ]
)

model = Pipeline([
    ('preprocessor', preprocessor),
    ('model', RandomForestClassifier())
])

model.fit(x_train,y_train)

pickle.dump(model, open("model.pkl", "wb"))