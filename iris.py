import streamlit as st
from joblit import load

model = load('data/iris_model.joblib')

col1,col2 = st.columns(2)

with col1:
    sepal_len = st.number_input('Sepal len')
    sepal_width = st.number_input('Sepal width')
    
with col2:
    petal_len = st.number_input('Petal len')
    petal_width = st.number_input('Petal width')

prediction = model.predict([[1,2,3,4]])

sepal_len = st.number_input('Sepal len')
sepal_width = st.number_input('Sepal width')
petal_len = st.number_input('Petal len')
petal_width = st.number_input('Petal width')

if st.button("Predict"):
    prediction = model.predict([[Sepal_len,
                                 Sepal_width,
                                 Petal_len,
                                 Petal_width]])[0]
    
    if prediction == 0:
        image = Images.open('images/iris_setosa.png')
    
    elif prediction == 1:
        image = Images.open('images/iris_versicolor.png')
        
    else:
         image = Images.open('images/iris_virginica.png')
            
    st.image(image)
     