import csv


def chercherLabel(listePatients, label):
    cpt = 0
    print("Voici la liste des patients de label " + str(label) + "\n")
    for patient in listePatients:
        cpt += 1
        if patient[8] == label:
            print("Patient n°" + str(cpt) + " : " + str(patient))


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

    def haveLabel4(self):
        if self.Label == 4:
            return True
        else:
            return False


Patients = [Patient()]


def getAverageAge():
    moyenne = 0
    total = 0
    j = 0
    for patient in Patients:
        if patient.haveLabel4() == True:
            j = j+1
            total += patient.age

    moyenne = total / j
    print("Age moyen : "+str(int(moyenne))+" ans.")


def getPartMen():
    homme = 0
    total = 0
    for patient in Patients:
        if patient.haveLabel4() == True:
            total = total + 1
            if patient.genre == 1:
                homme = homme + 1
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
    for patient in Patients:
        if patient.Label != 0 : 
            label1234 = label1234 + 1
            if patient.Label == 1 :
                label1 = label1 +1;
            elif patient.Label == 2 :
                label2 = label2 +1;
            elif patient.Label == 3 :
                label3 = label3 +1;
            elif patient.Label == 4 :
                label4 = label4 +1;

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            yos4 = yos4 + patient.yos
            tot4 = tot4+1
        elif patient.Label == 0:
            yos1 = yos1 + patient.yos
            tot1 = tot1 + 1

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            cpd4 = cpd4 + patient.cpd
            tot4 = tot4+1
        elif patient.Label == 0:
            cpd1 = cpd1 + patient.cpd
            tot1 = tot1 + 1

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            fev4 = fev4 + patient.avg_FEV
            tot4 = tot4+1
        elif patient.Label == 0:
            fev1 = fev1 + patient.avg_FEV
            tot1 = tot1 + 1

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            fev4 = fev4 + patient.FEV
            tot4 = tot4+1
        elif patient.Label == 0:
            fev1 = fev1 + patient.FEV
            tot1 = tot1 + 1

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            ox4 = ox4 + patient.OX2
            tot4 = tot4+1
        elif patient.Label == 0:
            ox1 = ox1 + patient.OX2
            tot1 = tot1 + 1

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
    for patient in Patients:
        if patient.haveLabel4() == True:
            miles4 = miles4 + patient.Miles
            tot4 = tot4+1
        elif patient.Label == 0:
            miles1 = miles1 + patient.Miles
            tot1 = tot1 + 1

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
    with open('Exo4/copd_1100_train.csv', 'r') as fichier:
        # on crée un objet reader
        lecture = csv.reader(fichier, delimiter=',')
        # on transforme l'itérateur en liste

        listePatients = list(lecture)
        #Patients = [Patient()]*len(listePatients)
        i = 0
        for patient in listePatients:
            if i == 0:
                i = i+1
            else:
                Patients.insert(i, Patient())
                Patients[i].age = float(patient[0])
                Patients[i].genre = float(patient[1])
                Patients[i].yos = float(patient[2])
                Patients[i].cpd = float(patient[3])
                Patients[i].avg_FEV = float(patient[4])
                Patients[i].FEV = float(patient[5])
                Patients[i].OX2 = float(patient[6])
                Patients[i].Miles = float(patient[7])
                Patients[i].Label = float(patient[8])
                i = i+1

        
        chercherLabel(listePatients, "4")

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
