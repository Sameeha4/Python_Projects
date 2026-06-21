message=int(input("PLease select Option.\nDo you want to perform some calculations:\n1.YES\n2.NO\nEnter option number here:"))
if message==1:
    print("------WELCOME DEAR----------")
    while message!=2:
     n1=float(input("Enter 1st no="))
     n2=float(input("Enter 2nd no="))
     option=int(input("Which operation you like to per form?\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\nEnter option number here:"))
     if option==1:
         add=n1+n2
         print(n1,"+",n2,"=",add)
     elif option==2:
         sub=n1-n2
         print(n1,"-",n2,"=",sub)
     elif option==3:
         mul=n1*n2
         print(n1,"*",n2,"=",mul)
     elif option==4:
         if n2==0:
            print("ERROR")
         else:
            div=n1/n2
            print(n1,"/",n2,"=",div)
     elif(option>4 or option<=0):
         print("----CHOOSE INVALID OPTION------")
     message=int(input("Do you want to perform some calculations again:\n1.YES\n2.NO\nEnter option number here:"))
    print("THANK YOU FOR USING MY APP") 
elif(message==2):
     print("------AS YOU WISH-------") 
elif(message<=0 or message>2 ):
     print("-----CHOOSE CORRECT OPTION------")
