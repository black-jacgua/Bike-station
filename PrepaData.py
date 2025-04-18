import pandas as pd
import glob

# 1. Lire tous les fichiers CSV
fichiers = glob.glob("./getting/_*.csv")  

dfs = [pd.read_csv(f) for f in fichiers]

# 2. Union = concaténation
df = pd.concat(dfs, ignore_index=True)


#Regrouper les donnees suivant : country, city et position en faisant le sum de velo disponibles
df0 = df.groupby(['country','city','position']).sum(numeric_only=True).reset_index()
df0 = df0[df0['position'] != 17]


# pour trouver les variation dans de la quantite de velo
df0['glis'] = abs(df0['free_bikes'] - df0['free_bikes'].shift(1))
df0['glis1'] = df0['free_bikes'] - df0['free_bikes'].shift(1)

#on elimine les premiere position pour chaque city 
df1 = df0[df0['position'] != 0]

# on calcule la somme total pour chaque ville sur tous les position

df2 = df1[['country','city','glis', 'glis1']].groupby(['country','city']).sum(numeric_only=True).reset_index()

#On recuper toutes les premieres valeurs pour connaitre la variation global.
df00 = df0[df0['position'] == 0][['free_bikes','city']]

#jointure sur les donnees
df3 = pd.merge(df2, df00, how='inner', on='city')
df3['percent'] = df3['glis1']*100/df3['free_bikes']

#dernier validation des donnees.

data = df3[['country','city','glis','percent']].copy()


data["Region"] = "Europe"

data.loc[data['country'].isin(['Usa','Canada']), "Region"] = "America"

#Sauvegarder les donnees
data.to_csv("./live/bike_frenquency_station.csv", index=False)
