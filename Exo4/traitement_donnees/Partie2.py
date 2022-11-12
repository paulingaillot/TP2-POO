import csv


class Patient:
    age = 0
    genre = 1
    yos = 0
    cpd = 0
    avg_FEV = 0
    FEV=0
    OX2 = 0
    Miles = 0
    Label = 0

    def haveLabel(self, label):
        if self.Label == label:
            return True
        else:
            return False
    
    def __init__ (self, patient):
        self.age = int(patient[0])
        self.genre = int(patient[1])
        self.yos = int(patient[2])
        self.cpd = int(patient[3])
        self.avg_FEV = float(patient[4])
        self.FEV = float(patient[5])
        self.OX2 = float(patient[6])
        self.Miles = float(patient[7])
        self.Label = int(patient[8])
           

    def __str__(self):
        return "[" + str(self.age) + ", " + str(self.genre) + ", "  + str(self.yos) + ", "  + str(self.cpd) + ", "  + str(self.avg_FEV) + ", "  + str(self.FEV) + ", "  + str(self.OX2) + ", "  + str(self.Miles) + ", "  + str(self.Label) + "]"

listePatients = []

def chercherLabel(listePatients, label):
    cpt = 0
    print("Voici la liste des patients de label " + str(label) + "\n")
    for patient in listePatients:
        cpt += 1
        if patient.haveLabel(label):
            print("Patient n°" + str(cpt) + " : " + str(patient))



def getAverageAge():
    moyenne = 0
    total = 0
    j = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            j = j+1
            total += patient.age

    if j > 0:
        moyenne = total / j
        print("Age moyen : "+str(int(moyenne))+" ans.")


def getPartMen():
    homme = 0
    total = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            total = total + 1
            if patient.genre == 1:
                homme = homme + 1
    if total > 0:
        partHomme = (homme*100) / total
        partFemme = 100-int(partHomme)
        print("Pourcentage d'Hommes atteind par le type 4 : "+str(int(partHomme))+"%.")
        print("Pourcentage de Femmes atteind par le type 4 : "+str(int(partFemme))+"%.")

def getProbaType4() :
    label1234 =0
    label4 = 0
    label3 = 0
    label2 = 0
    label1 = 0
    for patient in listePatients:
        if patient.Label != 0 : 
            label1234 = label1234 + 1
            if patient.Label == 1 :
                label1 = label1 +1
            elif patient.Label == 2 :
                label2 = label2 +1
            elif patient.Label == 3 :
                label3 = label3 +1
            elif patient.Label == 4 :
                label4 = label4 +1

    if label1234 > 0:
        proba = round(label1 * 100 / label1234,2)
        print("Probabilité d'avoir la maladie de type 1 : "+str(proba)+"%.")
        proba = round(label2 * 100 / label1234,2)
        print("Probabilité d'avoir la maladie de type 2 : "+str(proba)+"%.")
        proba = round(label3 * 100 / label1234,2)
        print("Probabilité d'avoir la maladie de type 3 : "+str(proba)+"%.")
        proba = round(label4 * 100 / label1234,2)
        print("Probabilité d'avoir la maladie de type 4 : "+str(proba)+"%.")

def compareYOS():
    yos1 = 0
    tot1 = 0
    yos4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            yos4 = yos4 + patient.yos
            tot4 = tot4+1
        elif patient.Label == 0:
            yos1 = yos1 + patient.yos
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(yos1 / tot1,2)
        moy4 = round(yos4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("Yos           |      "+str(moy1)+"     |      "+str(moy4)+"      |   "+value+"   |")

def compareCPD():
    cpd1 = 0
    tot1 = 0
    cpd4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            cpd4 = cpd4 + patient.cpd
            tot4 = tot4+1
        elif patient.Label == 0:
            cpd1 = cpd1 + patient.cpd
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(cpd1 / tot1,2)
        moy4 = round(cpd4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("CPD           |      "+str(moy1)+"      |      "+str(moy4)+"       |   "+value+"   |")


def compareAverageFEV():
    fev1 = 0
    tot1 = 0
    fev4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            fev4 = fev4 + patient.avg_FEV
            tot4 = tot4+1
        elif patient.Label == 0:
            fev1 = fev1 + patient.avg_FEV
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(fev1 / tot1,2)
        moy4 = round(fev4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("Average FEV   |      "+str(moy1)+"      |      "+str(moy4)+"       |    "+value+"    |")


def compareFEV():
    fev1 = 0
    tot1 = 0
    fev4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            fev4 = fev4 + patient.FEV
            tot4 = tot4+1
        elif patient.Label == 0:
            fev1 = fev1 + patient.FEV
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(fev1 / tot1,2)
        moy4 = round(fev4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("FEV           |      "+str(moy1)+"      |      "+str(moy4)+"       |    "+value+"    |")


def compareOX2():
    ox1 = 0
    tot1 = 0
    ox4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            ox4 = ox4 + patient.OX2
            tot4 = tot4+1
        elif patient.Label == 0:
            ox1 = ox1 + patient.OX2
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(ox1 / tot1,2)
        moy4 = round(ox4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("Average OX2   |      "+str(moy1)+"      |      "+str(moy4)+"       |    "+value+"    |")


def compareMiles():
    miles1 = 0
    tot1 = 0
    miles4 = 0
    tot4 = 0
    for patient in listePatients:
        if patient.haveLabel(4) == True:
            miles4 = miles4 + patient.Miles
            tot4 = tot4+1
        elif patient.Label == 0:
            miles1 = miles1 + patient.Miles
            tot1 = tot1 + 1

    if tot1 > 0 & tot4 > 0:
        moy1 = round(miles1 / tot1,2)
        moy4 = round(miles4 / tot4,2)
        value = "correct"
        if moy1 > moy4 :
            value = "lack"
        elif moy1 < moy4 : 
            value = "excess"
        print("Average Miles |      "+str(moy1)+"      |      "+str(moy4)+"       |    "+value+"    |")


def main():
    # ouverture en lecture du fichier csv
    with open('Exo4/traitement_donnees/copd_1100_train.csv', 'r') as fichier:
        # on crée un objet reader
        lecture = csv.reader(fichier, delimiter=',')

        # on transforme l'itérateur en liste
        liste = list(lecture)

        # on crée une liste d'objets Patient
        for i, patient in enumerate(liste):
            if i != 0:
                listePatients.insert(i, Patient(patient))
        
        chercherLabel(listePatients, 4)

        print("\nInformations utiles\n")

        getAverageAge()
        getPartMen()
        getProbaType4()

        print("\nTableau de comapraison\n")
        print("              |   Non-Malade   | Malade Type 4   |    Etat    |")
        compareYOS()
        compareCPD()
        compareFEV()
        compareAverageFEV()
        compareOX2()
        compareMiles()





if __name__ == "__main__":
    main()

# test
