"""
created by Oscar Enrique Estrada García
oenriqueg@gmail.com
"""

import os
import xml.etree.ElementTree as ET
import pandas as pd

cwd = os.getcwd()
files = os.listdir(cwd+'/xmls/')

for file in files:
    # Abrimos y parseamos el fichero XML
    #with open(file, 'rb') as f:
    tree = ET.parse('xmls/'+file)
    
    name = file.split('.')
    filename = name[0]
    print(f'Archivo procesado:  {filename}.xml')
    
    # Obtenemos el elemento raíz del fichero XML,
    # es decir, la etiqueta <Data>
    factura = tree.getroot()

    # Creamos el array vacío que contendrá los
    # datos agrupados de los dependientes
    lista_de_empleados = []

    # Iteramos sobre cada dependiente del fichero
    for empleado in factura[4][0]:
        # Almacenamos en una lista todos los
        # atributos de un dependiente
        for atributo in empleado:
            lista_atributos = [atributo.attrib.values() for atributo in empleado]


    dataframe = pd.DataFrame(lista_atributos, columns=['CURP', 'FECHA', 'ID', 'IMPORTE','NOMBRE','IMSS','RFC'])
    dataframe['IMPORTE'] = dataframe['IMPORTE'].apply(pd.to_numeric, errors='coerce').fillna(0)
    dataframe.set_index('NOMBRE', inplace = True)
    writer = pd.ExcelWriter(f'resultado_{filename}'+'.xlsx', engine='xlsxwriter', datetime_format='dd/Mmm/yyyy')
    dataframe.to_excel(writer,'empleados', index=True)
    writer.save()