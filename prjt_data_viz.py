import streamlit as st
import os
import pydeck as pdk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
import plotly.express as px
import plotly
import folium
from folium.plugins import HeatMap
import plotly.express as px


print(plotly.__version__)

st.balloons()
st.write(st.__version__)

page = st.sidebar.selectbox("Sélectionnez une page", ["Page d'accueil", "Exploration des données", "Analyse des taux de participation", "Répartition des voix par parti"])

if page == "Page d'accueil":
    st.markdown("<h2 style='text-align: center; color: #4CAF50;'>Welcome to my portfolio</h2>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center; font-size: 18px;'>Hello! I'm Oumou Sangare, currently based in Ile-de-France.</p>",
        unsafe_allow_html=True)

    # Afficher la lettre de motivation
    st.markdown("---")
    st.markdown("<h3 style='text-align: left;'>Lettre de motivation</h3>", unsafe_allow_html=True)
    lettre_de_motivation = """
        Consciente de mon intérêt envers la Data Science depuis ma participation au projet Prioréno à la Banque des Territoires et attirée par l’innovation dans ce domaine ; je vous présente ma candidature pour un stage technique en Data Science de 5 mois, prévu du 04 novembre 2024 au 04 avril 2025.

        Actuellement étudiante en quatrième année à EFREI Paris, école d’ingénieur spécialisée dans l’informatique et l’électronique, je débute ma première année de master en Data Engineering. C’est au cours de mon stage d'observation en tant qu’agent occasionnel à la Caisse des Dépôts et Consignation que j'ai découvert un intérêt pour la Data Science en juillet 2022. Par la suite, j'ai acquis des compétences de base en Python, SQL et Machine Learning durant mes deux années de classe préparatoire. Plus récemment, j’ai approfondi ces compétences lors d’un mois de Mastercamp intensif de 30 heures axé sur la Data Science, en vue de mon entrée en master. J'y ai assimilé des bibliothèques Python telles que numpy, pandas, matplotlib, seaborn et scikit-learn et réalisé une analyse de données immobilières relatives aux demandes de valeurs foncières en France, appliquant la méthode d'Analyse Exploratoire des Données (EDA). Cette analyse m’a permis d’identifier les tendances du marché, détecter des anomalies et cerner les facteurs influençant les prix.

        Pour conclure ce stage préparatoire, j'ai contribué à la réponse à un appel d'offre de l’entreprise LIPSTIP, pour le développement d'un système de classification de brevets. J'ai ainsi développé un modèle performant basé sur l'intelligence artificielle, utilisant BERT avec un score F1 supérieur à 0.85, tout en intégrant des méthodes explicatives telles que LIME et SHAP. Cette expérience m’a aidé à renforcer mes compétences en travail d'équipe et démontrer notre expertise technique et organisationnelle pour remporter l’appel d'offre, avant le début de ma recherche de stage.

        Désireuse de fournir un travail rigoureux et de qualité, je m'engage à répondre efficacement aux besoins de l’entreprise, afin d'apporter des résultats optimaux à mon employeur tout en enrichissant mon bagage professionnel. Intégrer votre enseigne représenterait pour moi l’opportunité précieuse d'acquérir ma première expérience technique dans mon domaine d’apprentissage.

        Je vous remercie pour l’attention portée à ma candidature et reste à votre disposition pour tout complément d'information. Veuillez agréer, Madame, Monsieur, l'expression de mes sentiments les plus respectueux.
        """
    st.markdown(lettre_de_motivation)

    # Image de profil
    st.sidebar.image("C:\\Users\\oumis\\Downloads\\photo_profil_portfolio.jpg", use_column_width=True)
    st.sidebar.header("À propos de moi")
    st.sidebar.markdown(
        "<p style='font-size: 14px;'>Actuellement en première année de Master en Data Engineering à l'EFREI Paris.</p>",
        unsafe_allow_html=True
    )
    st.sidebar.markdown(
        "<p style='font-size: 14px;'>Assisté par Dr Mano Mathew, manageur du département de Data Visualisation.</p>",
        unsafe_allow_html=True
    )
    st.sidebar.image("C:\\Users\\oumis\\Downloads\\Documents\\TP1\\img\\Logo-efrei.jpg", use_column_width=True)
    st.sidebar.markdown("---")

    # Informations de contact
    st.sidebar.markdown("""
        <div style="padding: 10px; border-radius: 10px; background-color: #f4f4f4; margin-bottom: 0px;">
            <h3 style="color: #333;">Contact Information</h3>
            <p>📧 : oumou.sangare@efrei.net</p>
            <p>📍 : Ile-de-France</p>
        </div>
    """, unsafe_allow_html=True)

    # Ajouter un espace avant le bouton LinkedIn
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Bouton LinkedIn
    linkedin_url = "http://www.linkedin.com/in/oumou-sangar%C3%A9-8138a0238"
    st.sidebar.markdown(f"""
        <div style="border: 2px solid #0e76a8; padding: 10px; text-align: center; border-radius: 10px; margin-bottom: 20px;">
            <a href="{linkedin_url}" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" style="width:40px; height:40px;">
            </a>
            <p><a href="{linkedin_url}" target="_blank" style="text-decoration:none; color:#0e76a8;">My LinkedIn profil</a></p>
        </div>
    """, unsafe_allow_html=True)

    # Ajouter un espace entre LinkedIn et le bouton CV
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Bouton de téléchargement du CV
    cv_file_path = "C:\\Users\\oumis\\Downloads\\CV Oumou SANGARE.pdf"
    with open(cv_file_path, "rb") as cv_file:
        st.sidebar.download_button(
            label="📄 Télécharger mon CV",
            data=cv_file,
            file_name="Oumou_Sangare_CV.pdf",
            mime="application/pdf"
        )

    # Ajouter un espace entre le bouton CV et GitHub
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    # Bouton vers la section projets GitHub
    if st.sidebar.button("🔍 View My Projects on Git Hub"):
        st.sidebar.markdown(f"[Cliquez ici pour voir mes projets sur GitHub](https://github.com/Oumousgr)")

elif page == "Exploration des données":
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; border: 2px solid black; padding: 10px; border-radius: 10px; background-color: #f0f0f0;">
            <h2 style="text-align: center; color: black; margin: 0;">Exploration des données</h2>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.title("Tableau de Données Initial")
    st.subheader("Résultats des élections européennes 2014 :")
    # Fonction pour charger les données avec mise en cache
    @st.cache_data
    def load_data(file_path):
        # Lire le fichier CSV
        data = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', on_bad_lines='skip')
        return data


    # Chargement des données avec mise en cache
    url = r"C:\Users\oumis\OneDrive\Documents\goodfichier.csv"
    df = load_data(url)
    st.write(df)

    # Définir les colonnes pertinentes à garder
    colonnes_a_garder = [
        'Code du département',
        'Libellé du département',
        'Inscrits',
        'Abstentions',
        '% Abs/Ins',
        'Votants',
        '% Vot/Ins',
        'Blancs',
        '% BlBlancs/Vot',
        'Exprimés',
        'Libellé Abrégé Liste',
        'Voix',
        '% Voix/Exp'
    ]

    # Ajouter les colonnes supplémentaires jusqu'à 30
    for i in range(1, 31):
        colonnes_a_garder.extend([
            f'Libellé Abrégé Liste.{i}',
            f'Voix.{i}',
            f'% Voix/Exp.{i}'
        ])

    # Filtrer les données pour garder seulement les colonnes pertinentes
    df_filtered = df[colonnes_a_garder]

    # Remplacer les valeurs manquantes (None ou NaN) par 0
    df_filtered.fillna(0, inplace=True)

    # Affichage des données filtrées
    st.title("Nettoyage des donnés")
    st.write("Voici les données filtrées avec les colonnes pertinentes :")
    st.dataframe(df_filtered)

    # Bouton de téléchargement du fichier
    st.download_button(
        label="Télécharger les données au format CSV",
        data=df_filtered.to_csv(sep=';', index=False),  # Utilisation du point-virgule comme séparateur
        file_name='df_filtered.csv',
        mime='text/csv',
        key='unique_download_button_1'
    )

    st.write("Types des colonnes avant la conversion :")
    st.write(df_filtered.dtypes)

    # Colonnes à convertir
    colonnes_a_convertir = [
        '% Abs/Ins', '% Vot/Ins', '% BlBlancs/Vot',
        '% Voix/Exp', '% Voix/Exp.1', '% Voix/Exp.2', '% Voix/Exp.3',
        '% Voix/Exp.4', '% Voix/Exp.5', '% Voix/Exp.6', '% Voix/Exp.7',
        '% Voix/Exp.8', '% Voix/Exp.9', '% Voix/Exp.10', '% Voix/Exp.11',
        '% Voix/Exp.12', '% Voix/Exp.13', '% Voix/Exp.14', '% Voix/Exp.15',
        '% Voix/Exp.16', '% Voix/Exp.17', '% Voix/Exp.18', '% Voix/Exp.19',
        '% Voix/Exp.20', '% Voix/Exp.21', '% Voix/Exp.22', '% Voix/Exp.23',
        '% Voix/Exp.24', '% Voix/Exp.25', '% Voix/Exp.26', '% Voix/Exp.27',
        '% Voix/Exp.28', '% Voix/Exp.29', '% Voix/Exp.30'
    ]

    # Conversion des colonnes en float
    for col in colonnes_a_convertir:
        df_filtered[col] = pd.to_numeric(df_filtered[col].str.replace(',', '.'), errors='coerce')

    # Vérification des types après conversion
    st.write("Types des colonnes après la conversion :")
    st.write(df_filtered.dtypes)

    # Agrégation par département
    try:
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            "Inscrits": "sum",
            "Abstentions": "sum",
            "% Abs/Ins": "mean",
            "Votants": "sum",
            "% Vot/Ins": "mean",
            "Blancs": "sum",
            "% BlBlancs/Vot": "mean",
            "Exprimés": "sum",

            "Libellé Abrégé Liste": "first",
            "Voix": "sum",
            "% Voix/Exp": "mean",

            "Libellé Abrégé Liste.1": "first",
            "Voix.1": "sum",
            '% Voix/Exp.1': "mean",

            "Libellé Abrégé Liste.2": "first",
            "Voix.2": "sum",
            '% Voix/Exp.2': "mean",

            "Libellé Abrégé Liste.3": "first",
            "Voix.3": "sum",
            '% Voix/Exp.3': "mean",

            "Libellé Abrégé Liste.4": "first",
            "Voix.4": "sum",
            '% Voix/Exp.4': "mean",

            "Libellé Abrégé Liste.5": "first",
            "Voix.5": "sum",
            '% Voix/Exp.5': "mean",

            "Libellé Abrégé Liste.6": "first",
            "Voix.6": "sum",
            '% Voix/Exp.6': "mean",

            "Libellé Abrégé Liste.7": "first",
            "Voix.7": "sum",
            '% Voix/Exp.7': "mean",

            "Libellé Abrégé Liste.8": "first",
            "Voix.8": "sum",
            '% Voix/Exp.8': "mean",

            "Libellé Abrégé Liste.9": "first",
            "Voix.9": "sum",
            '% Voix/Exp.9': "mean",

            "Libellé Abrégé Liste.10": "first",
            "Voix.10": "sum",
            '% Voix/Exp.10': "mean",

            "Libellé Abrégé Liste.11": "first",
            "Voix.11": "sum",
            '% Voix/Exp.11': "mean",

            "Libellé Abrégé Liste.12": "first",
            "Voix.12": "sum",
            '% Voix/Exp.12': "mean",

            "Libellé Abrégé Liste.13": "first",
            "Voix.13": "sum",
            '% Voix/Exp.13': "mean",

            "Libellé Abrégé Liste.14": "first",
            "Voix.14": "sum",
            '% Voix/Exp.14': "mean",

            "Libellé Abrégé Liste.15": "first",
            "Voix.15": "sum",
            '% Voix/Exp.15': "mean",

            "Libellé Abrégé Liste.16": "first",
            "Voix.16": "sum",
            '% Voix/Exp.16': "mean",

            "Libellé Abrégé Liste.17": "first",
            "Voix.17": "sum",
            '% Voix/Exp.17': "mean",

            "Libellé Abrégé Liste.18": "first",
            "Voix.18": "sum",
            '% Voix/Exp.18': "mean",

            "Libellé Abrégé Liste.19": "first",
            "Voix.19": "sum",
            '% Voix/Exp.19': "mean",

            "Libellé Abrégé Liste.20": "first",
            "Voix.20": "sum",
            '% Voix/Exp.20': "mean",

            "Libellé Abrégé Liste.21": "first",
            "Voix.21": "sum",
            '% Voix/Exp.21': "mean",

            "Libellé Abrégé Liste.22": "first",
            "Voix.22": "sum",
            '% Voix/Exp.22': "mean",

            "Libellé Abrégé Liste.23": "first",
            "Voix.23": "sum",
            '% Voix/Exp.23': "mean",

            "Libellé Abrégé Liste.24": "first",
            "Voix.24": "sum",
            '% Voix/Exp.24': "mean",

            "Libellé Abrégé Liste.25": "first",
            "Voix.25": "sum",
            '% Voix/Exp.25': "mean",

            "Libellé Abrégé Liste.26": "first",
            "Voix.26": "sum",
            '% Voix/Exp.26': "mean",

            "Libellé Abrégé Liste.27": "first",
            "Voix.27": "sum",
            '% Voix/Exp.27': "mean",

            "Libellé Abrégé Liste.28": "first",
            "Voix.28": "sum",
            '% Voix/Exp.28': "mean",

            "Libellé Abrégé Liste.29": "first",
            "Voix.29": "sum",
            '% Voix/Exp.29': "mean",

            "Libellé Abrégé Liste.30": "first",
            "Voix.30": "sum",
            '% Voix/Exp.30': "mean",

        }).reset_index()

        # Ajout des nouvelles colonnes vides
        nouvelles_colonnes_vides = [
            'Voix_Liste Divers', '% Voix/Exp_Liste Divers',
            'Voix_Liste Divers droite', '% Voix/Exp_Liste Divers droite',
            'Voix_Liste Divers gauche', '% Voix/Exp_Liste Divers gauche',
            'Voix_Liste Europe-Ecologie-Les Verts', '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            'Voix_Liste Extrême droite', '% Voix/Exp_Liste Extrême droite',
            'Voix_Liste Extrême gauche', '% Voix/Exp_Liste Extrême gauche',
            'Voix_Liste Front National', '% Voix/Exp_Liste Front National',
            'Voix_Liste Front de Gauche', '% Voix/Exp_Liste Front de Gauche',
            'Voix_Liste Union de la Gauche', '% Voix/Exp_Liste Union de la Gauche',
            'Voix_Liste Union du Centre', '% Voix/Exp_Liste Union du Centre',
            'Voix_Liste Union pour un Mouvement Populaire', '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajout des nouvelles colonnes avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides:
            df_filtered[col] = 0

        # Remplissage des colonnes de voix en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                voix_col = f'Voix.{j}' if j > 0 else 'Voix'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and voix_col in df_filtered.columns:
                    voix_value = row[voix_col]
                    voix_value = float(voix_value) if pd.notnull(voix_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] == 'Liste Divers':
                        df_filtered.at[index, 'Voix_Liste Divers'] += voix_value
                    elif row[label_col] == 'Liste Divers droite':
                        df_filtered.at[index, 'Voix_Liste Divers droite'] += voix_value
                    elif row[label_col] == 'Liste Divers gauche':
                        df_filtered.at[index, 'Voix_Liste Divers gauche'] += voix_value
                    elif row[label_col] == 'Liste Europe-Ecologie-Les Verts':
                        df_filtered.at[index, 'Voix_Liste Europe-Ecologie-Les Verts'] += voix_value
                    elif row[label_col] == 'Liste Extrême droite':
                        df_filtered.at[index, 'Voix_Liste Extrême droite'] += voix_value
                    elif row[label_col] == 'Liste Extrême gauche':
                        df_filtered.at[index, 'Voix_Liste Extrême gauche'] += voix_value
                    elif row[label_col] == 'Liste Front National':
                        df_filtered.at[index, 'Voix_Liste Front National'] += voix_value
                    elif row[label_col] == 'Liste Front de Gauche':
                        df_filtered.at[index, 'Voix_Liste Front de Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union de la Gauche':
                        df_filtered.at[index, 'Voix_Liste Union de la Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union du Centre':
                        df_filtered.at[index, 'Voix_Liste Union du Centre'] += voix_value
                    elif row[label_col] == 'Liste Union pour un Mouvement Populaire':
                        df_filtered.at[index, 'Voix_Liste Union pour un Mouvement Populaire'] += voix_value

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajouter les colonnes remplies
            'Voix_Liste Divers': 'sum',
            'Voix_Liste Divers droite': 'sum',
            'Voix_Liste Divers gauche': 'sum',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            'Voix_Liste Extrême droite': 'sum',
            'Voix_Liste Extrême gauche': 'sum',
            'Voix_Liste Front National': 'sum',
            'Voix_Liste Front de Gauche': 'sum',
            'Voix_Liste Union de la Gauche': 'sum',
            'Voix_Liste Union du Centre': 'sum',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum'
        }).reset_index()

        # Ajout des nouvelles colonnes pour les moyennes des pourcentages des voix
        nouvelles_colonnes_vides_pourcent = [
            '% Voix/Exp_Liste Divers',
            '% Voix/Exp_Liste Divers droite',
            '% Voix/Exp_Liste Divers gauche',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            '% Voix/Exp_Liste Extrême droite',
            '% Voix/Exp_Liste Extrême gauche',
            '% Voix/Exp_Liste Front National',
            '% Voix/Exp_Liste Front de Gauche',
            '% Voix/Exp_Liste Union de la Gauche',
            '% Voix/Exp_Liste Union du Centre',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajout des nouvelles colonnes avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides_pourcent:
            df_filtered[col] = 0

        # Ajout des colonnes pour compter les occurrences des listes et calculer la moyenne
        compte_occurrences = {
            'Liste Divers': 'Occurrences_Liste Divers',
            'Liste Divers droite': 'Occurrences_Liste Divers droite',
            'Liste Divers gauche': 'Occurrences_Liste Divers gauche',
            'Liste Europe-Ecologie-Les Verts': 'Occurrences_Liste Europe-Ecologie-Les Verts',
            'Liste Extrême droite': 'Occurrences_Liste Extrême droite',
            'Liste Extrême gauche': 'Occurrences_Liste Extrême gauche',
            'Liste Front National': 'Occurrences_Liste Front National',
            'Liste Front de Gauche': 'Occurrences_Liste Front de Gauche',
            'Liste Union de la Gauche': 'Occurrences_Liste Union de la Gauche',
            'Liste Union du Centre': 'Occurrences_Liste Union du Centre',
            'Liste Union pour un Mouvement Populaire': 'Occurrences_Liste Union pour un Mouvement Populaire'
        }

        # Initialisation des colonnes de comptage avec 0
        for col in compte_occurrences.values():
            df_filtered[col] = 0

        # Remplissage des colonnes de pourcentages en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des pourcentages des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                pourcentage_col = f'% Voix/Exp.{j}' if j > 0 else '% Voix/Exp'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and pourcentage_col in df_filtered.columns:
                    pourcentage_value = row[pourcentage_col]
                    pourcentage_value = float(pourcentage_value) if pd.notnull(pourcentage_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] in compte_occurrences:
                        # Ajouter le pourcentage cumulé
                        moyenne_col = f'% Voix/Exp_{row[label_col]}'
                        df_filtered.at[index, moyenne_col] += pourcentage_value
                        # Incrémenter le compteur d'occurrences
                        compte_col = compte_occurrences[row[label_col]]
                        df_filtered.at[index, compte_col] += 1

        # Calcule de la moyenne des pourcentages en divisant le total cumulé par le nombre d'occurrences
        for label, compte_col in compte_occurrences.items():
            moyenne_col = f'% Voix/Exp_{label}'
            df_filtered[moyenne_col] = df_filtered[moyenne_col] / df_filtered[compte_col]
            # Remplacer les NaN résultants de divisions par 0
            df_filtered[moyenne_col].fillna(0, inplace=True)

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajout des colonnes de voix et de moyennes de pourcentages remplies
            'Voix_Liste Divers': 'sum',
            '% Voix/Exp_Liste Divers': 'mean',
            'Voix_Liste Divers droite': 'sum',
            '% Voix/Exp_Liste Divers droite': 'mean',
            'Voix_Liste Divers gauche': 'sum',
            '% Voix/Exp_Liste Divers gauche': 'mean',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts': 'mean',
            'Voix_Liste Extrême droite': 'sum',
            '% Voix/Exp_Liste Extrême droite': 'mean',
            'Voix_Liste Extrême gauche': 'sum',
            '% Voix/Exp_Liste Extrême gauche': 'mean',
            'Voix_Liste Front National': 'sum',
            '% Voix/Exp_Liste Front National': 'mean',
            'Voix_Liste Front de Gauche': 'sum',
            '% Voix/Exp_Liste Front de Gauche': 'mean',
            'Voix_Liste Union de la Gauche': 'sum',
            '% Voix/Exp_Liste Union de la Gauche': 'mean',
            'Voix_Liste Union du Centre': 'sum',
            '% Voix/Exp_Liste Union du Centre': 'mean',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire': 'mean'
        }).reset_index()

        # Affichage du dataframe regroupé
        st.title("Tableau de Données nettoyé")
        st.write(" Voici les données regroupées par département et classées par parti politique:")
        st.write(df_grouped)

        # Bouton pour télécharger les données regroupées
        df_filtered_2 = df_grouped
        st.download_button(
            label="Télécharger les données au format CSV",
            data=df_filtered_2.to_csv(sep=';', index=False),
            file_name='df_filtered_2.csv',
            mime='text/csv',
            key='unique_download_button_2'
        )

        totaux = {
            'Inscrits': df_filtered_2['Inscrits'].sum(),
            'Abstentions': df_filtered_2['Abstentions'].sum(),
            'Votants': df_filtered_2['Votants'].sum(),
            'Blancs': df_filtered_2['Blancs'].sum(),
            'Exprimés': df_filtered_2['Exprimés'].sum()
        }

        # Visualisation
        totaux_df = pd.DataFrame(list(totaux.items()), columns=['Catégorie', 'Total'])
        st.subheader("Totaux des inscrits, abstentions, votants, blancs et exprimés.")
        fig = px.bar(totaux_df, x='Catégorie', y='Total')
        st.plotly_chart(fig)

        # Votant et non votant
        total_inscrits = df_filtered_2['Inscrits'].sum()
        total_votants = df_filtered_2['Votants'].sum()
        total_non_votants = total_inscrits - total_votants

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

elif page == "Analyse des taux de participation":
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; border: 2px solid black; padding: 10px; border-radius: 10px; background-color: #f0f0f0;">
            <h2 style="text-align: center; color: black; margin: 0;">Analyse des taux de participation</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("Tableau de Données nettoyé")


    # Fonction pour charger les données avec mise en cache
    @st.cache_data
    def load_data(file_path):
        # Lire le fichier CSV
        data = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', on_bad_lines='skip')
        return data


    # Chargement des données avec mise en cache
    url = r"C:\Users\oumis\OneDrive\Documents\goodfichier.csv"
    df = load_data(url)

    # Définir les colonnes pertinentes à garder
    colonnes_a_garder = [
        'Code du département',
        'Libellé du département',
        'Inscrits',
        'Abstentions',
        '% Abs/Ins',
        'Votants',
        '% Vot/Ins',
        'Blancs',
        '% BlBlancs/Vot',
        'Exprimés',
        'Libellé Abrégé Liste',
        'Voix',
        '% Voix/Exp'
    ]

    # Ajouter les colonnes supplémentaires jusqu'à 30
    for i in range(1, 31):
        colonnes_a_garder.extend([
            f'Libellé Abrégé Liste.{i}',
            f'Voix.{i}',
            f'% Voix/Exp.{i}'
        ])

    # Filtrer les données pour garder seulement les colonnes pertinentes
    df_filtered = df[colonnes_a_garder]

    # Remplacer les valeurs manquantes (None ou NaN) par 0
    df_filtered.fillna(0, inplace=True)

    # Liste des colonnes à convertir
    colonnes_a_convertir = [
        '% Abs/Ins', '% Vot/Ins', '% BlBlancs/Vot',
        '% Voix/Exp', '% Voix/Exp.1', '% Voix/Exp.2', '% Voix/Exp.3',
        '% Voix/Exp.4', '% Voix/Exp.5', '% Voix/Exp.6', '% Voix/Exp.7',
        '% Voix/Exp.8', '% Voix/Exp.9', '% Voix/Exp.10', '% Voix/Exp.11',
        '% Voix/Exp.12', '% Voix/Exp.13', '% Voix/Exp.14', '% Voix/Exp.15',
        '% Voix/Exp.16', '% Voix/Exp.17', '% Voix/Exp.18', '% Voix/Exp.19',
        '% Voix/Exp.20', '% Voix/Exp.21', '% Voix/Exp.22', '% Voix/Exp.23',
        '% Voix/Exp.24', '% Voix/Exp.25', '% Voix/Exp.26', '% Voix/Exp.27',
        '% Voix/Exp.28', '% Voix/Exp.29', '% Voix/Exp.30'
    ]

    # Conversion des colonnes en float
    for col in colonnes_a_convertir:
        df_filtered[col] = pd.to_numeric(df_filtered[col].str.replace(',', '.'), errors='coerce')


    # Agrégation par département
    try:
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            "Inscrits": "sum",
            "Abstentions": "sum",
            "% Abs/Ins": "mean",
            "Votants": "sum",
            "% Vot/Ins": "mean",
            "Blancs": "sum",
            "% BlBlancs/Vot": "mean",
            "Exprimés": "sum",

            "Libellé Abrégé Liste": "first",
            "Voix": "sum",
            "% Voix/Exp": "mean",

            "Libellé Abrégé Liste.1": "first",
            "Voix.1": "sum",
            '% Voix/Exp.1': "mean",

            "Libellé Abrégé Liste.2": "first",
            "Voix.2": "sum",
            '% Voix/Exp.2': "mean",

            "Libellé Abrégé Liste.3": "first",
            "Voix.3": "sum",
            '% Voix/Exp.3': "mean",

            "Libellé Abrégé Liste.4": "first",
            "Voix.4": "sum",
            '% Voix/Exp.4': "mean",

            "Libellé Abrégé Liste.5": "first",
            "Voix.5": "sum",
            '% Voix/Exp.5': "mean",

            "Libellé Abrégé Liste.6": "first",
            "Voix.6": "sum",
            '% Voix/Exp.6': "mean",

            "Libellé Abrégé Liste.7": "first",
            "Voix.7": "sum",
            '% Voix/Exp.7': "mean",

            "Libellé Abrégé Liste.8": "first",
            "Voix.8": "sum",
            '% Voix/Exp.8': "mean",

            "Libellé Abrégé Liste.9": "first",
            "Voix.9": "sum",
            '% Voix/Exp.9': "mean",

            "Libellé Abrégé Liste.10": "first",
            "Voix.10": "sum",
            '% Voix/Exp.10': "mean",

            "Libellé Abrégé Liste.11": "first",
            "Voix.11": "sum",
            '% Voix/Exp.11': "mean",

            "Libellé Abrégé Liste.12": "first",
            "Voix.12": "sum",
            '% Voix/Exp.12': "mean",

            "Libellé Abrégé Liste.13": "first",
            "Voix.13": "sum",
            '% Voix/Exp.13': "mean",

            "Libellé Abrégé Liste.14": "first",
            "Voix.14": "sum",
            '% Voix/Exp.14': "mean",

            "Libellé Abrégé Liste.15": "first",
            "Voix.15": "sum",
            '% Voix/Exp.15': "mean",

            "Libellé Abrégé Liste.16": "first",
            "Voix.16": "sum",
            '% Voix/Exp.16': "mean",

            "Libellé Abrégé Liste.17": "first",
            "Voix.17": "sum",
            '% Voix/Exp.17': "mean",

            "Libellé Abrégé Liste.18": "first",
            "Voix.18": "sum",
            '% Voix/Exp.18': "mean",

            "Libellé Abrégé Liste.19": "first",
            "Voix.19": "sum",
            '% Voix/Exp.19': "mean",

            "Libellé Abrégé Liste.20": "first",
            "Voix.20": "sum",
            '% Voix/Exp.20': "mean",

            "Libellé Abrégé Liste.21": "first",
            "Voix.21": "sum",
            '% Voix/Exp.21': "mean",

            "Libellé Abrégé Liste.22": "first",
            "Voix.22": "sum",
            '% Voix/Exp.22': "mean",

            "Libellé Abrégé Liste.23": "first",
            "Voix.23": "sum",
            '% Voix/Exp.23': "mean",

            "Libellé Abrégé Liste.24": "first",
            "Voix.24": "sum",
            '% Voix/Exp.24': "mean",

            "Libellé Abrégé Liste.25": "first",
            "Voix.25": "sum",
            '% Voix/Exp.25': "mean",

            "Libellé Abrégé Liste.26": "first",
            "Voix.26": "sum",
            '% Voix/Exp.26': "mean",

            "Libellé Abrégé Liste.27": "first",
            "Voix.27": "sum",
            '% Voix/Exp.27': "mean",

            "Libellé Abrégé Liste.28": "first",
            "Voix.28": "sum",
            '% Voix/Exp.28': "mean",

            "Libellé Abrégé Liste.29": "first",
            "Voix.29": "sum",
            '% Voix/Exp.29': "mean",

            "Libellé Abrégé Liste.30": "first",
            "Voix.30": "sum",
            '% Voix/Exp.30': "mean",

        }).reset_index()

        # Ajout des nouvelles colonnes vides
        nouvelles_colonnes_vides = [
            'Voix_Liste Divers', '% Voix/Exp_Liste Divers',
            'Voix_Liste Divers droite', '% Voix/Exp_Liste Divers droite',
            'Voix_Liste Divers gauche', '% Voix/Exp_Liste Divers gauche',
            'Voix_Liste Europe-Ecologie-Les Verts', '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            'Voix_Liste Extrême droite', '% Voix/Exp_Liste Extrême droite',
            'Voix_Liste Extrême gauche', '% Voix/Exp_Liste Extrême gauche',
            'Voix_Liste Front National', '% Voix/Exp_Liste Front National',
            'Voix_Liste Front de Gauche', '% Voix/Exp_Liste Front de Gauche',
            'Voix_Liste Union de la Gauche', '% Voix/Exp_Liste Union de la Gauche',
            'Voix_Liste Union du Centre', '% Voix/Exp_Liste Union du Centre',
            'Voix_Liste Union pour un Mouvement Populaire', '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajouter les nouvelles colonnes à df_grouped avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides:
            df_filtered[col] = 0  # Initialisation avec 0

        # Remplir les colonnes de voix en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                voix_col = f'Voix.{j}' if j > 0 else 'Voix'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and voix_col in df_filtered.columns:
                    voix_value = row[voix_col]
                    voix_value = float(voix_value) if pd.notnull(voix_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] == 'Liste Divers':
                        df_filtered.at[index, 'Voix_Liste Divers'] += voix_value
                    elif row[label_col] == 'Liste Divers droite':
                        df_filtered.at[index, 'Voix_Liste Divers droite'] += voix_value
                    elif row[label_col] == 'Liste Divers gauche':
                        df_filtered.at[index, 'Voix_Liste Divers gauche'] += voix_value
                    elif row[label_col] == 'Liste Europe-Ecologie-Les Verts':
                        df_filtered.at[index, 'Voix_Liste Europe-Ecologie-Les Verts'] += voix_value
                    elif row[label_col] == 'Liste Extrême droite':
                        df_filtered.at[index, 'Voix_Liste Extrême droite'] += voix_value
                    elif row[label_col] == 'Liste Extrême gauche':
                        df_filtered.at[index, 'Voix_Liste Extrême gauche'] += voix_value
                    elif row[label_col] == 'Liste Front National':
                        df_filtered.at[index, 'Voix_Liste Front National'] += voix_value
                    elif row[label_col] == 'Liste Front de Gauche':
                        df_filtered.at[index, 'Voix_Liste Front de Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union de la Gauche':
                        df_filtered.at[index, 'Voix_Liste Union de la Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union du Centre':
                        df_filtered.at[index, 'Voix_Liste Union du Centre'] += voix_value
                    elif row[label_col] == 'Liste Union pour un Mouvement Populaire':
                        df_filtered.at[index, 'Voix_Liste Union pour un Mouvement Populaire'] += voix_value

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajouter les colonnes que nous avons remplies
            'Voix_Liste Divers': 'sum',
            'Voix_Liste Divers droite': 'sum',
            'Voix_Liste Divers gauche': 'sum',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            'Voix_Liste Extrême droite': 'sum',
            'Voix_Liste Extrême gauche': 'sum',
            'Voix_Liste Front National': 'sum',
            'Voix_Liste Front de Gauche': 'sum',
            'Voix_Liste Union de la Gauche': 'sum',
            'Voix_Liste Union du Centre': 'sum',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum'
        }).reset_index()

        # Ajout des nouvelles colonnes pour les moyennes des pourcentages des voix
        nouvelles_colonnes_vides_pourcent = [
            '% Voix/Exp_Liste Divers',
            '% Voix/Exp_Liste Divers droite',
            '% Voix/Exp_Liste Divers gauche',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            '% Voix/Exp_Liste Extrême droite',
            '% Voix/Exp_Liste Extrême gauche',
            '% Voix/Exp_Liste Front National',
            '% Voix/Exp_Liste Front de Gauche',
            '% Voix/Exp_Liste Union de la Gauche',
            '% Voix/Exp_Liste Union du Centre',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajouter les nouvelles colonnes à df_filtered avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides_pourcent:
            df_filtered[col] = 0  # Initialisation avec 0

        # Ajouter des colonnes pour compter les occurrences des listes, pour calculer la moyenne
        compte_occurrences = {
            'Liste Divers': 'Occurrences_Liste Divers',
            'Liste Divers droite': 'Occurrences_Liste Divers droite',
            'Liste Divers gauche': 'Occurrences_Liste Divers gauche',
            'Liste Europe-Ecologie-Les Verts': 'Occurrences_Liste Europe-Ecologie-Les Verts',
            'Liste Extrême droite': 'Occurrences_Liste Extrême droite',
            'Liste Extrême gauche': 'Occurrences_Liste Extrême gauche',
            'Liste Front National': 'Occurrences_Liste Front National',
            'Liste Front de Gauche': 'Occurrences_Liste Front de Gauche',
            'Liste Union de la Gauche': 'Occurrences_Liste Union de la Gauche',
            'Liste Union du Centre': 'Occurrences_Liste Union du Centre',
            'Liste Union pour un Mouvement Populaire': 'Occurrences_Liste Union pour un Mouvement Populaire'
        }

        # Initialiser les colonnes de comptage avec 0
        for col in compte_occurrences.values():
            df_filtered[col] = 0

        # Remplir les colonnes de pourcentages en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des pourcentages des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                pourcentage_col = f'% Voix/Exp.{j}' if j > 0 else '% Voix/Exp'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and pourcentage_col in df_filtered.columns:
                    pourcentage_value = row[pourcentage_col]
                    pourcentage_value = float(pourcentage_value) if pd.notnull(pourcentage_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] in compte_occurrences:
                        # Ajouter le pourcentage cumulé
                        moyenne_col = f'% Voix/Exp_{row[label_col]}'
                        df_filtered.at[index, moyenne_col] += pourcentage_value
                        # Incrémenter le compteur d'occurrences
                        compte_col = compte_occurrences[row[label_col]]
                        df_filtered.at[index, compte_col] += 1

        # Calculer la moyenne des pourcentages en divisant le total cumulé par le nombre d'occurrences
        for label, compte_col in compte_occurrences.items():
            moyenne_col = f'% Voix/Exp_{label}'
            df_filtered[moyenne_col] = df_filtered[moyenne_col] / df_filtered[compte_col]
            # Remplacer les NaN résultants de divisions par zéro par 0
            df_filtered[moyenne_col].fillna(0, inplace=True)

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajouter les colonnes de voix et de moyennes de pourcentages que nous avons remplies
            'Voix_Liste Divers': 'sum',
            '% Voix/Exp_Liste Divers': 'mean',
            'Voix_Liste Divers droite': 'sum',
            '% Voix/Exp_Liste Divers droite': 'mean',
            'Voix_Liste Divers gauche': 'sum',
            '% Voix/Exp_Liste Divers gauche': 'mean',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts': 'mean',
            'Voix_Liste Extrême droite': 'sum',
            '% Voix/Exp_Liste Extrême droite': 'mean',
            'Voix_Liste Extrême gauche': 'sum',
            '% Voix/Exp_Liste Extrême gauche': 'mean',
            'Voix_Liste Front National': 'sum',
            '% Voix/Exp_Liste Front National': 'mean',
            'Voix_Liste Front de Gauche': 'sum',
            '% Voix/Exp_Liste Front de Gauche': 'mean',
            'Voix_Liste Union de la Gauche': 'sum',
            '% Voix/Exp_Liste Union de la Gauche': 'mean',
            'Voix_Liste Union du Centre': 'sum',
            '% Voix/Exp_Liste Union du Centre': 'mean',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire': 'mean'
        }).reset_index()

        # Affichage du dataframe regroupé
        st.write(df_grouped)

        # Répartition des abstentions, votants et votes blancs par département
        st.subheader("Répartition des abstentions, votants et votes blancs par département")

        # Création d'un DataFrame pour la visualisation
        df_votes = df_grouped[['Libellé du département', 'Abstentions', 'Votants', 'Blancs']]
        df_votes.set_index('Libellé du département', inplace=True)

        # Graphique à barres
        fig_votes = px.bar(
            df_votes,
            x=df_votes.index,
            y=['Abstentions', 'Votants', 'Blancs'],
            title='Répartition des Abstentions, Votants et Votes Blancs par Département',
            labels={'value': 'Nombre de Votes', 'variable': 'Type de Vote'},
            barmode='stack'
        )

        # Rotation des étiquettes de l'axe x pour une meilleure lisibilité
        fig_votes.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig_votes)

        # Calcul du taux de participation
        df_grouped['taux_participation'] = (df_grouped['Votants'] / df_grouped['Inscrits']) * 100

        # Département avec le plus fort taux de participation
        dep_max_participation = df_grouped.loc[df_grouped['taux_participation'].idxmax()]

        # Affichage du département avec le plus fort taux de participation
        st.subheader("Département avec le plus fort taux de participation")
        st.write(
            f"Département : {dep_max_participation['Libellé du département']} - Taux de participation : {dep_max_participation['taux_participation']:.2f}%"
        )

        # Graphique pour le département avec le plus fort taux de participation
        fig_max = go.Figure(data=[go.Bar(
            x=['Votants', 'Inscrits'],
            y=[dep_max_participation['Votants'], dep_max_participation['Inscrits']],
            text=[dep_max_participation['Votants'], dep_max_participation['Inscrits']],
            textposition='auto',
            marker_color=['green', 'blue']
        )])

        fig_max.update_layout(
            title=f"Répartition des votes dans le département {dep_max_participation['Libellé du département']}",
            xaxis_title="Type",
            yaxis_title="Nombre total",
            width=800,
            height=600
        )
        st.plotly_chart(fig_max)

        # Département avec le moins de participation
        dep_min_participation = df_grouped.loc[df_grouped['taux_participation'].idxmin()]

        # Affichage du département avec le moins de participation
        st.subheader("Département avec le moins de participation")
        st.write(
            f"Département : {dep_min_participation['Libellé du département']} - Taux de participation : {dep_min_participation['taux_participation']:.2f}%"
        )

        # Graphique pour le département avec le moins de participation
        fig_min = go.Figure(data=[go.Bar(
            x=['Votants', 'Inscrits'],
            y=[dep_min_participation['Votants'], dep_min_participation['Inscrits']],
            text=[dep_min_participation['Votants'], dep_min_participation['Inscrits']],
            textposition='auto',
            marker_color=['red', 'blue']
        )])

        fig_min.update_layout(
            title=f"Répartition des votes dans le département {dep_min_participation['Libellé du département']}",
            xaxis_title="Type",
            yaxis_title="Nombre total",
            width=800,
            height=600
        )
        st.plotly_chart(fig_min)

        # Heatmap pour les 5 meilleurs et 5 pires taux de participation
        top_5 = df_grouped.nlargest(5, 'taux_participation')
        bottom_5 = df_grouped.nsmallest(5, 'taux_participation')
        df_heatmap = pd.concat([top_5, bottom_5])

        # Création d'une heatmap

        fig_heatmap = px.imshow(
            df_heatmap[['Libellé du département', 'taux_participation']].set_index('Libellé du département'),
            title="Heatmap des Taux de Participation par Département",
            labels=dict(x="Département", y="Taux de Participation"),
            color_continuous_scale='Plasma',  # Choix d'une palette de couleurs plus vive
            width=1000,  # Largeur de la carte
            height=600  # Hauteur de la carte
        )

        # Personnalisation de la mise en page pour un rendu plus attrayant
        fig_heatmap.update_layout(
            title_font=dict(size=24, family='Arial', color='darkblue'),  # Style du titre
            coloraxis_colorbar=dict(
                title="Participation (%)",
                tickvals=[10, 20, 30, 40, 50],  # Ajustement des valeurs de l'échelle
                ticktext=["10%", "20%", "30%", "40%", "50%"],
                lenmode='fraction',
                len=0.75
            )
        )

        # Afficher la heatmap dans Streamlit
        st.plotly_chart(fig_heatmap, use_container_width=True)

        # Création de la carte
        st.subheader("Carte des 5 meilleurs et 5 pires taux de participation")

        # Coordonnées des départements
        departement_coords = {
            "AIN": [46.2044, 5.2257],
            "AISNE": [49.5686, 3.3609],
            "ALLIER": [46.3416, 3.1985],
            "ALPES DE HAUTE PROVENCE": [44.0666, 6.2314],
            "ALPES MARITIMES": [43.9367, 7.2620],
            "ARDECHE": [44.7951, 4.3702],
            "ARDENNES": [49.7613, 4.7074],
            "ARIEGE": [43.0323, 1.5555],
            "AUBE": [48.3284, 4.0794],
            "AUDE": [43.1575, 2.3997],
            "AVEYRON": [44.2778, 2.5297],
            "BAS RHIN": [48.5846, 7.7507],
            "BOUCHES DU RHONE": [43.4477, 5.4000],
            "CALVADOS": [49.0802, -0.3806],
            "CANTAL": [45.0150, 2.5200],
            "CHARENTE": [45.6913, 0.1590],
            "CHARENTE MARITIME": [45.8750, -0.9513],
            "CHER": [47.0652, 2.3962],
            "CORREZE": [45.2736, 1.7888],
            "CORSE SUD": [41.5917, 8.9961],
            "COTE D'OR": [47.3167, 4.8283],
            "COTES D'ARMOR": [48.5146, -2.8871],
            "CREUSE": [46.0735, 1.9984],
            "DEUX SEVRES": [46.3230, -0.4545],
            "DORDOGNE": [45.1839, 0.7186],
            "DOUBS": [47.2366, 6.0227],
            "DROME": [44.7322, 4.8902],
            "ESSONNE": [48.6314, 2.2379],
            "EURE": [49.0379, 1.2110],
            "EURE ET LOIR": [48.4483, 1.4723],
            "FINISTERE": [48.2321, -4.2217],
            "GARD": [43.9174, 4.4200],
            "GERS": [43.6736, 0.5872],
            "GIRONDE": [44.8378, -0.5792],
            "GUADELOUPE": [16.9950, -62.0671],
            "GUYANE": [4.9372, -52.3262],
            "HAUT RHIN": [47.7486, 7.3398],
            "HAUTE CORSE": [42.2097, 9.1813],
            "HAUTE GARONNE": [43.6047, 1.4442],
            "HAUTE LOIRE": [45.0428, 3.8844],
            "HAUTE MARNE": [48.1110, 5.3302],
            "HAUTE SAONE": [47.6239, 6.1535],
            "HAUTE SAVOIE": [45.8992, 6.1294],
            "HAUTE VIENNE": [45.8350, 1.2624],
            "HAUTES ALPES": [44.5085, 6.2274],
            "HAUTES PYRENEES": [43.0987, 0.1677],
            "HAUTS DE SEINE": [48.8607, 2.2435],
            "HERAULT": [43.6119, 3.8772],
            "ILLE ET VILAINE": [48.1173, -1.6778],
            "INDRE": [46.6969, 1.4686],
            "INDRE ET LOIRE": [47.3936, 0.6897],
            "ISERE": [45.1885, 5.7245],
            "JURA": [46.6754, 5.5744],
            "LA REUNION": [-21.1151, 55.5364],
            "LANDES": [43.9493, -0.5992],
            "LOIR ET CHER": [47.5895, 1.3361],
            "LOIRE": [45.4315, 4.3922],
            "LOIRE ATLANTIQUE": [47.2186, -1.5546],
            "LOIRET": [47.9029, 1.9092],
            "LOT": [44.4475, 1.4403],
            "LOT ET GARONNE": [44.3517, 0.6381],
            "LOZERE": [44.5196, 3.4998],
            "MAINE ET LOIRE": [47.4749, -0.5562],
            "MANCHE": [48.8323, -1.5275],
            "MARNE": [49.0440, 4.0246],
            "MARTINIQUE": [14.6415, -61.0242],
            "MAYENNE": [48.3023, -0.6168],
            "MAYOTTE": [-12.8275, 45.1662],
            "MEURTHE ET MOSELLE": [48.6921, 6.1844],
            "MEUSE": [48.9976, 5.3697],
            "MORBIHAN": [47.8004, -2.7771],
            "MOSELLE": [49.1193, 6.1757],
            "NIEVRE": [47.0514, 3.6567],
            "NORD": [50.6292, 3.0573],
            "NOUVELLE CALEDONIE": [-21.4426, 165.6180],
            "OISE": [49.4162, 2.8261],
            "ORNE": [48.6196, 0.1113],
            "PARIS": [48.8566, 2.3522],
            "PAS DE CALAIS": [50.4252, 2.8312],
            "POLYNESIE FRANCAISE": [-17.6797, -149.4068],
            "PUY DE DOME": [45.7772, 3.0826],
            "PYRENEES ATLANTIQUES": [43.2951, -0.3708],
            "PYRENEES ORIENTALES": [42.6988, 2.8954],
            "RHONE": [45.7640, 4.8357],
            "SAONE ET LOIRE": [46.7556, 4.8535],
            "SARTHE": [48.0077, 0.1996],
            "SAVOIE": [45.5646, 5.9178],
            "SEINE ET MARNE": [48.6082, 2.6021],
            "SEINE MARITIME": [49.4432, 1.0993],
            "SEINE SAINT-DENIS": [48.9356, 2.3535],
            "SOMME": [49.9219, 2.3007],
            "TARN": [43.8939, 2.1499],
            "TARN ET GARONNE": [44.0068, 1.3555],
            "TERRITOIRE DE BELFORT": [47.6383, 6.8628],
            "VAL D'OISE": [49.0514, 2.1160],
            "VAL DE MARNE": [48.7920, 2.4712],
            "VAR": [43.4667, 6.2211],
            "VAUCLUSE": [44.0563, 5.0501],
            "VENDEE": [46.6705, -1.4269],
            "VIENNE": [46.5802, 0.3404],
            "VOSGES": [48.2156, 6.4238],
            "YONNE": [47.7973, 3.5674],
            "YVELINES": [48.7802, 1.9876]
        }

        # Créer la carte centrée sur la France
        map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

        # Heatmap pour les 10 meilleurs et 10 pires taux de participation
        top_10 = df_grouped.nlargest(15, 'taux_participation')
        bottom_10 = df_grouped.nsmallest(15, 'taux_participation')
        df_heatmap = pd.concat([top_10, bottom_10])

        # Ajouter les départements avec le plus de votants à la carte
        for index, row in top_10.iterrows():
            departement_name = row['Libellé du département']
            if departement_name in departement_coords:
                lat, lon = departement_coords[departement_name]
                folium.CircleMarker(
                    location=[lat, lon],
                    radius=10,
                    popup=f"Top Participation - {departement_name}: {row['taux_participation']:.2f}%",
                    color="green",
                    fill=True,
                    fill_color="green"
                ).add_to(map)

        # Ajouter les départements avec le moins de votants à la carte
        for index, row in bottom_10.iterrows():
            departement_name = row['Libellé du département']
            if departement_name in departement_coords:
                lat, lon = departement_coords[departement_name]
                folium.CircleMarker(
                    location=[lat, lon],
                    radius=10,
                    popup=f"Pire Participation - {departement_name}: {row['taux_participation']:.2f}%",
                    color="red",
                    fill=True,
                    fill_color="red"
                ).add_to(map)

        # Afficher la carte dans Streamlit
        st_folium(map, width=700, height=500)

    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")


elif page == "Répartition des voix par parti":
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; border: 2px solid black; padding: 10px; border-radius: 10px; background-color: #f0f0f0;">
            <h2 style="text-align: center; color: black; margin: 0;">Répartition des voix par parti</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.title("Tableau de Données nettoyé")


    # Fonction pour charger les données avec mise en cache
    @st.cache_data
    def load_data(file_path):
        # Lire le fichier CSV
        data = pd.read_csv(file_path, sep=';', encoding='ISO-8859-1', on_bad_lines='skip')
        return data


    # Chargement des données avec mise en cache
    url = r"C:\Users\oumis\OneDrive\Documents\goodfichier.csv"
    df = load_data(url)

    # Définir les colonnes pertinentes à garder
    colonnes_a_garder = [
        'Code du département',
        'Libellé du département',
        'Inscrits',
        'Abstentions',
        '% Abs/Ins',
        'Votants',
        '% Vot/Ins',
        'Blancs',
        '% BlBlancs/Vot',
        'Exprimés',
        'Libellé Abrégé Liste',
        'Voix',
        '% Voix/Exp'
    ]

    # Ajouter les colonnes supplémentaires jusqu'à 30
    for i in range(1, 31):
        colonnes_a_garder.extend([
            f'Libellé Abrégé Liste.{i}',
            f'Voix.{i}',
            f'% Voix/Exp.{i}'
        ])

    # Filtrer les données pour garder seulement les colonnes pertinentes
    df_filtered = df[colonnes_a_garder]

    # Remplacer les valeurs manquantes (None ou NaN) par 0
    df_filtered.fillna(0, inplace=True)

    # Liste des colonnes à convertir
    colonnes_a_convertir = [
        '% Abs/Ins', '% Vot/Ins', '% BlBlancs/Vot',
        '% Voix/Exp', '% Voix/Exp.1', '% Voix/Exp.2', '% Voix/Exp.3',
        '% Voix/Exp.4', '% Voix/Exp.5', '% Voix/Exp.6', '% Voix/Exp.7',
        '% Voix/Exp.8', '% Voix/Exp.9', '% Voix/Exp.10', '% Voix/Exp.11',
        '% Voix/Exp.12', '% Voix/Exp.13', '% Voix/Exp.14', '% Voix/Exp.15',
        '% Voix/Exp.16', '% Voix/Exp.17', '% Voix/Exp.18', '% Voix/Exp.19',
        '% Voix/Exp.20', '% Voix/Exp.21', '% Voix/Exp.22', '% Voix/Exp.23',
        '% Voix/Exp.24', '% Voix/Exp.25', '% Voix/Exp.26', '% Voix/Exp.27',
        '% Voix/Exp.28', '% Voix/Exp.29', '% Voix/Exp.30'
    ]

    # Conversion des colonnes en float
    for col in colonnes_a_convertir:
        df_filtered[col] = pd.to_numeric(df_filtered[col].str.replace(',', '.'), errors='coerce')

    # Agrégation par département
    try:
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            "Inscrits": "sum",
            "Abstentions": "sum",
            "% Abs/Ins": "mean",
            "Votants": "sum",
            "% Vot/Ins": "mean",
            "Blancs": "sum",
            "% BlBlancs/Vot": "mean",
            "Exprimés": "sum",

            "Libellé Abrégé Liste": "first",
            "Voix": "sum",
            "% Voix/Exp": "mean",

            "Libellé Abrégé Liste.1": "first",
            "Voix.1": "sum",
            '% Voix/Exp.1': "mean",

            "Libellé Abrégé Liste.2": "first",
            "Voix.2": "sum",
            '% Voix/Exp.2': "mean",

            "Libellé Abrégé Liste.3": "first",
            "Voix.3": "sum",
            '% Voix/Exp.3': "mean",

            "Libellé Abrégé Liste.4": "first",
            "Voix.4": "sum",
            '% Voix/Exp.4': "mean",

            "Libellé Abrégé Liste.5": "first",
            "Voix.5": "sum",
            '% Voix/Exp.5': "mean",

            "Libellé Abrégé Liste.6": "first",
            "Voix.6": "sum",
            '% Voix/Exp.6': "mean",

            "Libellé Abrégé Liste.7": "first",
            "Voix.7": "sum",
            '% Voix/Exp.7': "mean",

            "Libellé Abrégé Liste.8": "first",
            "Voix.8": "sum",
            '% Voix/Exp.8': "mean",

            "Libellé Abrégé Liste.9": "first",
            "Voix.9": "sum",
            '% Voix/Exp.9': "mean",

            "Libellé Abrégé Liste.10": "first",
            "Voix.10": "sum",
            '% Voix/Exp.10': "mean",

            "Libellé Abrégé Liste.11": "first",
            "Voix.11": "sum",
            '% Voix/Exp.11': "mean",

            "Libellé Abrégé Liste.12": "first",
            "Voix.12": "sum",
            '% Voix/Exp.12': "mean",

            "Libellé Abrégé Liste.13": "first",
            "Voix.13": "sum",
            '% Voix/Exp.13': "mean",

            "Libellé Abrégé Liste.14": "first",
            "Voix.14": "sum",
            '% Voix/Exp.14': "mean",

            "Libellé Abrégé Liste.15": "first",
            "Voix.15": "sum",
            '% Voix/Exp.15': "mean",

            "Libellé Abrégé Liste.16": "first",
            "Voix.16": "sum",
            '% Voix/Exp.16': "mean",

            "Libellé Abrégé Liste.17": "first",
            "Voix.17": "sum",
            '% Voix/Exp.17': "mean",

            "Libellé Abrégé Liste.18": "first",
            "Voix.18": "sum",
            '% Voix/Exp.18': "mean",

            "Libellé Abrégé Liste.19": "first",
            "Voix.19": "sum",
            '% Voix/Exp.19': "mean",

            "Libellé Abrégé Liste.20": "first",
            "Voix.20": "sum",
            '% Voix/Exp.20': "mean",

            "Libellé Abrégé Liste.21": "first",
            "Voix.21": "sum",
            '% Voix/Exp.21': "mean",

            "Libellé Abrégé Liste.22": "first",
            "Voix.22": "sum",
            '% Voix/Exp.22': "mean",

            "Libellé Abrégé Liste.23": "first",
            "Voix.23": "sum",
            '% Voix/Exp.23': "mean",

            "Libellé Abrégé Liste.24": "first",
            "Voix.24": "sum",
            '% Voix/Exp.24': "mean",

            "Libellé Abrégé Liste.25": "first",
            "Voix.25": "sum",
            '% Voix/Exp.25': "mean",

            "Libellé Abrégé Liste.26": "first",
            "Voix.26": "sum",
            '% Voix/Exp.26': "mean",

            "Libellé Abrégé Liste.27": "first",
            "Voix.27": "sum",
            '% Voix/Exp.27': "mean",

            "Libellé Abrégé Liste.28": "first",
            "Voix.28": "sum",
            '% Voix/Exp.28': "mean",

            "Libellé Abrégé Liste.29": "first",
            "Voix.29": "sum",
            '% Voix/Exp.29': "mean",

            "Libellé Abrégé Liste.30": "first",
            "Voix.30": "sum",
            '% Voix/Exp.30': "mean",

        }).reset_index()

        # Ajout des nouvelles colonnes vides
        nouvelles_colonnes_vides = [
            'Voix_Liste Divers', '% Voix/Exp_Liste Divers',
            'Voix_Liste Divers droite', '% Voix/Exp_Liste Divers droite',
            'Voix_Liste Divers gauche', '% Voix/Exp_Liste Divers gauche',
            'Voix_Liste Europe-Ecologie-Les Verts', '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            'Voix_Liste Extrême droite', '% Voix/Exp_Liste Extrême droite',
            'Voix_Liste Extrême gauche', '% Voix/Exp_Liste Extrême gauche',
            'Voix_Liste Front National', '% Voix/Exp_Liste Front National',
            'Voix_Liste Front de Gauche', '% Voix/Exp_Liste Front de Gauche',
            'Voix_Liste Union de la Gauche', '% Voix/Exp_Liste Union de la Gauche',
            'Voix_Liste Union du Centre', '% Voix/Exp_Liste Union du Centre',
            'Voix_Liste Union pour un Mouvement Populaire', '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajouter les nouvelles colonnes à df_grouped avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides:
            df_filtered[col] = 0  # Initialisation avec 0

        # Remplir les colonnes de voix en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                voix_col = f'Voix.{j}' if j > 0 else 'Voix'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and voix_col in df_filtered.columns:
                    voix_value = row[voix_col]
                    voix_value = float(voix_value) if pd.notnull(voix_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] == 'Liste Divers':
                        df_filtered.at[index, 'Voix_Liste Divers'] += voix_value
                    elif row[label_col] == 'Liste Divers droite':
                        df_filtered.at[index, 'Voix_Liste Divers droite'] += voix_value
                    elif row[label_col] == 'Liste Divers gauche':
                        df_filtered.at[index, 'Voix_Liste Divers gauche'] += voix_value
                    elif row[label_col] == 'Liste Europe-Ecologie-Les Verts':
                        df_filtered.at[index, 'Voix_Liste Europe-Ecologie-Les Verts'] += voix_value
                    elif row[label_col] == 'Liste Extrême droite':
                        df_filtered.at[index, 'Voix_Liste Extrême droite'] += voix_value
                    elif row[label_col] == 'Liste Extrême gauche':
                        df_filtered.at[index, 'Voix_Liste Extrême gauche'] += voix_value
                    elif row[label_col] == 'Liste Front National':
                        df_filtered.at[index, 'Voix_Liste Front National'] += voix_value
                    elif row[label_col] == 'Liste Front de Gauche':
                        df_filtered.at[index, 'Voix_Liste Front de Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union de la Gauche':
                        df_filtered.at[index, 'Voix_Liste Union de la Gauche'] += voix_value
                    elif row[label_col] == 'Liste Union du Centre':
                        df_filtered.at[index, 'Voix_Liste Union du Centre'] += voix_value
                    elif row[label_col] == 'Liste Union pour un Mouvement Populaire':
                        df_filtered.at[index, 'Voix_Liste Union pour un Mouvement Populaire'] += voix_value

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajouter les colonnes que nous avons remplies
            'Voix_Liste Divers': 'sum',
            'Voix_Liste Divers droite': 'sum',
            'Voix_Liste Divers gauche': 'sum',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            'Voix_Liste Extrême droite': 'sum',
            'Voix_Liste Extrême gauche': 'sum',
            'Voix_Liste Front National': 'sum',
            'Voix_Liste Front de Gauche': 'sum',
            'Voix_Liste Union de la Gauche': 'sum',
            'Voix_Liste Union du Centre': 'sum',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum'
        }).reset_index()

        # Ajout des nouvelles colonnes pour les moyennes des pourcentages des voix
        nouvelles_colonnes_vides_pourcent = [
            '% Voix/Exp_Liste Divers',
            '% Voix/Exp_Liste Divers droite',
            '% Voix/Exp_Liste Divers gauche',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts',
            '% Voix/Exp_Liste Extrême droite',
            '% Voix/Exp_Liste Extrême gauche',
            '% Voix/Exp_Liste Front National',
            '% Voix/Exp_Liste Front de Gauche',
            '% Voix/Exp_Liste Union de la Gauche',
            '% Voix/Exp_Liste Union du Centre',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire'
        ]

        # Ajouter les nouvelles colonnes à df_filtered avec une valeur initiale de 0
        for col in nouvelles_colonnes_vides_pourcent:
            df_filtered[col] = 0  # Initialisation avec 0

        # Ajouter des colonnes pour compter les occurrences des listes, pour calculer la moyenne
        compte_occurrences = {
            'Liste Divers': 'Occurrences_Liste Divers',
            'Liste Divers droite': 'Occurrences_Liste Divers droite',
            'Liste Divers gauche': 'Occurrences_Liste Divers gauche',
            'Liste Europe-Ecologie-Les Verts': 'Occurrences_Liste Europe-Ecologie-Les Verts',
            'Liste Extrême droite': 'Occurrences_Liste Extrême droite',
            'Liste Extrême gauche': 'Occurrences_Liste Extrême gauche',
            'Liste Front National': 'Occurrences_Liste Front National',
            'Liste Front de Gauche': 'Occurrences_Liste Front de Gauche',
            'Liste Union de la Gauche': 'Occurrences_Liste Union de la Gauche',
            'Liste Union du Centre': 'Occurrences_Liste Union du Centre',
            'Liste Union pour un Mouvement Populaire': 'Occurrences_Liste Union pour un Mouvement Populaire'
        }

        # Initialiser les colonnes de comptage avec 0
        for col in compte_occurrences.values():
            df_filtered[col] = 0

        # Remplir les colonnes de pourcentages en fonction de la liste correspondante
        for index, row in df_filtered.iterrows():
            for j in range(0, 31):  # Parcourir les 30 colonnes des pourcentages des voix
                label_col = f'Libellé Abrégé Liste.{j}' if j > 0 else 'Libellé Abrégé Liste'
                pourcentage_col = f'% Voix/Exp.{j}' if j > 0 else '% Voix/Exp'

                # Vérifier que les colonnes existent
                if label_col in df_filtered.columns and pourcentage_col in df_filtered.columns:
                    pourcentage_value = row[pourcentage_col]
                    pourcentage_value = float(pourcentage_value) if pd.notnull(pourcentage_value) else 0

                    # Identifier la colonne correspondante en fonction du libellé de la liste
                    if row[label_col] in compte_occurrences:
                        # Ajouter le pourcentage cumulé
                        moyenne_col = f'% Voix/Exp_{row[label_col]}'
                        df_filtered.at[index, moyenne_col] += pourcentage_value
                        # Incrémenter le compteur d'occurrences
                        compte_col = compte_occurrences[row[label_col]]
                        df_filtered.at[index, compte_col] += 1

        # Calculer la moyenne des pourcentages en divisant le total cumulé par le nombre d'occurrences
        for label, compte_col in compte_occurrences.items():
            moyenne_col = f'% Voix/Exp_{label}'
            df_filtered[moyenne_col] = df_filtered[moyenne_col] / df_filtered[compte_col]
            # Remplacer les NaN résultants de divisions par zéro par 0
            df_filtered[moyenne_col].fillna(0, inplace=True)

        # Maintenant, agrégation par département pour résumer les données
        df_grouped = df_filtered.groupby("Libellé du département").agg({
            'Inscrits': 'sum',
            'Abstentions': 'sum',
            '% Abs/Ins': 'mean',
            'Votants': 'sum',
            '% Vot/Ins': 'mean',
            'Blancs': 'sum',
            '% BlBlancs/Vot': 'mean',
            'Exprimés': 'sum',
            # Ajouter les colonnes de voix et de moyennes de pourcentages que nous avons remplies
            'Voix_Liste Divers': 'sum',
            '% Voix/Exp_Liste Divers': 'mean',
            'Voix_Liste Divers droite': 'sum',
            '% Voix/Exp_Liste Divers droite': 'mean',
            'Voix_Liste Divers gauche': 'sum',
            '% Voix/Exp_Liste Divers gauche': 'mean',
            'Voix_Liste Europe-Ecologie-Les Verts': 'sum',
            '% Voix/Exp_Liste Europe-Ecologie-Les Verts': 'mean',
            'Voix_Liste Extrême droite': 'sum',
            '% Voix/Exp_Liste Extrême droite': 'mean',
            'Voix_Liste Extrême gauche': 'sum',
            '% Voix/Exp_Liste Extrême gauche': 'mean',
            'Voix_Liste Front National': 'sum',
            '% Voix/Exp_Liste Front National': 'mean',
            'Voix_Liste Front de Gauche': 'sum',
            '% Voix/Exp_Liste Front de Gauche': 'mean',
            'Voix_Liste Union de la Gauche': 'sum',
            '% Voix/Exp_Liste Union de la Gauche': 'mean',
            'Voix_Liste Union du Centre': 'sum',
            '% Voix/Exp_Liste Union du Centre': 'mean',
            'Voix_Liste Union pour un Mouvement Populaire': 'sum',
            '% Voix/Exp_Liste Union pour un Mouvement Populaire': 'mean'
        }).reset_index()

        # Affichage du dataframe regroupé
        st.subheader("Données regroupées par département :")
        st.write(df_grouped)

        ####
        # Coordonnées des départements
        departement_coords = {
            "AIN": [46.2044, 5.2257],
            "AISNE": [49.5686, 3.3609],
            "ALLIER": [46.3416, 3.1985],
            "ALPES DE HAUTE PROVENCE": [44.0666, 6.2314],
            "ALPES MARITIMES": [43.9367, 7.2620],
            "ARDECHE": [44.7951, 4.3702],
            "ARDENNES": [49.7613, 4.7074],
            "ARIEGE": [43.0323, 1.5555],
            "AUBE": [48.3284, 4.0794],
            "AUDE": [43.1575, 2.3997],
            "AVEYRON": [44.2778, 2.5297],
            "BAS RHIN": [48.5846, 7.7507],
            "BOUCHES DU RHONE": [43.4477, 5.4000],
            "CALVADOS": [49.0802, -0.3806],
            "CANTAL": [45.0150, 2.5200],
            "CHARENTE": [45.6913, 0.1590],
            "CHARENTE MARITIME": [45.8750, -0.9513],
            "CHER": [47.0652, 2.3962],
            "CORREZE": [45.2736, 1.7888],
            "CORSE SUD": [41.5917, 8.9961],
            "COTE D'OR": [47.3167, 4.8283],
            "COTES D'ARMOR": [48.5146, -2.8871],
            "CREUSE": [46.0735, 1.9984],
            "DEUX SEVRES": [46.3230, -0.4545],
            "DORDOGNE": [45.1839, 0.7186],
            "DOUBS": [47.2366, 6.0227],
            "DROME": [44.7322, 4.8902],
            "ESSONNE": [48.6314, 2.2379],
            "EURE": [49.0379, 1.2110],
            "EURE ET LOIR": [48.4483, 1.4723],
            "FINISTERE": [48.2321, -4.2217],
            "GARD": [43.9174, 4.4200],
            "GERS": [43.6736, 0.5872],
            "GIRONDE": [44.8378, -0.5792],
            "GUADELOUPE": [16.9950, -62.0671],
            "GUYANE": [4.9372, -52.3262],
            "HAUT RHIN": [47.7486, 7.3398],
            "HAUTE CORSE": [42.2097, 9.1813],
            "HAUTE GARONNE": [43.6047, 1.4442],
            "HAUTE LOIRE": [45.0428, 3.8844],
            "HAUTE MARNE": [48.1110, 5.3302],
            "HAUTE SAONE": [47.6239, 6.1535],
            "HAUTE SAVOIE": [45.8992, 6.1294],
            "HAUTE VIENNE": [45.8350, 1.2624],
            "HAUTES ALPES": [44.5085, 6.2274],
            "HAUTES PYRENEES": [43.0987, 0.1677],
            "HAUTS DE SEINE": [48.8607, 2.2435],
            "HERAULT": [43.6119, 3.8772],
            "ILLE ET VILAINE": [48.1173, -1.6778],
            "INDRE": [46.6969, 1.4686],
            "INDRE ET LOIRE": [47.3936, 0.6897],
            "ISERE": [45.1885, 5.7245],
            "JURA": [46.6754, 5.5744],
            "LA REUNION": [-21.1151, 55.5364],
            "LANDES": [43.9493, -0.5992],
            "LOIR ET CHER": [47.5895, 1.3361],
            "LOIRE": [45.4315, 4.3922],
            "LOIRE ATLANTIQUE": [47.2186, -1.5546],
            "LOIRET": [47.9029, 1.9092],
            "LOT": [44.4475, 1.4403],
            "LOT ET GARONNE": [44.3517, 0.6381],
            "LOZERE": [44.5196, 3.4998],
            "MAINE ET LOIRE": [47.4749, -0.5562],
            "MANCHE": [48.8323, -1.5275],
            "MARNE": [49.0440, 4.0246],
            "MARTINIQUE": [14.6415, -61.0242],
            "MAYENNE": [48.3023, -0.6168],
            "MAYOTTE": [-12.8275, 45.1662],
            "MEURTHE ET MOSELLE": [48.6921, 6.1844],
            "MEUSE": [48.9976, 5.3697],
            "MORBIHAN": [47.8004, -2.7771],
            "MOSELLE": [49.1193, 6.1757],
            "NIEVRE": [47.0514, 3.6567],
            "NORD": [50.6292, 3.0573],
            "NOUVELLE CALEDONIE": [-21.4426, 165.6180],
            "OISE": [49.4162, 2.8261],
            "ORNE": [48.6196, 0.1113],
            "PARIS": [48.8566, 2.3522],
            "PAS DE CALAIS": [50.4252, 2.8312],
            "POLYNESIE FRANCAISE": [-17.6797, -149.4068],
            "PUY DE DOME": [45.7772, 3.0826],
            "PYRENEES ATLANTIQUES": [43.2951, -0.3708],
            "PYRENEES ORIENTALES": [42.6988, 2.8954],
            "RHONE": [45.7640, 4.8357],
            "SAONE ET LOIRE": [46.7556, 4.8535],
            "SARTHE": [48.0077, 0.1996],
            "SAVOIE": [45.5646, 5.9178],
            "SEINE ET MARNE": [48.6082, 2.6021],
            "SEINE MARITIME": [49.4432, 1.0993],
            "SEINE SAINT-DENIS": [48.9356, 2.3535],
            "SOMME": [49.9219, 2.3007],
            "TARN": [43.8939, 2.1499],
            "TARN ET GARONNE": [44.0068, 1.3555],
            "TERRITOIRE DE BELFORT": [47.6383, 6.8628],
            "VAL D'OISE": [49.0514, 2.1160],
            "VAL DE MARNE": [48.7920, 2.4712],
            "VAR": [43.4667, 6.2211],
            "VAUCLUSE": [44.0563, 5.0501],
            "VENDEE": [46.6705, -1.4269],
            "VIENNE": [46.5802, 0.3404],
            "VOSGES": [48.2156, 6.4238],
            "YONNE": [47.7973, 3.5674],
            "YVELINES": [48.7802, 1.9876]
        }

        parti = df_grouped[['Voix_Liste Divers',
            'Voix_Liste Divers droite',
            'Voix_Liste Divers gauche',
            'Voix_Liste Europe-Ecologie-Les Verts',
            'Voix_Liste Extrême droite',
            'Voix_Liste Extrême gauche',
            'Voix_Liste Front National',
            'Voix_Liste Front de Gauche',
            'Voix_Liste Union de la Gauche',
            'Voix_Liste Union du Centre',
            'Voix_Liste Union pour un Mouvement Populaire']]
        total_voix_par_parti = parti.sum()

        fig = px.pie(
            names=total_voix_par_parti.index,
            values=total_voix_par_parti.values,
            title="Répartition des voix par parti politique",
            labels={'names': 'Partis politiques', 'values': 'Nombre de voix'}
        )
        st.plotly_chart(fig)

        # Calcul du taux de participation
        df_grouped['taux_participation'] = (df_grouped['Votants'] / df_grouped['Inscrits']) * 100

        # Trier les départements par taux de participation
        df_sorted_participation = df_grouped.sort_values('taux_participation', ascending=False)

        # Graphique interactif pour les 10 départements avec le plus haut taux de participation
        top_10 = df_sorted_participation.head(10)
        fig_top = px.bar(
            top_10,
            x='Libellé du département',
            y='taux_participation',
            title='Top 10 départements - Taux de participation',
            labels={'taux_participation': 'Taux de participation (%)', 'Libellé du département': 'Département'},
            color='taux_participation',
            color_continuous_scale='greens',
            height=500
        )
        fig_top.update_layout(xaxis_title="Département", yaxis_title="Taux de participation (%)")

        # Afficher le graphique interactif dans Streamlit
        st.plotly_chart(fig_top)

        # Graphique interactif pour les 10 départements avec le plus bas taux de participation
        bottom_10 = df_sorted_participation.tail(10)
        fig_bottom = px.bar(
            bottom_10,
            x='Libellé du département',
            y='taux_participation',
            title='Bottom 10 départements - Taux de participation',
            labels={'taux_participation': 'Taux de participation (%)', 'Libellé du département': 'Département'},
            color='taux_participation',
            color_continuous_scale='reds',
            height=500
        )
        fig_bottom.update_layout(xaxis_title="Département", yaxis_title="Taux de participation (%)")

        # Afficher le graphique interactif dans Streamlit
        st.plotly_chart(fig_bottom)

        # Heatmap 2 ####
        # Titre encadré et centré
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center; border: 2px solid #4CAF50; padding: 10px; border-radius: 10px; background-color: #f0f0f0;">
                <h2 style="text-align: center; color: #4CAF50; margin: 0;">Parti majoritaire par département - Élections européennes 2014</h2>
            </div>
            """,
            unsafe_allow_html=True
        )
        # Calculer le parti avec le plus de voix pour chaque département
        df_grouped['Parti_majoritaire'] = df_grouped[
            ['Voix_Liste Divers', 'Voix_Liste Divers droite', 'Voix_Liste Divers gauche',
             'Voix_Liste Europe-Ecologie-Les Verts', 'Voix_Liste Extrême droite',
             'Voix_Liste Extrême gauche', 'Voix_Liste Front National',
             'Voix_Liste Front de Gauche', 'Voix_Liste Union de la Gauche',
             'Voix_Liste Union du Centre', 'Voix_Liste Union pour un Mouvement Populaire']
        ].idxmax(axis=1)

        # Remplacer les valeurs pour avoir des libellés plus clairs
        df_grouped['Parti_majoritaire'] = df_grouped['Parti_majoritaire'].replace({
            'Voix_Liste Divers': 'Liste Divers',
            'Voix_Liste Divers droite': 'Liste Divers droite',
            'Voix_Liste Divers gauche': 'Liste Divers gauche',
            'Voix_Liste Europe-Ecologie-Les Verts': 'Liste Europe-Ecologie-Les Verts',
            'Voix_Liste Extrême droite': 'Liste Extrême droite',
            'Voix_Liste Extrême gauche': 'Liste Extrême gauche',
            'Voix_Liste Front National': 'Liste Front National',
            'Voix_Liste Front de Gauche': 'Liste Front de Gauche',
            'Voix_Liste Union de la Gauche': 'Liste Union de la Gauche',
            'Voix_Liste Union du Centre': 'Liste Union du Centre',
            'Voix_Liste Union pour un Mouvement Populaire': 'Liste Union pour un Mouvement Populaire'
        })

        # Ajouter les coordonnées géographiques pour chaque département
        df_grouped['Latitude'] = df_grouped['Libellé du département'].map(
            lambda x: departement_coords.get(x.upper(), [0, 0])[0])
        df_grouped['Longitude'] = df_grouped['Libellé du département'].map(
            lambda x: departement_coords.get(x.upper(), [0, 0])[1])

        # Couleurs personnalisées plus vives pour les partis
        couleurs_vives = {
            'Liste Front National': '#1f78b4',  # Bleu vif
            'Liste Union pour un Mouvement Populaire': '#ff7f00',  # Orange vif
            'Liste Union de la Gauche': '#e31a1c',  # Rouge vif
            'Liste Europe-Ecologie-Les Verts': '#33a02c',  # Vert vif
            'Liste Divers gauche': '#6a3d9a',  # Violet vif
            'Liste Union du Centre': '#fb9a99',  # Rose vif
        }

        # Créer la carte 3D avec Plotly, en utilisant la taille pour refléter le taux de participation
        fig = px.scatter_mapbox(
            df_grouped,
            lat='Latitude',
            lon='Longitude',
            text='Libellé du département',
            color='Parti_majoritaire',
            size='taux_participation',  # Utiliser le taux de participation pour la taille des points
            color_discrete_map=couleurs_vives,  # Couleurs vives pour chaque parti
            title="Parti majoritaire par département - Vue 3D",
            height=1000,  # Hauteur de la carte pour un affichage plus grand
            width=1500,  # Largeur de la carte pour un affichage plus grand
            zoom=5  # Zoom pour centrer sur la France
        )

        # Ajuster les paramètres de la carte pour une vue en 3D
        fig.update_layout(
            mapbox_style="open-street-map",
            mapbox=dict(
                center=dict(lat=46.5, lon=2.5),  # Centrer sur la France
                zoom=5,  # Niveau de zoom pour inclure toute la France
                pitch=50,  # Inclinaison pour une vue 3D
            ),
            margin=dict(l=0, r=0, t=50, b=0),  # Marges minimales pour maximiser la carte
            title_font=dict(size=24, family='Arial', color='darkblue')  # Style du titre
        )

        # Personnaliser les points pour améliorer la visibilité et ajouter un effet 3D dynamique
        fig.update_traces(
            marker=dict(
                size=10,  # Taille des points augmentée
                opacity=0.8  # Légère transparence pour visualiser les superpositions
            )
        )

        # Afficher la carte 3D dans Streamlit
        st.plotly_chart(fig, use_container_width=True)


    except Exception as e:
        st.error(f"Une erreur s'est produite : {e}")

