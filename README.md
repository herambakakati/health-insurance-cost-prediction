# 💰 Medical Insurance Cost Prediction

Mini Project – Supervised Machine Learning
**By: Heramba Kakati (Batch 13)**

## 🚀 About the Project

This project is about predicting **medical insurance costs** using machine learning.
Based on details like age, BMI, smoking habit, etc., the model estimates how much insurance a person might be charged.

The goal is to build a model that is **accurate, reliable, and practically useful**.

## 📊 Dataset

* Total records: **1337 (after removing duplicates)** 
* Features used:

  * Age
  * Sex
  * BMI
  * Children
  * Smoker
  * Region
* Target:

  * Charges (insurance cost)

✔ No missing values
✔ Data is clean and ready to use

## 🔍 What I Found (EDA Insights)

* Insurance charges are **not normally distributed (skewed)**
* **Smokers pay much higher charges** than non-smokers 
* **Age and BMI** increase insurance cost
* Number of children has very little impact

## ⚙️ Data Preparation

To improve the model:

* Removed duplicate rows
* Converted categorical data using encoding
* Scaled numerical features
* Applied log transformation:

```latex id="tx8d2a"
y = \log(1 + charges)
```

This helped reduce skewness and improve accuracy.

## 🤖 Models I Tried

I tested multiple models:

* Linear Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* SVR (Support Vector Regression)
* KNN

## 🏆 Best Model: SVR

After comparing all models, **SVR performed the best**.

### 📈 Performance

* Train R²: **0.828**
* Test R²: **0.880** 
* Adjusted R²: **0.876**

✔ No overfitting
✔ Good accuracy

## 🔧 Hyperparameter Tuning

Used:

* GridSearchCV
* RandomizedSearchCV

Result:

* Performance stayed around **0.88**, meaning the model was already well-optimized.

## 📊 Model Comparison

| Model             | Test R² | Overfitting |
| ----------------- | ------- | ----------- |
| SVR               | 0.880   | No          |
| Gradient Boosting | 0.878   | No          |
| Random Forest     | 0.842   | Yes         |
| Linear Regression | 0.829   | No          |
| KNN               | 0.733   | Yes         |
| Decision Tree     | 0.699   | Yes         |

## 🌐 Streamlit App

I also created a simple web app using **Streamlit**.

User inputs:

* Age
* BMI
* Children
* Sex
* Smoker
* Region

👉 Output: Predicted insurance cost (₹)

## ▶️ How to Run

```bash id="run88"
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Real-World Use

* Helps estimate insurance cost quickly
* Useful for insurance companies
* Identifies high-risk people (like smokers) 

## ✅ Final Conclusion

* Data was skewed → fixed using log transformation
* Smoking is the most important factor
* SVR gives the best results

👉 Final Model: **SVR**


