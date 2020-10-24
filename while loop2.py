import random
n=random.randint(0,10)
guss=int(input("guess number from 0 to 10:: "))
while True:
    if guss==n:
        print("correct")
        break
    else:
        guss=int(input("guss number:: "))
    


