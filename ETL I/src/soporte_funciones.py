import pandas as pd
import numpy as np
import datetime as datetime

# info general de los df
def explorar_df(lista_df):
    for df in lista_df:
        display(df.head())
        display(df.describe())
        display(df.describe(include='O'))
        display(df.info())
        print('Duplicados totales:', df.duplicated().sum())
        print('-'*20)


# valores numéricos de object a integer
def to_int(valor):
    try:
        return int(valor.replace(',','.'))
    except:
        valor


# fechas de object a date
def to_date(valor):
    try:
        fecha = datetime.strptime(valor, '%Y-%m-%d').date()
        return fecha
    except:
        return valor


# renombrar columnas
def nuevas_columnas(df):
    nuevas_columnas = {columna: columna.lower() for columna in df.columns}
    return df.rename(columns=nuevas_columnas, inplace= True)


# limpieza de df productos
def tabla_productos(productos):
    productos.insert(0, 'id', productos.index)

    productos.reset_index(inplace=True)

    nueva_columna = pd.merge(productos['Origen'].fillna(''), productos['Descripción'].fillna(''), left_index=True, right_index=True)
    productos['Descripción'] = nueva_columna.apply(lambda x: ''.join(x), axis=1)

    productos.drop(columns=['index', 'Origen'], axis=1, inplace=True)

    productos = productos.set_axis(['id', 'nombre_producto', 'categoria', 'precio', 'origen', 'descripcion'], axis=1)

    return productos


# convertir todos los datos object de los df a minúscula
def unify(valor):
    try:
        return valor.lower().strip()
    except:
        return valor

# aplicar cambios a df    
def homog_tablas(lista_df):
    for df in lista_df:
        nuevas_columnas(df)
    
    for df in lista_df:
        for columna in df.columns:
            df[columna] = df[columna].apply(unify)
    

