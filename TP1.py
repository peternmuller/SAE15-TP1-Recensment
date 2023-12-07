import csv

def importation(fichier, separateur):
    liste = []
    with open(fichier, newline='', encoding="UTF-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=separateur)
        for row in reader:
            liste.append(row)
    return liste

donnees_2008 = importation("donnees_2008.csv", ",")
donnees_2016 = importation("donnees_2016.csv", ",")
donnees_2021 = importation("donnees_2021.csv", ";")
metadonnees_communes = importation("metadonnees_communes.csv", ";")

def selec_region(donnees, annee, code_dep, meta, agglo):
    liste = []
    if annee < 2020:
        for ligne in donnees:
            if ligne[2].isdigit() and int(ligne[2]) == code_dep and ligne[6] in agglo:
                liste.append([ligne[6], int(ligne[7]), int(ligne[8]), int(ligne[9])])
    else:
        for ligne in donnees:
            if ligne[1].isdigit() and int(ligne[1]) == code_dep:
                for communes in meta:
                    if ligne[2] == communes[2] and communes[3] in agglo:
                        liste.append([communes[3], int(ligne[3]), int(ligne[4]), int(ligne[5])])
    return liste

agglo_immediate = ["Appoigny", "Auxerre", "Monéteau", "Perrigny", "Saint-Georges-sur-Baulche"]
agglo_total = ["Appoigny", "Augy", "Auxerre", "Bleigny-le-Carreau", "Branches", "Champs-sur-Yonne", "Charbuy", "Chevannes", "Chitry", "Coulanges-la-Vineuse", "Escamps", "Escolives-Sainte-Camille", "Gurgy", "Gy-l'Évêque", "Irancy", "Jussy", "Lindry", "Monéteau", "Montigny-la-Resle", "Perrigny", "Quenne", "Saint-Bris-le-Vineux", "Saint-Georges-sur-Baulche", "Vallan", "Venoy", "Villefargeau", "Villeneuve-Saint-Salves", "Vincelles", "Vincelottes"]

donnees_2008_auxerre = selec_region(donnees_2008, 2008, 89, metadonnees_communes, ["Auxerre"])
donnees_2016_auxerre = selec_region(donnees_2016, 2016, 89, metadonnees_communes, ["Auxerre"])
donnees_2021_auxerre = selec_region(donnees_2021, 2021, 89, metadonnees_communes, ["Auxerre"])

donnees_2008_immediate = selec_region(donnees_2008, 2008, 89, metadonnees_communes, agglo_immediate)
donnees_2016_immediate = selec_region(donnees_2016, 2016, 89, metadonnees_communes, agglo_immediate)
donnees_2021_immediate = selec_region(donnees_2021, 2021, 89, metadonnees_communes, agglo_immediate)

donnees_2008_total = selec_region(donnees_2008, 2008, 89, metadonnees_communes, agglo_total)
donnees_2016_total = selec_region(donnees_2016, 2016, 89, metadonnees_communes, agglo_total)
donnees_2021_total = selec_region(donnees_2021, 2021, 89, metadonnees_communes, agglo_total)