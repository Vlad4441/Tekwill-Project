import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

def read_file2():
    data=pd.read_csv('Dataframe_original')
    data = data.drop(['Unnamed: 0'],axis=1)
    data=data.drop(['Grade'], axis=1)

    def concat(*args):
        strs = [str(arg) for arg in args if not pd.isnull(arg)]
        return ','.join(strs) if strs else np.nan
    np_concat = np.vectorize(concat)
    data['Clasa'] = np_concat(data['Clasa(L)'], data['Clasa(G)'])
    df = data.drop(columns=['Clasa(G)', 'Clasa(L)'])

    df['Weekly alcohol'] = df['Weekly alcohol'].fillna(1)
    df['Weekend alcohol'] = df['Weekend alcohol'].fillna(1)
    df['Profil'] = df['Profil'].fillna(float(1))
    df['Clasa'] = df.Clasa.astype('float64')
    return df

def process2(d):
    df = read_file2()
    #adauga la dataframe inputul de la user
    for i in d.keys():
        df.at[170, i] = d[i]

    df["Alcohol"] = (df['Weekly alcohol'] + df['Weekend alcohol']) / 2
    df["Alcohol"] = df.Alcohol.apply(lambda x: int(x))
    df = df.drop(['Weekly alcohol', 'Weekend alcohol'], axis=1)

    le = preprocessing.LabelEncoder()
    cols = ['Study time', 'School sup', 'Mom ed', 'Dad ed', 'Failiures', 'School extra', 'Trip time']
    for i in cols:
        df[i] = le.fit_transform(df[i])

    df_dummies=pd.get_dummies(df)

    scaler = MinMaxScaler()
    df_dummies = scaler.fit_transform(df_dummies)
    df_dummies = pd.DataFrame(df_dummies)
    np.random.seed(123)
    corr = df_dummies.corr()

    columns = np.full((corr.shape[0],), True, dtype=bool)
    for i in range(corr.shape[0]):
        for j in range(i + 1, corr.shape[0]):
            if corr.iloc[i, j] >= 0.85:
                if columns[j]:
                    columns[j] = False
    selected_columns = df_dummies.columns[columns]
    df_dummies = df_dummies[selected_columns]

    # creeaza din Dataframe array bidimensional
    ar = []
    for j in df_dummies.columns:
        ar.append(int(df_dummies.at[170, j]))
    #new_df_dummies.to_csv('df.csv',index=False)
    return [ar]