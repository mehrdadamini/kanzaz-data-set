import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer

def ReadData():
    df = pd.read_csv('train_test_data.csv')

    le =LabelEncoder()
    le.fit(df['Formation'])
    df['Formation'] = le.transform(df['Formation'])



    data = df.copy().drop(labels='Well Name', axis=1)

    imputer = KNNImputer(n_neighbors=5, weights="distance")
    data = imputer.fit_transform(data)
    df = np.c_[df['Well Name'].values, data]

    df = pd.DataFrame(df, columns = ['Well Name','Facies','Formation', 'Depth','GR','ILD_log10','DeltaPHI', 'PHIND','PE','NM_M','RELPOS'])
    
    df['Facies'] = np.array(df['Facies'], dtype=int)
    df['GR'] = np.array(df['GR'], dtype=float)
    df['ILD_log10'] = np.array(df['ILD_log10'], dtype=float)
    df['DeltaPHI'] = np.array(df['DeltaPHI'], dtype=float)
    df['PHIND'] = np.array(df['PHIND'], dtype=float)
    df['PE'] = np.array(df['PE'], dtype=float)
    df['Depth'] = np.array(df['Depth'], dtype=float)
    df['RELPOS'] = np.array(df['RELPOS'], dtype=float)
    df['NM_M'] = np.array(df['NM_M'], dtype=float)

    wells = df.groupby('Well Name')

    number = 1 
    for i in df['Well Name'].unique(): 
        globals()['well_number' + str(number)] = wells.get_group(i)
        number = number + 1
        
    return well_number1, well_number2, well_number3, well_number4, well_number5, well_number6, well_number7, well_number8, well_number9, well_number10, well_number11, well_number12, df['Well Name'].unique()

    
    