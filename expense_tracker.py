m=print("WELCOME DEAR")
category={"a":"food","b":"Transport","c":"shoppig","d":"Education","e":"Entertainment","f":"others"}
type=[]
item=[]
price=[]
while True:
    menue=(input("---Main Menue---\n1. Add Expense\n2. View All Expenses\n3. View Total Expenses\n4. Search Expense\n5. Delete Expense\n6. Exit\nEnter you choice here:"))
    con=1
    if menue=="1":
        while con!=2:
         Expense_category=(input("Expense category\na.Food\nb.Transport\nc.Shopping\nd.Education\ne.Entertainment\nf.Others\nEnter you choice here:"))
         if Expense_category in category:
            collect=category.get(Expense_category)
            type.append(collect)
            diceription=str(input("Expense description="))
            item.append(diceription)
            amount=int(input("Enter Price=Rs"))
            price.append(amount)
            con=int(input("1.Add more Expense\n2.Back to Menue\nEnter your choice here:"))
         elif Expense_category not in category:
             print("---Invalid choice Try again----")
    elif menue=="2":
        print("---View All Expenses---")
        if len(type)==0:
            print("No expenses yet available")
        if len(type)!=0:
            for i in range(len(type)):
                print(i+1,".",type[i],"  ",item[i]," ",price[i])
        con=int(input("1.Back to Menue"))
    elif menue=="3":
       print("---View Total Expenses---")
       if len(price)==0:
            print("Total Expenses=Rs0")
       if len(price)!=0:
           Totalprice=0
           for i in range(len(price)):
               Totalprice=Totalprice+price[i]
           print("Total Expenses=",Totalprice)
       con=int(input("1.Back to Menue"))
    elif menue=="4":
        print("---Search Expense---")
        while con!=2:
            search=input("Enter expense type you want to search=")
            if(type==[]):
                   print("no item found of this type")
            elif(type!=[]):
                for i in range(len(type)):
                   if search==type[i]:
                      print(item[i])
            con=int(input("1.Search again\n2.Back to Menue\nEnter your choice here:"))
    elif menue=="5":
        print("---Delete Expense---")
        while con!=2:
           rem=input("Enter expense type you want to delete=")
           if(type==[]):
                   print("no item found of this type")
           elif(type!=[]):
               print("available items of type",rem,"is")
               for i in range(len(type)):
                   if rem==type[i]:
                      print(i+1,item[i]," ",price[i])
               rem=int(input("Enter Expense no you want to delete="))
               if rem in range(1,len(item)+1):
                   del(item[rem-1])
                   del(type[rem-1])
                   del(price[rem-1])
                   print("Expense remove successfully")
               else:
                   print("invalid idex")
           con=int(input("1.Delete again\n2.Back to Menue\nEnter your choice here:"))
    elif(menue=="6"):
        print("Thanks to use my app")
        break
    else:
        print("Invalid choice. Please try again.")
        
