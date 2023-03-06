# FI Mex state
# Parra Caporal José Andrés
# 3/03/23

# Modules
import os
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import statsmodels.formula.api as smf

# Directory
os.chdir("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Data")

# Data
num_sheets = list(range(0,32))

inv = []

for i in num_sheets:
    a = pd.read_excel("flujosporentidadfederativa.xls", 
                          sheet_name = i,
                          header = None,
                          skiprows = 11,
                          nrows= 1,
                          usecols ="A,F,K,P,U,Z,AE,AJ,AO,AT,AY,BD,BI,BN,BS,BX,CC,CH,CM,CR,CW,DB,DG,DL,DQ")
    inv.append(a)

inv = pd.concat(inv, axis = 0)

del a, i, num_sheets

inv[0] = ["Aguascalientes",
          "Baja California",
          "Baja California Sur",
          "Campeche",
          "Chiapas",
          "Chihuahua",
          "Ciudad de México",
          "Coahuila de Zaragoza",
          "Colima",
          "Durango",
          "Estado de México",
          "Guanajuato",
          "Guerrero",
          "Hidalgo",
          "Jalisco",
          "Michoacán de Ocampo",
          "Morelos",
          "Nayarit",
          "Nuevo León",
          "Oaxaca",
          "Puebla",
          "Querétaro",
          "Quintana Roo",
          "San Luis Potosí",
          "Sinaloa",
          "Sonora",
          "Tabasco",
          "Tamaulipas",
          "Tlaxcala",
          "Veracruz de Ignacio de la Llave",
          "Yucatán",
          "Zacatecas"]

years = list(range(1999,2023))
years = [str(i) for i in years]
years.insert(0, "estado")

inv.columns = years
inv = inv.set_index("estado")

del years, states

# Mexico map
entidades = gpd.read_file("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Data\\Marco_geoestadistico_INEGI\\Entidades\\00ent.shp")

# Making a GIF
    # Min max values
min_inv = inv.to_numpy().min()
max_inv = inv.to_numpy().max()

    # Def mapping function
def inv_ent(year,name):
    mex = entidades.merge(inv[year], left_on = 'NOMGEO', 
                          right_index = True, how = 'left')
    mapa_f_invest = mex.plot(column = year,
                             vmin= min_inv, vmax = max_inv,
                             legend = True,
                             cmap = 'RdPu',
                             legend_kwds = {'orientation': "horizontal"})
    plt.title("Foreing Investment by State, Mexico (Millon USD): " + year)
    plt.text(.3, -.5, "Source: Secretaría de Economía, México", fontsize = 'xx-small', color = "#808080")
    plt.axis('off')
    plt.savefig(name, dpi = 300, bbox_inches='tight')
    return mapa_f_invest

names_plots = ["C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_1999.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2000.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2001.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2002.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2003.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2004.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2005.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2006.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2007.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2008.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2009.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2010.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2011.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2012.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2013.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2014.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2015.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2016.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2017.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2018.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2019.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2020.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2021.jpg",
               "C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\plots\\inv_2022.jpg",]

for i,j in zip(inv.columns,names_plots):
    inv_ent(i,j)
    
###Creating the GIF
def make_gif(frame_folder):
    frames = [Image.open(image) for image in names_plots]
    frame_one = frames[0]
    frame_one.save("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\inv_foreing_mex.gif", format="GIF", append_images=frames,
               save_all=True, duration= 800, loop=0)
    
if __name__ == "__main__":
    make_gif("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foreing_inv_state\\")