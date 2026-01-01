# 🔥 CALORIES BURNT PREDICTION USING MACHINE LEARNING🔥

# 📌 OVERVIEW

This project is a end-to-end **Machine Learning application** that predicts the number of **calories burnt** during a workout based on various physiological and activity parameters. It leverages **Scikit-learn** for data preprocessing and model evaluation, uses an **XGBoost Regressor** for accurate predictions, and employs **Joblib** for efficient model serialization. The interactive web interface is built and deployed using **Streamlit**.

---

## 📂 PROJECT STRUCTURE

* **`app.py`**: The main Streamlit application script that serves the user interface.
* **`final_model.py`**: Python script used to train the final XGBoost model and save it as `model.pkl`.
* **`model.pkl`**: The serialized, pre-trained machine learning model (XGBoost) used for making predictions in the app.
* **`eda.ipynb`**: Jupyter Notebook containing Exploratory Data Analysis (EDA) to visualize data distributions, check for outliers, and understand correlations.
* **`model_evaluation.ipynb`**: Jupyter Notebook for evaluating different machine learning models and fine-tuning hyperparameters.
* **`requirements.txt`**: A text file listing the Python dependencies required to run the project.
* **Datasets**:
  * `calories.csv`: Raw dataset containing calorie burn information.
  * `exercise.csv`: Raw dataset containing exercise parameters (duration, heart rate, etc.).
  * `data_with_outliers.csv`: The merged dataset combining exercise and calorie data (includes detected outliers).
  * `data_without_outliers.csv`: Cleaned dataset with outliers removed, used for training the final model.

---

## 📊 EXPLORATORY DATA ANALYSIS

* **Data Overview**: Merged `exercise.csv` and `calories.csv` (15k samples). Dropped `User_ID` as it's not predictive.
* **Feature Distribution**:
  * **Gender**: Balanced dataset (Female: 7553, Male: 7447).
  * **Age**: Right-skewed distribution, more younger individuals (20-30s).
  * **Height & Weight**: Roughly normal distributions.
* **Key Correlations**:
  * **Duration vs Calories**: Extremely high positive correlation.
  * **Heart Rate vs Calories**: Strong positive correlation.
* **Outlier Handling**:
  * Boxplots identified outliers in `Heart_Rate` and `Body_Temp`.
  * Applied **Interquartile Range (IQR)** method to clip outliers, improving model stability.
  * Created `data_without_outliers.csv` for final model training.

---

## 🛠️ FEATURES

* **Interactive Web App**: Built with Streamlit, offering a responsive and visually appealing "Dark Gym" themed interface.
* **Real-time Prediction**: Users can input their details via sliders and get instant calorie burn predictions.
* **High Accuracy**: Utilizes an XGBoost Regressor model trained on cleaned data for precise estimation.
* **Visualizations**: The notebooks include various plots (correlation heatmaps, distribution plots) to understand the underlying data.

---

## 🚀 INSTALLATION & USAGE

### Prerequisites

* Python 3.8 or higher is recommended.
* pip (Python package installer).

### Steps

1. **Navigate to the project directory**:

   ```bash
   cd "Calories Burnt Prediction"
   ```
2. **Install Dependencies**:
   Install the required Python libraries using `pip`.

   > **Note:** Ensure `streamlit` is installed as it is required to run the app.
   >

   ```bash
   pip install -r requirements.txt
   pip install streamlit
   ```
3. **Run the Application**:
   Launch the Streamlit app with the following command:

   ```bash
   streamlit run app.py
   ```

   The app should automatically open in your default web browser.

---

## 🧠 MODEL PERFORMANCE

We compared four regression models to select the best predictor:

* **Linear Regression**: High error (MAE ~8.3).
* **Decision Tree**: Good but prone to overfitting.
* **Random Forest**: Very robust (MAE ~1.7).
* **XGBoost (Selected)**: Best performance (MAE ~1.48) and accuracy (>99%).

### Final Configuration

The prediction model uses the **XGBoost** algorithm with the following configuration (as seen in `final_model.py`):

* **Algorithm**: XGBRegressor
* **Estimators**: 300
* **Learning Rate**: 0.05
* **Max Depth**: 6
* **Objective**: `reg:squarederror`

---

## 🎨 UI/UX DESIGN & CHALLENGES

Creating a custom "Dark Gym" theme in Streamlit presented specific challenges:

* **No Native Classes**: Streamlit widgets don't accept custom CSS classes, requiring internal ID targeting.
* **Global Scope**: Injected CSS styles generally affect the entire app, making component isolation difficult.
* **Responsiveness**: Custom `@media` queries were implemented to override Streamlit's default padding for mobile devices.

---

## 📊 DATA INPUTS

The model predicts calories based on the following 7 input features:

* **Gender**: Male / Female
* **Age**: 20 - 79 years
* **Height**: 130 - 220 cm
* **Weight**: 35 - 130 kg
* **Duration**: 1 - 30 minutes
* **Heart Rate**: 65 - 130 bpm
* **Body Temperature**: 38 - 42 °C

---

## 🎉 CONCLUSION

* **End-to-End Solution**: Demonstrates a complete ML workflow, from rigorous data analysis and XGBoost model tuning to a deployed, real-time prediction app.
* **User-Centric Design**: Features a responsive "Dark Gym" aesthetic that makes advanced machine learning accessible, practical, and engaging for fitness enthusiasts.

---

*Made with 💝 by [PRANAV](https://www.linkedin.com/in/pranavchoubey89)*
