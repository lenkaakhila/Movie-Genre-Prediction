
import streamlit as st
import pickle
import numpy as np

# Load the trained model and label encoders
try:
    model = pickle.load(open("genre_prediction_model.pkl","rb"))
    # In a real application, you would also load the label encoder for 'listed_in'
    # to transform the numerical prediction back into the actual genre name.
    # For this example, we assume the model directly predicts the encoded genre index.
    # For example, if le_filtered_y was saved: le_filtered_y = pickle.load(open("le_filtered_y.pkl","rb"))
except FileNotFoundError:
    st.error("Error: Model file 'genre_prediction_model.pkl' not found. Please ensure it's in the same directory.")
    st.stop() # Stop the app if the model isn't found

# Assuming the label encoder for 'listed_in' (y_filtered_encoded) was saved
# You might need to adjust the path or name if it was saved differently
try:
    # This part requires the actual le_filtered_y to be saved.
    # For simplicity, we'll assume we return the encoded label if it's not available.
    pass # Placeholder if le_filtered_y is not available in current execution
except FileNotFoundError:
    st.warning("Label encoder for genres not found. Returning numerical prediction.")

st.title("Movie Genre Prediction App")
st.write("Enter movie details to predict the genre")

# Based on feature importance and the X_scaled used, we need 10 features.
# The order and meaning of these features are crucial.
# These inputs should represent the preprocessed (encoded and scaled) features.
feature_names = [
    'type_encoded', 'director_encoded', 'cast_encoded', 'country_encoded',
    'date_added_encoded', 'release_year', 'rating_encoded', 'duration_encoded',
    'description_encoded', 'platform_encoded'
]

feature_values = []
for i, name in enumerate(feature_names):
    feature_values.append(st.number_input(f"Enter value for {name}", key=f"feature_{i}"))

if st.button("Predict Genre"):
    if len(feature_values) == 10:
        try:
            input_features = np.array([feature_values]).reshape(1, -1)
            prediction_encoded = model.predict(input_features)[0]

            # If le_filtered_y was loaded, you'd do:
            # predicted_genre_name = le_filtered_y.inverse_transform([prediction_encoded])[0]
            # st.success(f"Predicted Genre: {predicted_genre_name}")
            st.success(f"Predicted Genre (encoded): {prediction_encoded}")

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.error(f"Please ensure all {len(feature_names)} feature inputs are provided.")
