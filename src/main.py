import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import os

# Get the absolute path of the model file
model_path = os.path.join(os.path.dirname(__file__), "../model/aqi_model.pkl")

# Normalize the path to handle different OS path styles
model_path = os.path.abspath(model_path)
# Streamlit App Title
st.title("AQI Prediction Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file for prediction", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, encoding="ISO-8859-1", dtype=str)
    st.subheader("Data Preview")
    st.write(df.head())
    # Compute AQI based on your formula before training
    df['aqi'] = df['no2'].astype(float) * 0.5 + df['so2'].astype(float) * 0.3 + df['rspm'].astype(float) * 0.2

    # Feature Selection
    feature_cols = ['so2', 'no2', 'rspm', 'spm', 'pm2_5', 'aqi']
    # for col in ['so2', 'no2', 'rspm', 'spm', 'pm2_5', 'aqi']:
    #   df[col] = pd.to_numeric(df[col], errors='coerce')

    if all(col in df.columns for col in feature_cols):
        X = df[['so2', 'no2', 'rspm', 'spm', 'pm2_5']]  # Ensure exactly 5 features
        X = X.to_numpy()  # Convert DataFrame to NumPy array before passing to model

        # Load or Train Model
        try:
            with open(model_path, "rb") as f:
                model = pickle.load(f)
        except FileNotFoundError:
            st.warning("Training a new model as no pre-trained model is found.")
            y = df['aqi'] if 'aqi' in df.columns else None
            if y is not None:
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
                model = RandomForestRegressor(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)
                with open("aqi_model.pkl", "wb") as f:
                    pickle.dump(model, f)
        
        # Make Predictions
        df['Predicted AQI'] = model.predict(X)
        
        st.subheader("Predictions")
        st.write(df[['Predicted AQI']].head())
        
        # Model Performance Metrics (if actual AQI is available)
        if 'aqi' in df.columns:
            y_actual = df['aqi'].dropna()
            y_pred = df['Predicted AQI'].iloc[y_actual.index]  # Ensure matching indices

            mae = mean_absolute_error(y_actual, y_pred)
            mse = mean_squared_error(y_actual, y_pred)
            rmse = mse ** 0.5
            r2 = r2_score(y_actual, y_pred)

            st.subheader("Model Performance Metrics")
            st.write(f"📌 **Mean Absolute Error (MAE):** {mae:.2f}")
            st.write(f"📌 **Mean Squared Error (MSE):** {mse:.2f}")
            st.write(f"📌 **Root Mean Squared Error (RMSE):** {rmse:.2f}")
            st.write(f"📌 **R² Score:** {r2:.2f}")
            print("Actual AQI:", y_actual.head())
            print("Predicted AQI:", y_pred.head())

            # Scatter Plot: Actual vs Predicted AQI
            st.subheader("Actual vs Predicted AQI")
            fig, ax = plt.subplots()
            ax.scatter(y_actual, y_pred, alpha=0.6, edgecolors='white', color='blue')
            ax.plot([y_actual.min(), y_actual.max()], [y_actual.min(), y_actual.max()], 'r--', lw=2)  # Line for reference
            ax.set_xlabel("Actual AQI")
            ax.set_ylabel("Predicted AQI")
            ax.set_title("Actual vs Predicted AQI")
            plt.tight_layout()
            st.pyplot(fig)
    else:
        st.error("Uploaded CSV must contain the required feature columns: 'so2', 'no2', 'rspm', 'spm', 'pm2_5'")
