## ⚙️ Technologies Used
- **Language:** Python
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Tools:** Jupyter Notebook, VS Code, Git

## 🔍 Approach
1. **Data Ingestion** — Loaded dataset and split into train/test sets
2. **Data Transformation** — Handled missing values, applied encoding and scaling via pipelines
3. **Model Training** — Trained and compared multiple algorithms (Linear Regression, Decision Tree, Random Forest, CatBoost)
4. **Hyperparameter Tuning** — Used `GridSearchCV` / `RandomizedSearchCV` for optimization
5. **Evaluation** — Selected best model based on R² score

## 📊 Results
| Metric | Score |
|--------|-------|
| Best Model | CatBoost Regressor |
| R² Score | ~0.88 |

## 🚀 Future Improvements
- Deploy as a Flask web application on AWS Elastic Beanstalk
- Add a student-facing UI for real-time predictions
- Experiment with neural network-based models
