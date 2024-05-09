import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)



st.title('Hello Wilders, je fais enfin cette quête !')

st.write("Je vais faire deux graphiques avec une petite analyse à chaque fois, j'espère que ça vous plaira :)")

st.write("Admirez cette liste déroulante qui rend mon graphique dynamique ")

# Pour rendre le graphique dynamique : 
continent_choisi = st.selectbox('Choisissez un continent', df_voiture['continent'].unique())

df_continent = df_voiture[df_voiture['continent'] == continent_choisi]

# Définition du graphique 1: 

viz_correlation = sns.scatterplot(data=df_continent, x='mpg', y='hp')

plt.ylabel('Horsepower (hp)')
plt.xlabel('Miles per gallon (mpg)')
plt.title('Relationship between Horsepower and fuel consumption')

st.pyplot(viz_correlation.figure)
st.write(" ANALYSE : On observe une corrélation négative entre la puissance et la consommation de carburant. Cela signifie que les véhicules avec une puissance plus élevée consomment plus de carburant par mile parcouru.")

df_voiture2 = df_voiture.drop(columns='continent')
                         
viz_correlation = sns.heatmap(df_voiture2.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)


plt.title('Correlation analysis between car characteristics')

st.pyplot(viz_correlation.figure)

st.write("ANALYSE : Les couleurs dans la heatmap indique la force et la direction de la corrélation entre chaque paire de caractéristiques. Plus la couleur est foncée, plus la corrélation est forte. ")









