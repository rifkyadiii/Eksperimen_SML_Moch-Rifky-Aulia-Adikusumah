import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def preprocess_data(input_path, output_path):
    """
    Membaca data mentah, melakukan preprocessing, dan menyimpan hasilnya.
    """
    df = pd.read_csv(input_path)

    # 1. Handle TotalCharges
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    median_total_charges = df['TotalCharges'].median()
    df['TotalCharges'].fillna(median_total_charges, inplace=True)

    # 2. Drop Unnecessary Column
    df.drop('customerID', axis=1, inplace=True)

    # 3. Encoding
    binary_cols = [col for col in df.columns if df[col].nunique() == 2 and col != 'Churn']
    multi_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].nunique() > 2]

    le = LabelEncoder()
    for col in binary_cols + ['Churn']:
        df[col] = le.fit_transform(df[col])

    df = pd.get_dummies(df, columns=multi_cols, drop_first=True)

    # 4. Scaling
    scaler = StandardScaler()
    numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
    df[numerical_features] = scaler.fit_transform(df[numerical_features])

    # 5. Save
    df.to_csv(output_path, index=False)
    print(f"Data yang telah diproses disimpan di: {output_path}")

if __name__ == "__main__":
    raw_data_path = 'dataset_raw/Telco-Customer-Churn.csv'
    processed_data_path = 'preprocessing/Telco-Customer-Churn_preprocessing.csv'
    preprocess_data(raw_data_path, processed_data_path)