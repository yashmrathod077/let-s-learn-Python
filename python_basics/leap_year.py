year_num = int(input("Enter a year: "))
if year_num % 4 == 0 :
    if year_num % 100 ==0 :
        if year_num % 400 ==0 :
            print("Leap year")
        else :
            print("Not a leap year")
