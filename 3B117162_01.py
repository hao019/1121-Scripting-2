s = int(input("請輸入最長的星星數量："))
a = int((s+1)/2)
b = a

for row in range(1, s+1):
    for col in range(1, s+1):
        if a <= col <= b:
            print("*", end="")
        else:
            print(" ", end="")

    if row < (s+1)/2:
        a -= 1
        b += 1
    else:
        a += 1
        b -= 1

    print()
 