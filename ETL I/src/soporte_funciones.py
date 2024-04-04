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

# aplicar función anterior a una lista de df dada
def cambiar_columnas(lista_df):
    for df in lista_df:
        nuevas_columnas(df)


# limpieza de df productos
def tabla_productos(productos):
    id_productos = list(productos.index)

    productos = pd.DataFrame({'id' : id_productos, 'nombre_producto': list(productos['ID']), 'categoria': list(productos['Nombre_Producto']), 'precio': list(productos['Categoría']), 'origen': list(productos['Precio']), 'descripcion': list(productos['Origen'])})
    
    return productos


# convertir todos los datos object de los df a minúscula
def unify(valor):
    try:
        return valor.lower().strip()
    except:
        return valor