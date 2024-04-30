import streamlit as st
 

tab1, tab2, tab3 = st.tabs(["Développement et test d’un outil décisionnel", "Données JSON", "Owl"])

with tab1 : 
 st.header("Développement et test d’un outil décisionnel")
 
 st.write("### Dévolopper un outil décisionnel sur les communes métropolitaine de plus de 20000 habitants. ")
 st.image("cody1.png")
 st.write("#### 3F1R, le nom que nous avons donné à notre groupe dans le but de simuler un cas réel.")
 st.markdown("Pour accéder à notre application il suffit de cliquer sur [ce lien](https://3f1rhome.streamlit.app/)")
 st.write("""Vous arriverez sur notre page d'acceuil.
         Pour la suite je vous laisse découvrir l'application.""")
 st.write("""Pendant le développement de cet outil j'ai sue prouver que je maitrise plusieurs des compétences 
             que j'ai apprise pendant mes 3 année de BUT. """)
 st.write("Nous pouvons donc dénombrer les suivante :")
 st.write("Compétence 1 « Traiter des données à des fins décisionnelles »")
 st.write("""- En intervenant à toutes les étapes du cycle de vie de la donnée (insertion, modification, extraction, suppression)
         \n- En utilisant le modèle de données adapté aux besoins
         \n- En traduisant correctement les demandes métier en programmes, avec le respect du cahier des charges s'il existe
         \n- En écrivant un programme correctement structuré et documenté, respectant les bonnes pratiques
         \n- En identifiant les librairies et langages dédiés
         \n- Identifier les solutions technologiques permettant la collecte et la diffusion de données
         \n- Comprendre les spécificités des données complexes et de leur exploitation""")
 st.write("Compétence 2 « Analyser statistiquement des données »")
 st.write("""- En identifiant et en mettant en œuvre les techniques adaptées aux données complexes (données massives, 
             données mal structurées, flux de données...)
             \n-Prendre conscience des limites des méthodes classiques pour l’analyse des données complexes 
             (données massives, données mal structurées...)""")
 st.write("Compétence 3 : « Valoriser une production dans un contexte professionnel »")
 st.write("""- Savoir transformer la donnée pour la mettre en conformité avec des normes (anonymisation, normalisation)""")
 st.write("Compétence 4 : « Développer un outil décisionnel » (parcours VCOD)")
 st.write("""- En mettant en œuvre une structuration des données adaptée à leurs caractéristiques (type, volume...)
             \n- En utilisant des méthodes de développement logiciel
             \n- Réaliser l’intérêt d’appliquer les méthodes de développement dans la réalisation d’un projet informatique""")
 
 st.write("""En effet, grâce au code suivant j'ai réussie à extraire les données, puis les modifier, 
             supprimer certain et les préparer pour l'insertion dans l'appli : \n
             import pandas as pd
         import requests
 
         # Fonction pour récupérer les données météorologiques d'une commune
         def get_weather_data(city_name, api_key):
             url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
             response = requests.get(url)
             if response.status_code == 200:
                 data = response.json()
                 weather_data = {
                     "city_name": city_name,
                     "temperature": data["main"]["temp"],
                     "humidity": data["main"]["humidity"],
                     "weather_description": data["weather"][0]["description"]
                 }
                 return weather_data
             else:
                 print(f"Failed to get weather data for {city_name}")
                 return None
 
         # Charger les données du fichier data_com-2.csv
         df = pd.read_csv("data_com-2.csv", sep=";")
 
         # Clef API OpenWeatherMap (que je ne donne pas ici bien évidemment)
         weather_api_key = "#"
 
         # Créer une liste pour stocker les données météorologiques
         weather_data_list = []
 
         # Parcourir chaque ligne du dataframe
         for index, row in df.iterrows():
             # Récupérer le nom de la commune ou le code département
             city_name = row["Nom"]
             if pd.isnull(city_name):  # Si le nom de la commune est manquant, utiliser le code département
                 city_name = row["com_code"]
             # Appeler la fonction pour récupérer les données météorologiques
             weather_data = get_weather_data(city_name, weather_api_key)
             if weather_data:
                 # Ajouter les données météorologiques à la liste
                 weather_data_list.append(weather_data)
 
         # Convertir la liste en dataframe
         weather_df = pd.DataFrame(weather_data_list)
 
         # Fusionner les données météorologiques avec le dataframe initial sur le nom de la commune ou le code département
         merged_df = pd.merge(df, weather_df, left_on=["Nom"], right_on=["city_name"], how="left")
 
 
         # Enregistrer le dataframe avec toutes les données
         merged_df.to_csv("data_com_with_weather.csv", index=False)
         """)
 st.write("Compétence 2 « Analyser statistiquement des données »")
 st.write("""- En identifiant et en mettant en œuvre les techniques adaptées aux attentes du client ou de l’instance décisionnaire
         & Mesurer l’importance de comprendre et de répondre à l'ensemble des problématiques posées (Compétence 3)
         \nEn répondant à la problématique posé
         \n- Prendre conscience des différences entre des outils statistiques pour choisir le plus adapté 
         \nNotre équipe maîtrisant mieux python que R nous avons choisie streamlit au lieu de Rshinny         """)
 
 st.write("Compétence 3 : « Valoriser une production dans un contexte professionnel »")
 st.write(""" - En s’adaptant au niveau d’expertise, à la culture et au statut du destinataire & En utilisant la forme de restitution adaptée
         & En réalisant des solutions de visualisation spécifiques aux données métier (Compétence 4) & En s’inscrivant dans une démarche de documentation des réalisations adaptée au public visé (Compétence 1)
         &Prendre conscience de la nécessité d’intégrer la vision de l’interlocuteur (transversalité, international, multiculture, niveau d’expertise…)
         \nComme vous pouvez le voir sur notre application nous avons choisie aucun graphique compliqué, 
         des cartes et des tableaux, pour que même un collégien puisse utiliser notre appli. 
         \n- En s’exprimant correctement, aussi bien en français que dans une langue étrangère, à l'oral comme à l'écrit & Identifier les clés d'une bonne communication (procédures et techniques utilisées)
         \nNotre présentation devant l'enseignant et nos camarades de classe.
         \n-  En veillant aux aspects éthiques, déontologiques et réglementaires d’utilisation et de diffusion des données (Comp 3 & Comp 4)
         \nNous avons veillé à ce qu'aucune données sensibles soit présent sur notre appli, tous nos sources de données sont
         des données 'opendata' trouvé sur internet et des données extrait d'API.
         \n- En interprétant et contextualisant les résultats (citations, vérification des sources, esprit critique)
         & En assurant la qualité des données et minimisant les biais liés à l’incertitude et l’imprécision dans les sources (Compétence 4) 
         \nNous avons vérifier chacune de nos sources. 
         \n- Être force de proposition & En intervenant à différents niveaux de la chaîne décisionnelle (Compétence 4)
         \nEtant de nature très sur de moi même, je n'hésite jamais à proposer mes idées, dans ce travail un certain nombre
         d'idée venais de moi.""")
 st.write("Compétence 4 : « Développer un outil décisionnel » (parcours VCOD)")
 st.write("""- Apprécier l’intérêt de l’utilisation d’un gestionnaire de versions de code
         \nIl n'existe aucun développeur qui ne fait aucune erreur, dans notre cas nous avons utiliser git pour controler
         les commits en utilisant des branches parallèles.""")
with tab2 : 
 st.header("Traiter des données sous format JavaScript Object Notation, JSON, réaliser en alternance")
 st.write("### Creer de nouvelles tables de données à partir des données brutes pour tester les nouvelles tables du système décisionnel.")
 st.write("Voici le format de données JSON :")
