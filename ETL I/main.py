#%%
from src import soporte_funciones as sp
import pandas as pd
import numpy as np
#%%
ventas = pd.read_csv('../ventas.csv', index_col=0)
productos = pd.read_csv('../productos.csv',on_bad_lines='skip', index_col=0)
clientes = pd.read_csv('../clientes.csv')
# %%
#sp.explorar_df([ventas, productos, clientes])

# limpieza de tablas
sp.tabla_productos(productos)
display(productos.head())
sp.cambiar_columnas([ventas, clientes, productos])
display(ventas.sample(), clientes.sample(), productos.sample())
# %%

# %%
