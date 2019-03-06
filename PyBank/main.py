import os
import csv
 
budget_csv= "/Users/armando_yaelm/Documents/GitHub/python-challenge/PyBank/budget_data.csv"
total_months = 0
sumatotal=0
total =[]
meses = []
#with open(budget_csv,newline="") as csvfile:
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    csvreaders=next(csvreader)
    #csvreader = csv.reader(csvfile, delimiter = ',',quotechar= ',')
    #csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        #print(row)
        total_months = total_months + 1
        total.append(int(row[1]))
        meses.append(str(row[0]))
print("Analisis Financiero")
print("-------------------")
print("Total de meses = " + str(total_months))

celdamayor=0
celdamenor=0

primervalor= total[1]-total[0]
palpromedio = []
palpromedio.append(int(primervalor))

difmayor= total[1]- total[0]
difmenor= total[1]- total[0]
for x in range(len(total)):
    sumatotal = sumatotal + total[x]
    if (x > 1):
        diferencia = total[x] - total[x-1]
        palpromedio.append(int(diferencia))
        if difmayor<diferencia:
            difmayor=diferencia
            celdamayor = x
        if difmenor>diferencia:
            difmenor=diferencia
            celdamenor = x

sumadediferencias=0
for x in range(len(palpromedio)):
    sumadediferencias= palpromedio[x]+sumadediferencias
cambiopromedio= sumadediferencias/(total_months-1)

print("Total          =" + str(sumatotal))
print("Cambio promedio=" + str(cambiopromedio))
print("Mayor incremento en ganancias = " + meses[celdamayor] + "  (" + str(difmayor) +")")
print("Menor incremento en ganancias = " + meses[celdamenor] + "  (" + str(difmenor) +")")


#archivo de salida
archivosalida="/Users/armando_yaelm/Documents/GitHub/python-challenge/main1.txt"

file = open(archivosalida,"w")

file.write("\n Total          =" + str(sumatotal))
file.write("\n Cambio promedio=" + str(cambiopromedio))
file.write("\n Mayor incremento en ganancias = " + meses[celdamayor] + "  (" + str(difmayor) +")")
file.write("\n Menor incremento en ganancias = " + meses[celdamenor] + "  (" + str(difmenor) +")")

file.close()
