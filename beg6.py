b = int(input())
if (b%4==0):
    if (b%100==0):
        if (b%400==0):
            print("yes")
        else:
            print("no")
    else:
        print("yes")
else:
    print("no")
