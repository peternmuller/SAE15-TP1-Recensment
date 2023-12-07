import csv
from pylab import *

def importation(fichier,separateur):									#permet d'importer un csv dans une liste en précisant le fichier et le séparateur
	liste=[]
	with open(fichier,newline='',encoding="UTF-8") as csvfile:
		reader=csv.reader(csvfile,delimiter=separateur)
		for row in reader:
			liste.append(row)
	return liste

donnees_2008 = importation("donnees_2008.csv",",")
donnees_2016 = importation("donnees_2016.csv",",")
donnees_2021 = importation("donnees_2021.csv",";")
metadonnees_communes = importation("metadonnees_communes.csv",";")
#On a maintenant 4 listes qui contiennent toutes les infos des fichiers

def selec_region(donnees, annee, code_dep, meta, agglo):				#permet de ne garder que les informations des villes de l'agglomération 
	liste=[]
	if annee < 2020 :													#pour différencier les fichiers, l'ordre des colonnes n'est pas le même partout
		for ligne in donnees :
			if ligne[2].isdigit() and int(ligne[2]) == code_dep and ligne[6] in agglo:	#Si le numéro est un chiffre, on vérifie si le déartement est 89 et on ne garde que les villes de l'agglomération totale
				liste.append([ligne[6],int(ligne[7]),int(ligne[8]),int(ligne[9])])		#la liste contient dans l'ordre : nom de la commune, population municipale, population comptée à part et population totale
	else :
		for ligne in donnees :
			if ligne[1].isdigit() and int(ligne[1]) == code_dep:		#Si le numéro est un chiffre, on vérifie si le déartement est 89 
				for communes in meta :									#On ouvre la liste qui contient les numéros et les noms des communes 
					if ligne[2] == communes[2] and communes[3] in agglo:	#On fait correspondre la numéro au nom de la commune, si la commune est dans l'agglomération:
						liste.append([communes[3],int(ligne[3]),int(ligne[4]),int(ligne[5])])	#la liste contient dans l'ordre : nom de la commune, population municipale, population comptée à part et population totale
	return liste

agglo_total=["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy", "Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives-Sainte-Camille", "Gurgy","Gy-l'Évêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny", "Quenne", "Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"]
agglo_imm=["Appoigny","Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"]

donnees_2008=selec_region(donnees_2008, 2008,89, metadonnees_communes,agglo_total)
donnees_2016=selec_region(donnees_2016, 2016,89, metadonnees_communes,agglo_total)
donnees_2021=selec_region(donnees_2021, 2021,89, metadonnees_communes,agglo_total)
#On a maintenant 3 listes qui contiennent dans l'ordre : nom de la commune, population municipale, population comptée à part et population totale

donnees=[]					#liste de 29 entrées pour les 29 communes avec leur population en 2008, 2016 et 2021
for i in range(29):
	donnees.append([donnees_2008[i][0],donnees_2008[i][3],donnees_2016[i][3],donnees_2021[i][3]])

donnees_agglo=[0,0,0]		#liste de 3 entrées pour la population en 2008, 2016 et 2021 sur l'agglomération totale
for commune in donnees:
	for annee in range(3):
		donnees_agglo[annee]=donnees_agglo[annee]+commune[annee+1]

donnees_agglo_imm=[0,0,0]	#liste de 3 entrées pour la population en 2008, 2016 et 2021 sur l'agglomération immédiate
for commune in donnees:
	for annee in range(3):
		if commune[0] in agglo_imm:
			donnees_agglo_imm[annee]=donnees_agglo_imm[annee]+commune[annee+1]
			
donnees_aux=[0,0,0]			#liste de 3 entrées pour la population en 2008, 2016 et 2021 sur Auxerre
for commune in donnees:
	for annee in range(3):
		if commune[0] == "Auxerre":
			donnees_aux[annee]=commune[annee+1]

annees=[2008,2016,2021]
figure("Evolution de la population") 
plot(annees,donnees_agglo,label="Agglomération totale")
plot(annees,donnees_agglo_imm,label="Agglomération immédiate")
plot(annees,donnees_aux,label="Auxerre")
plt.legend()
show()