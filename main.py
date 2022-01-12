import numpy as np

arrays = [np.array(list(map(int, line.split()))) for line in open('busy_day.in')]

nRows = arrays[0][0]
nCollumns = arrays[0][1]
nDrones = arrays[0][2]
nTurns = arrays[0][3]
maxload = arrays[0][4]

nProducttypes = arrays[1]
Producttypes = arrays[2]

nWarehouses = int(arrays[3])

stopWarehouse = int(nWarehouses) * 2 + 4
posWarehouse = np.empty((nWarehouses, 2))
count = 0
for i in range(4, stopWarehouse):
    if i % 2 == 0:
        posWarehouse[count] = arrays[i]
        count += 1

nOrders = int(arrays[stopWarehouse])
posOrders = np.empty((nOrders, 2))
stopOrders = nOrders*3 + stopWarehouse
count = 0
relpos = 0
for i in range(stopWarehouse+1, stopOrders+1):
    if relpos % 3 == 0:
        posOrders[count] = arrays[i]
        count += 1
    relpos += 1
