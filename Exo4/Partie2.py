import csv

def chercherLabel(listePatients, label):
    cpt = 0
    print("Voici la liste des patients de label " + str(label) + "\n")
    for patient in listePatients:
        cpt += 1
        if patient[8] == label:
            print("Patient n°" + str(cpt) + " : " + str(patient))


class Patient: 
    age=0
    genre=1
    yos=0
    cpd=0
    avg_FEV=0
    OX2=0
    Miles=0
    Label=0

    def haveLabel4(self) :
        if self.Label == 4 :
            return True
        else :
            return False
    
Patients = [Patient()]

def getAverageAge() :
    moyenne =0
    total = 0
    j=0
    for patient in Patients :
        if patient.haveLabel4() == True :      
            j=j+1
            total += patient.age

    moyenne = total / j
    print("Age moyen : "+str(int(moyenne))+" ans.")

def getPartMen() :
    homme =0
    total = len(Patients)
    for patient in Patients :
        if patient.genre == 1 :      
            homme = homme +1
    partHomme = (homme*100) / total
    partFemme = 100-int(partHomme)
    print("Pourcentage d'Hommes atteind par le type 4 : "+str(int(partHomme))+"%.")
    print("Pourcentage de Femmes atteind par le type 4 : "+str(int(partFemme))+"%.")

def main():
    # ouverture en lecture du fichier csv
    with open('Exo4/copd_1100_train.csv', 'r') as fichier:
        # on crée un objet reader
        lecture = csv.reader(fichier, delimiter=',')
        # on transforme l'itérateur en liste

        listePatients = list(lecture)
        #Patients = [Patient()]*len(listePatients)
        i=0
        for patient in listePatients : 
            if i == 0 :
                i=i+1
            else : 
                Patients.insert(i, Patient());
                Patients[i].age = int(patient[0])
                Patients[i].genre = int(patient[1])
                Patients[i].yos = patient[2]
                Patients[i].cpd = patient[3]
                Patients[i].avg_FEV = patient[4]
                Patients[i].OX2 = patient[6]
                Patients[i].Miles = patient[7]
                Patients[i].Label = int(patient[8])
                i=i+1
        getAverageAge()
        getPartMen()
        
        chercherLabel(listePatients, "4")

if __name__ == "__main__":
    main()

# test

