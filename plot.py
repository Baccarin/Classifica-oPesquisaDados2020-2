import matplotlib.pyplot as plt
import numpy as np

X=np.array([1,2,3,4,5,6,7,8,9,10])

insertion1 = round((0+0+0+0+0)/5)/100
insertion10 = round((0+0+0+0+0)/5)/100
insertion100 = round((0+0+0+0+0)/5)/100
insertion1000 = round((0+0+0+0+0)/5)/100
insertion10000 = round((108+100+94+115+109)/5)/100
insertion50000 = round((1546+1564+1256+1548+1499)/5)/100
insertion100000 = round((6978+7631+7299+7456+7591)/5)/100
insertion150000 = round((7889+7954+8215+8125+7959)/5)/100
insertion250000 = round((2451+2652+2956+3214+3102)/5)/100
insertion500000 = round((31254+32653+33652+36524+37854)/5)/100

insertionY=np.array([insertion1,insertion10,insertion100,insertion1000,insertion10000,insertion50000,insertion100000,insertion150000,insertion250000,insertion500000])

selection1 = round((0+0+0+0+0)/5)/100
selection10 = round((0+0+0+0+0)/5)/100
selection100 = round((0+0+0+0+0)/5)/100
selection1000 = round((1+1+1+1+1)/5)/100
selection10000 = round((134+125+145+128+130)/5)/100
selection50000 = round((3727+3763+3345+3456+3655)/5)/100
selection100000 = round((12600+11526+13465+12546+11546)/5)/100
selection150000 = round((32500+31658+33264+31254+32653)/5)/100
selection250000 = round((8379+82659+84565+84545+83646)/5)/100
selection500000 = round(360000/100)

selectionY=np.array([selection1,selection10,selection100,selection1000,selection10000,selection50000,selection100000,selection150000,selection250000,selection500000])


plt.ylabel('Tempo em segundos')
plt.xlabel('Número de entradas')

plt.plot(X,insertionY,'g--', label='insertion')

plt.plot(X,selectionY,'b--', label='selection')
plt.legend()
plt.show()

