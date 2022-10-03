
# Крестики нолики.

from krestil_nolik import ResultKN
from os import system

A = ['-', '-', '-']
B = ['-', '-', '-']
C = ['-', '-', '-']

for i in range(0, 4):
    first = int(input('Введите место, куда хотете поставить Х '))
    system("cls")
    for i in range(0,3):
        if first==(i+1) and (A[i] != ('O')) and (A[i] != ('X')):
            A[i]='X'
            ResultKN(A,B,C)
        
    for j in range(0,3):
        if first==(j+4) and (B[j] != ('O')) and (B[j] != ('X')):
            B[j]='X'
            ResultKN(A,B,C)
                
    for k in range(0,3):
        if first==(k+7) and (C[k] != ('O')) and (C[k] != ('X')):
            C[k]='X'
            ResultKN(A,B,C)

    second = int(input('Введите место, куда хотите поставить О '))
    system("cls")
    for i in range(0,3):
        if second==(i+1) and (A[i] != ('O')) and (A[i] != ('X')):
            A[i]='O'
            ResultKN(A,B,C)
    
    for j in range(0,3):
        if second==(j+4) and (B[j] != ('O')) and (B[j] != ('X')):
            B[j]='O'
            ResultKN(A,B,C)
            
    for k in range(0,3):
        if second==(k+7) and (C[k] != ('O')) and (C[k] != ('X')):
            C[k]='O'
            ResultKN(A,B,C)