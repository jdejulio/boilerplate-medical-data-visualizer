import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
csv_file = "medical_examination.csv"
df = pd.read_csv(csv_file)

#df["cholesterol"] = df.apply(lambda row: 1 if row["cholesterol"] == 1 or row["cholesterol"] == 2 or row["cholesterol"] == 3 else 0, axis=1)
#print(df[df["cholesterol"]==1])

#voy a sacar otra columna con el ciclo al que pertenecen (1 o 2) según el curso (1 y 2 para el ciclo 1)
data = {"nombre":["fulanito", "mengano", "pepe", "juan", "isabel"], "curso":[2, 3, 4, 1, 1]}
df = pd.DataFrame(data)
#df['ciclo'] = df['curso'].apply(lambda x: 1 if x in [1, 2] else (2 if x in [3, 4] else None))
#print(df)

def asigna_ciclo(curso):
    if curso in [1, 2]:
        return 1
    elif curso in [3, 4]:
        return 2
    else:
        return None
    
df["ciclo"] = df["curso"].apply(asigna_ciclo)
print(df)


