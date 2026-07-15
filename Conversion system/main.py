from base_connversion import *
print("This is system of conversions.\n")
print("1. Binary to decimal.")
print("2. Decimal to binary.\n")
choice = int(input("Enter your choice of conversion: "))

if choice==1:
    bi=int(input("Enter a binary number: "))
    print("The decimal of",bi,"is",binary_to_decimal(bi),".")
elif choice==2:
    dec=int(input("Enter a decimal number: "))
    print("The binary of",dec,"is",decimal_to_binary(dec),".")
else:
    print("you have entered an invalid choice of conversion.")
    print("Please try again")