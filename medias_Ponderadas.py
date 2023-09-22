
laco = int(input())
for vezes in range(laco):
    val1,val2,val3 = map(float,input().split())
    mediapond = ((val1 * 2) + (val2 * 3) + (val3 * 5)) / 10
    print("%.1f"%mediapond)