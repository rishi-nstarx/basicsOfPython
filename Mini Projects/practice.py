input  = input("Give the random number: ")
input = int(input)

if (input%2 !=0):
    print("Weird")
else:
    if input in range(2,6):
        print("Not Weird")
    elif input in range(6,21):
        print("Weird")
    else:
        print("Not Weird")
