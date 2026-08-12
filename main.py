#Write a program to understand how the value error exception works?
try:
    num=int(input("Enter number: "))
except Exception as e:
    print(f"There was an error {e} ")

