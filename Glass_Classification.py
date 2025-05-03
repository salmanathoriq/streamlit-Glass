import pickle
import streamlit as st

model = pickle.load(open('Glass_Classification.sav', 'rb'))

st.title('Glass Classification App')

RI = st.number_input('Input Refractive Index (RI)')
Na = st.number_input('Input Sodium (Na)')
Mg = st.number_input('Input Magnesium (Mg)')
Al = st.number_input('Input Aluminum (Al)')
Si = st.number_input('Input Silicon (Si)')
K = st.number_input('Input Potassium (K)')
Ca = st.number_input('Input Calcium (Ca)')
Ba = st.number_input('Input Barium (Ba)')
Fe = st.number_input('Input Iron (Fe)')


predict =  ''

if st.button('Classify Glass Type'):
    features = [[RI, Na, Mg, Al, Si, K, Ca, Ba, Fe]]
    prediction = model.predict(features)
    st.write('Predicted Glass Type:', prediction)