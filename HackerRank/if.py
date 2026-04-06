num = int(input(" enter a number "))
if num % 2==0 :
    print("Weird")
elif num in range(2,6):
    print("Not Weird")
elif num in range(6,20):
    print("Weird")