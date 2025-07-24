# 📊 Telco Customer Churn - Data Preprocessing Pipeline

Automated data preprocessing pipeline untuk dataset Telco Customer Churn menggunakan GitHub Actions dengan exploratory data analysis (EDA) dan feature engineering.

## 🎯 Overview

Pipeline ini secara otomatis:
- ✅ Preprocessing data mentah dari CSV
- ✅ Handle missing values dan data cleaning
- ✅ Feature encoding (Label & One-Hot)
- ✅ Standardization untuk numerical features
- ✅ Auto-commit hasil preprocessing

## 📁 Project Structure

```
.
├── .github/workflows/main.yml           # CI/CD preprocessing pipeline
├── dataset_raw/
│   └── Telco-Customer-Churn.csv        # Raw dataset
├── preprocessing/
│   ├── automate_Moch-Rifky-Aulia_Adikusumah.py    # Automation script
│   ├── Eksperimen_Moch-Rifky-Aulia_Adikusumah.ipynb # EDA notebook
│   └── Telco-Customer-Churn_preprocessing.csv      # Processed data
└── README.md
```

## 🚀 Quick Start

### Automatic Processing
1. Push ke repository
2. GitHub Actions otomatis menjalankan preprocessing
3. Hasil preprocessing di-commit ke `preprocessing/`

### Manual Processing
```bash
# Clone repository
git clone https://github.com/rifkyadiii/Eksperimen_SML_Moch-Rifky-Aulia-Adikusumah.git
cd Eksperimen_SML_Moch-Rifky-Aulia-Adikusumah

# Install dependencies
pip install pandas scikit-learn matplotlib seaborn jupyter

# Run preprocessing script
python preprocessing/automate_Moch-Rifky-Aulia_Adikusumah.py

# Or explore dengan Jupyter notebook
jupyter notebook preprocessing/Eksperimen_Moch-Rifky-Aulia_Adikusumah.ipynb
```

## 🔧 Data Preprocessing Steps

### 1. **Missing Values Handling**
- Convert `TotalCharges` to numeric
- Fill missing values dengan median

### 2. **Feature Engineering**
- Drop `customerID` (tidak relevan)
- Identify binary vs multi-class categorical features

### 3. **Encoding**
- **Label Encoding**: Binary features + target variable
- **One-Hot Encoding**: Multi-class categorical features

### 4. **Normalization**
- **StandardScaler**: `tenure`, `MonthlyCharges`, `TotalCharges`

## 📈 Dataset Information

- **Source**: Telco Customer Churn (Kaggle)
- **Rows**: ~7,000 customers
- **Features**: 21 columns
- **Target**: `Churn` (Yes/No)

### Feature Categories:
- **Demographic**: `gender`, `SeniorCitizen`, `Partner`, `Dependents`
- **Services**: `PhoneService`, `InternetService`, `OnlineSecurity`, etc.
- **Account**: `tenure`, `Contract`, `PaymentMethod`, `MonthlyCharges`

## 📊 Exploratory Data Analysis

Notebook mencakup:
- **Data Overview**: Info, shape, missing values
- **Target Distribution**: Churn vs Non-churn ratio
- **Numerical Features**: Histograms dengan KDE
- **Categorical Analysis**: Countplots by churn status
- **Statistical Summary**: Descriptive statistics

### Key Insights:
- Customer dengan contract month-to-month lebih cenderung churn
- Electronic check payment method berkorelasi dengan churn
- Fiber optic internet users memiliki churn rate lebih tinggi

## 🤖 Automated Workflow

GitHub Actions pipeline:
```yaml
1. Checkout repository
2. Setup Python 3.10
3. Install dependencies (pandas, scikit-learn)
4. Run preprocessing script
5. Auto-commit processed data
```

## 🔍 Output Files

### `Telco-Customer-Churn_preprocessing.csv`
- **Ready-to-use** dataset untuk machine learning
- **Cleaned & encoded** features
- **Standardized** numerical values
- **No missing values**

## 📝 Usage for ML Projects

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Load preprocessed data
df = pd.read_csv('preprocessing/Telco-Customer-Churn_preprocessing.csv')

# Split features and target
X = df.drop('Churn', axis=1)
y = df['Churn']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Ready for model training!
```

## 🛠️ Dependencies

```txt
pandas>=1.5.0
scikit-learn>=1.3.0
matplotlib>=3.6.0
seaborn>=0.12.0
numpy>=1.24.0
```

## 🔄 Continuous Integration

- **Trigger**: Setiap push ke repository
- **Auto-processing**: Script berjalan otomatis
- **Version control**: Hasil preprocessing di-track di Git
- **No manual intervention**: Fully automated pipeline

## 🎓 Educational Value

Perfect untuk:
- **Data Science students** learning preprocessing
- **ML practitioners** needing clean datasets
- **Automation enthusiasts** studying CI/CD for data

---

> 🚀 **Ready-to-use**: Dataset siap digunakan untuk training model churn prediction!
