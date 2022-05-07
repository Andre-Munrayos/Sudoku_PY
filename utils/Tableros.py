from dokusan import generators
import numpy as np
from pip import main
class Levels:
    def generateLevel():
        a=np.array(list(str(generators.random_sudoku(avg_rank=150))))
        s= a[0:9]
        s2=a[9:18]
        s3=a[18:27]
        s4=a[27:36]
        s5=a[36:45]
        s6=a[45:54]
        s7=a[54:63]
        s8=a[63:72]
        s9=a[72:81]
        
        row1 = ([int(x) for x in s])
        row2 = ([int(x) for x in s2])
        row3 = ([int(x) for x in s3])
        row4 = ([int(x) for x in s4])
        row5 = ([int(x) for x in s5])
        row6 = ([int(x) for x in s6])
        row7 = ([int(x) for x in s7])
        row8 = ([int(x) for x in s8])
        row9 = ([int(x) for x in s9])

        return row1, row2, row3, row4, row5, row6, row7, row8, row9



 
