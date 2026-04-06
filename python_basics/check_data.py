charactor =  input("Enter a character ")
if charactor.isdigit():
    print(" it is a number ")
elif charactor.isupper():
    print(" it is uppercase")
elif charactor.islower():
    print(" it is lowercase")
else :
    print(" its is a special character ")