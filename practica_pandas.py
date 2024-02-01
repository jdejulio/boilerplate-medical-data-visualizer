import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn
"""
# Crear diferentes tipos de datos
labels = ['a','b','c'] # lista de eetiquetas
my_list = [10,20,30] # lista con valores
arr = np.array([10,20,30]) # Convertir ista de valores en arreglo NumPy
d = {'a':10,'b':20,'c':30} # Creacion de un diccionario

# Convertir una lista en series usando el metodo pd.Series
# observe que se crean los nombres con las posiciones de cada elemento
serie1 = pd.Series(my_list)

# Convertir una lista en series usando el metodo pd.Series
# se puede ingresar el nombre de las posiciones
serie2 = pd.Series(data=my_list,index=labels)

# Creacion de una serie con sus labels o indices
ser1 = pd.Series([1,2,3,4], index = ['USA', 'Alemania','Italia', 'Japon'])                                   




#############
#####DATAFRAMESSSSSSS
#############

# Importar la funcion de NumPy para crear arreglos de numeros enteros
##from numpy.random import randn
np.random.seed(101) # Inicializar el generador aleatorio

# Forma rapida de crear una lista de python desde strings
'A B C D E F'.split()

['A', 'B', 'C', 'D', 'E']

# Crear un dataframe con numeros aleatorios de 4 Columnas y 6 Filas
# Crear listas rapidamente usando la funcion split 'A B C D E'.split()
# Esto evita tener que escribir repetidamente las comas

df_sinuso = pd.DataFrame(randn(6,4),
                  index='A B C D E F'.split(),
                  columns='W X Y Z'.split())

###############
####INSERTANDO CSV
###############

archivo = "sample.csv"
df2 = pd.read_csv(archivo)

##########
###A MANITAAA
########## CON Agrupación por variable dentro del DF

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',

                              'Parrot', 'Parrot'],

                   'Max Speed': [380., 370., 24., 26.]})


df.groupby(['Animal']).mean()
#print(df.groupby(['Animal']).mean())


#df = pd.DataFrame({"cholesterol":[1, 0, 1, 1, 0],
#                   "gluc":[0, 0, 1, 1, 1],
#                   "alco":[1, 1, 0, 0, 0],
#                   "cardio":[1, 1, 0, 0, 1]})

#df_cat = df[["cholesterol", "gluc", "alco"]].melt()



# Agrupar por "cardio" y calcular la suma de cada variable
#grouped_df = df.groupby("cardio").sum().reset_index()

#######
#SEABORNNNNNN
#######

df = sns.load_dataset("titanic")
sns.catplot(
    data=df, x="class", y="survived", col="sex",
    kind="bar", height=4, aspect=.6,
)
plt.show()
"""

