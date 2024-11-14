# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

T = int(input())

for i in range(T):
    S = input()
    try:
        re.compile(S)
        print("True")    
    except re.error:
        print('False')
"""import sys
import re

lista = []
for line in sys.stdin:
    if(line != ''):
        lista.append(line.rstrip())

for i in range(int(lista[0])):
    try:
        re.compile(lista[i+1])
        is_valid = True
        print('True')
    except re.error:
        is_valid = False
        print('False')
"""