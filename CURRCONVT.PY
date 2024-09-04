print("***************************************")
print("*           WELCOME OUR               *")
print("*  INR TO OTHER CURRENCY CONVERTER    *")
print("***************************************")
print("               CREATED BY Nikhil patel ")

# menu options for choose
print("1: Convert INR to USD")
print("3: Convert INR to GBP")
print("2: Convert INR to Euro")
print("4: Convert INR to JPY")
print("5: Exit")

# get input by the User

a=int(input("choose a convert statement in 1st to 5th  :"))

# values of diffrent currencys
USD= 0.012
GBP= 0.011
EURO= 0.0095
JPY= 1.65

# get inr rupee input by the user
Amt=float(input("enter the amount in INR :"))

# apply conditions for diffrent currencys
if(a==1):
    print(f"the {Amt} INR in USD IS {Amt*USD} USD")
elif(a==2):
    print(f"the {Amt} INR in GBP IS {Amt*GBP} GBP")
elif(a==3):
     print(f"the {Amt} INR in EURO IS {Amt*EURO} Euro")
elif(a==4):
     print(f"the {Amt} INR in JYP IS {Amt*JPY} Jyp")
elif(a==5):
    print("exit the prograam run again the program ")
    print("*************************************")
    print("Reset it!!!!!!")
else:
    print("incorrect choosen")

print("\n")
print("***end the program , created by nikhil***")
# end of this program