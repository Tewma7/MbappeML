import pandas as pd
import numpy as np

#Fonctions
#Supprime les colonnes inutiles
def dropCol(dataset):
    dataset = dataset.drop(
        columns=['Photo', 'Flag', 'Club Logo', 'Work Rate', 'Body Type', 'Real Face', 'Jersey Number', 'Joined',
                 'Loaned From', 'Contract Valid Until', 'Release Clause', 'DefensiveAwareness', 'Crossing', 'Finishing',
                 'HeadingAccuracy',
                 'ShortPassing', 'Volleys', 'Dribbling', 'Curve', 'FKAccuracy',
                 'LongPassing', 'BallControl', 'Acceleration', 'SprintSpeed', 'Agility',
                 'Reactions', 'Balance', 'ShotPower', 'Jumping', 'Stamina', 'Strength',
                 'LongShots', 'Aggression', 'Interceptions', 'Positioning', 'Vision',
                 'Penalties', 'Composure', 'Marking', 'StandingTackle', 'SlidingTackle',
                 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes'])

#Transforme les string en int (0=res, 1=sub, 2=autre)
def int_position(dataset):
  position= dataset['Position'].apply(str)
  for k in range(len(position)):
    if 'RES' in position[k]:
      position[k] = 0
    elif 'SUB' in position[k]:
      position[k] = 1
    else:
      position[k] = 2
  dataset['Position'] = position

#Transforme les string en int (pied droit=1, gauche=0)
def Preferred_Foot(dataset):
  foot= dataset['Preferred Foot']
  for k in range(len(foot)):
    if foot[k]=='Right':
      foot[k] = 1
    else:
      foot[k] = 0
  dataset['Preferred Foot'] = foot


#Chargement des données
data_21 = pd.read_csv("FIFA21_official_data.csv")
data_20 = pd.read_csv("FIFA20_official_data.csv")
data_19 = pd.read_csv("FIFA19_official_data.csv")
data_19['DefensiveAwareness'] = np.nan  # Ajout de la colonne pour le dataset 2019 pour avoir le même nombre de colonne

#Suppression des colonnes inutiles
data_19_2 = dropCol(data_19)
data_20_2 = dropCol(data_20)
data_21_2 = dropCol(data_21)

#Transformation des positions
int_position(data_19_2)
int_position(data_20_2)
int_position(data_21_2)

#Transformation des pieds
Preferred_Foot(data_19_2)
Preferred_Foot(data_20_2)
Preferred_Foot(data_21_2)

