import os
import csv
 
 #Leer el archivo:

election_csv= "/Users/armando_yaelm/Documents/GitHub/python-challenge/PyPoll/election_data.csv"
total_votes = 0
candidatos =[]
paises = []
voterid = []
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csvreaders=next(csvreader)
    for row in csvreader:
        total_votes = total_votes + 1
        candidatos.append(str(row[2]))
        paises.append(str(row[1]))
        voterid.append(str(row[0]))

#Contar los votos de cada candidato:

Correy = 0
Khan = 0
Li = 0
Otooley=0

for x in range(len(candidatos)):
    if candidatos[x] == "Correy":
        Correy+=1
    if candidatos[x] == "Khan":
        Khan+=1
    if candidatos[x] == "Li":
        Li+=1
    if candidatos[x] == "O'Tooley":
        Otooley+=1

# Determinar el % de cada candidato

porcentajeCorrey = (Correy / total_votes) * 100
porcentajeKhan = (Khan / total_votes) * 100
porcentajeLi = (Li / total_votes) * 100
porcentajeOtooley = (Otooley / total_votes) * 100

#Determinar el ganador

Ganador = Correy
Nombre= "Correy"
if Ganador < Khan:
    Ganador = Khan
    Nombre = "Khan"
elif Ganador < Li:
    Ganador = Li
    Nomre = "Li"
elif Ganador < Otooley:
    Ganador = Otooley
    Nombre = "O`tooley"

#Imprimir los resultados

print("------------------------------------------")
print("Votos Totales =" + str(total_votes))
print("------------------------------------------")
print("Candidato Khan = "+ str(porcentajeKhan) +"%  " + "Votos de Khan= " + str(Khan))
print("Candidato Correy = "+ str(porcentajeCorrey) +"%  " + "Votos de Correy= " + str(Correy))
print("Candidato Li = "+ str(porcentajeLi) +"%  " + "Votos de Li= " + str(Li))
print("Candidato O'Tooley = "+ str(porcentajeOtooley) +"%  " + "Votos de O'Tooley= " + str(Otooley))
print("------------------------------------------")
print("Y EL GANADOR ES: " + str(Nombre))
print("------------------------------------------")

#archivo de salida
archivosalida="/Users/armando_yaelm/Documents/GitHub/python-challenge/main2.txt"

file = open(archivosalida,"w")

file.write("\n -----------------------------------")
file.write("\n Votos Totales =" + str(total_votes))
file.write("\n -----------------------------------")
file.write("\n Candidato Correy = "+ str(porcentajeCorrey) +"%  " + "Votos de Correy= " + str(Correy))
file.write("\n Candidato Khan = "+ str(porcentajeKhan) +"%  " + "Votos de Khan= " + str(Khan))
file.write("\n Candidato Li = "+ str(porcentajeLi) +"%  " + "Votos de Li= " + str(Li))
file.write("\n Candidato O'Tooley = "+ str(porcentajeOtooley) +"%  " + "Votos de O'Tooley= " + str(Otooley))
file.write("\n -----------------------------------")
file.write("\n Y EL GANADOR ES: " + str(Nombre))
file.close()