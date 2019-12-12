import matplotlib.pyplot as plt
import numpy as np
import matrixfiller
import shapefilereader
import date_processor
import csv

# dictionary holding the coordinates of the cities, taken from latitude.to
stations = {
    'arad' : (46.18333, 21.31667),
    'bacau' : (46.56667, 26.9),
    'botosani' : (47.75, 26.66667),
    'bucuresti' : (44.43225, 26.10626),
    'buzau' : (45.15, 26.83333),
    'calarasi' : (44.2051, 27.31356),
    'caransebes' : (45.41667, 22.21667),
    'ceahlau_toaca' : (46.955, 25.9457),
    'cluj_napoca' : (46.76667, 23.6),
    'constanta' : (44.18073, 28.63432),
    'deva' : (45.88333, 22.9),
    'drobeta_tr_severin' : (44.63194, 22.65611),
    'galati' : (45.45, 28.05),
    'iasi' : (47.16667, 27.6),
    'miercurea_ciuc' : (46.35, 25.8),
    'ocna_sugatag' : (47.78333, 23.93333),
    'rm_vilcea' : (45.1, 24.36667),
    'rosiorii_de_vede' : (44.11667, 24.98333),
    'sibiu' : (45.792784, 24.152069)
}

cities = []

tempvectors = []
coordvector = []

for station, coordinates in stations.items():
    tempvector = []
    with open('dataset/' + station + '.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        last_date = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
                continue
            if line_count == 1:
                date = int(row[2])
                last_date = date
                temperature = float(row[3].strip())
                tempvector.append((date, temperature))
                continue
            else:
                date = int(row[2].strip())
                temperature = float(row[3].strip())
                while last_date < date:
                    last_date = date_processor.increment_date(last_date)
                    tempvector.append((last_date, temperature))
                line_count += 1
    tempvectors.append(tempvector)
    coordvector.append(coordinates)

first_common_date = max(tempvector[0][0] for tempvector in tempvectors)
indicevector = []
for tempvector in tempvectors:
    for i in range(0, len(tempvector)):
        if tempvector[i][0] == first_common_date:
            indicevector.append(i)
            break

ok = 1
count = 0
while ok:
    z = [[coordvector[i][0], coordvector[i][1], tempvectors[i][indicevector[i] + count][1]] for i in range(0, len(coordvector))]
    print(z)
    count += 1
    z = matrixfiller.matrix_from_array(z, 100, 100)

    plt.imshow(z)
    plt.show()
