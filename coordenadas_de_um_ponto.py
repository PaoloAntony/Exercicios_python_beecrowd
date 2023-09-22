cordx,cordy = map(float,input().split())

if cordx > 0 and cordy > 0:
    print("Q1")
elif cordx >0 and cordy < 0:
    print("Q4")
elif cordx < 0 and cordy > 0:
    print("Q2")
elif cordx < 0 and cordy < 0:
    print("Q3")
elif cordx == 0 and cordy > 0:
    print("Eixo Y")
elif cordx > 0 and cordy == 0:
    print("Eixo X")
else: print("Origem")
