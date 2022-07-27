#import numpy as np

table = [[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,0,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

def melyik_negyzet(sor,o):
    negyzet1 = []
    negyzet2 = []
    negyzet3 = []
    negyzet4 = []
    negyzet5 = []
    negyzet6 = []
    negyzet7 = []
    negyzet8 = []
    negyzet9 = []
    for i in range(0,9):
        for j in range(0,9):
            if i < 3 and j < 3:
                negyzet1.append(table[i][j])
            elif i < 3 and j < 6:
                negyzet2.append(table[i][j])
            elif i < 3 and j < 9:
                negyzet3.append(table[i][j])
            elif i < 6 and j < 3:
                negyzet4.append(table[i][j])
            elif i < 6 and j < 6:
                negyzet5.append(table[i][j])
            elif i < 6 and j < 9:
                negyzet6.append(table[i][j])
            elif i < 9 and j < 3:
                negyzet7.append(table[i][j])
            elif i < 9 and j < 6:
                negyzet8.append(table[i][j])
            else:
                negyzet9.append(table[i][j])
    if sor < 3 and o < 3:
        return negyzet1
    elif sor < 3 and o < 6:
        return negyzet2
    elif sor < 3 and o < 9:
        return negyzet3
    elif sor < 6 and o < 3:
        return negyzet4
    elif sor < 6 and o < 6:
        return negyzet5
    elif sor < 6 and o < 9:
        return negyzet6
    elif sor < 9 and o < 3:
        return negyzet7
    elif sor < 9 and o < 6:
        return negyzet8
    elif sor < 9 and o < 9:
        return negyzet9

def lehetseges(y,x,n):
    global table
    for i in range(0,9):
        if table[i][x] == n:
            return False
    for j in range(0,9):
        if table[y][j] == n:
            return False
    
    for sor in melyik_negyzet(y,x):
        if sor == n:
            return False
    
    return True

def megoldas():
    global table
    for i in range(9):
        for j in range(9):
            if table[i][j] == 0:
                for n in range(1,10):
                    if lehetseges(i,j,n):
                        table[i][j] = n
                        megoldas()
                        table[i][j] = 0
                        
                return
    #ha több megoldás van elválasztva legyenek
    for i in range(len(table)):
        if i % 9 == 0:
            print('---------------------------')
            print(table[i])
        else:
            print(table[i])

megoldas()  
