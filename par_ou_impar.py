num_casos = int(input())

for casos in range(num_casos):
    caso = int(input())
    if caso == 0 :
        print("NULL")
    if caso > 0 and caso % 2 == 0:
        print("EVEN POSITIVE")
    if caso > 0 and caso % 2 != 0: 
        print("ODD POSITIVE")
    if caso < 0 and caso % 2 != 0:
        print("ODD NEGATIVE")
    if caso < 0 and caso % 2 == 0:
        print("EVEN NEGATIVE")
