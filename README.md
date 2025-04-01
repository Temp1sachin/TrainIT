# 🌍 Impact-X: Climate Change Analysis

## 🚀 Hackathon: TrainIT - Where Data Meets Creativity

**🏫 Organizer:** Army Institute of Technology (AIT), Pune\
**📌 Track:** ImpactX\
**👥 Team:** 3 Peas in a Pod

## 📖 Project Description

This project utilizes data science to analyze climate change factors such as air quality and rainfall patterns. The aim is to provide insights through Exploratory Data Analysis (EDA) and predictive modeling to assess environmental sustainability.

## 📊 Datasets Used

The datasets provided by the organizers are:

1. **🌫️ Air Quality Data in India** – Central Pollution Control Board (CPCB)\
   [📂 Kaggle Link](https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data)
2. **🌧️ India Rainfall Data (1901-Present)** – IMD Climate Data\
   [📂 Kaggle Link](https://www.kaggle.com/datasets/saisaran2/rainfall-data-from-1901-to-2017-for-india)

## 📁 Project Structure

```
├── 📂 data
│   ├── dataset.csv
│   ├── merged_dataset.csv  # 🔄 Generated dynamically when running 3 (merging_datasets).ipynb
│   ├── Rainfall_Data_LL.csv
│
├── 🤖 model
│   ├── aqi_model.pkl  # 🔄 Model will be generated upon execution
│
├── 📓 notebook
│   ├── 1 (eda_aqi_analysis).ipynb
│   ├── 2 (training_aqi).ipynb  # 🏋️‍♂️ Runs training and saves the model
│   ├── 3 (merging_datasets).ipynb  # 🔗 Merges datasets
│
├── 🖥️ src
│   ├── stream.py  # 🎨 Streamlit application for visualization
│
├── .gitignore
├── README.md
├── requirements.txt
```

## 📌 Deliverables

- 📊 **Exploratory Data Analysis (EDA)** with visualizations.
- 🔮 **Predictive model** for analyzing air quality trends (generated dynamically when running `2 (training_aqi).ipynb`).
- 🔗 **Merged dataset** (generated dynamically when running `3 (merging_datasets).ipynb`).
- 📜 **Social impact report** summarizing insights.

## 🛠️ Tools & Technologies

- **💻 Programming Language:** Python
- **📚 Libraries:** Pandas, NumPy, Matplotlib, Scikit-learn
- **🎨 Visualization:** Streamlit

## ⚠️ Constraints

- 🚫 Only the provided dataset is used.
- 🚫 No external datasets or pre-trained models.

## ▶️ How to Run the Project

1. 🔧 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. 📓 Run Jupyter notebooks for EDA and model training:
   - Execute `1 (eda_aqi_analysis).ipynb` for data analysis.
   - Execute `2 (training_aqi).ipynb` to train and save the model.
   - Execute `3 (merging_datasets).ipynb` to generate the merged dataset.
3. 🎨 Start the Streamlit application:
   ```bash
   streamlit run src/stream.py
   ```

## 🔮 Future Improvements

- 📈 Expanding dataset coverage.
- 🤖 Enhancing predictive modeling techniques.
- 🌐 Incorporating real-time data for dynamic analysis.

---

## 👥 Contributors

- **Asmi Srivastava, Aameya Devansh, Sachin Mishra** (3 Peas in a Pod) 🌱

