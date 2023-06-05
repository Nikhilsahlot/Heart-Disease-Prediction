import streamlit as st
from sklearn.preprocessing import StandardScaler
import joblib
import numpy
# from tensorflow.keras.models import load_model

model = joblib.load('dt (3).C5')

st.write('Heart disease prediction')

age = float(st.number_input("Age", min_value=0, max_value=150, value=25))
sex = float(st.number_input("Sex", min_value=0, max_value=1, step=1, value=0))
cp = float(st.number_input("Chest Pain Type", min_value=0, max_value=4, step=1, value=0))
trestbps = float(st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=300, value=120))
chol = float(st.number_input("Serum Cholesterol (mg/dL)", min_value=0, max_value=1000, value=200))
fbs = float(st.number_input("Fasting Blood Sugar > 120 mg/dL", min_value=0, max_value=1, step=1, value=0))
restecg = float(st.number_input("Resting Electrocardiographic Results", min_value=0, max_value=2, step=1, value=0))
thalach = float(st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, value=150))
exang = float(st.number_input("Exercise Induced Angina", min_value=0, max_value=1, step=1, value=0))
oldpeak = float(st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0, step=0.1))
slope = float(st.number_input("Slope of Peak Exercise ST Segment", min_value=0, max_value=2, step=1, value=0))
ca = float(st.number_input("CA", min_value=0, max_value=4, step=1, value=0))
thal = float(st.number_input("Thalassemia", min_value=0, max_value=7, step=1, value=0))


features  = [age,sex,cp,trestbps,chol,fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]
# features = [-1.18272244,  0.64895597,  1.01170979, -0.08885372, -0.27021467,
#        -0.42209113,  0.92106058,  1.30164335,  1.38873015, -0.57054279,
#         0.97028605, -0.74195458, -0.5144228 ]
features = numpy.array(features)
features = features.reshape(1,-1)

# scaler = StandardScaler()
# features = scaler.fit_transform(features)


preds = model.predict(features)

if st.button('Predict'):
    if preds[0]==1:
        st.write("Disease detected")
    else:
        st.write("You are Safe")