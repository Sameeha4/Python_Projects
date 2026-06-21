import random
import string
m=str(input("Welcome this page give suggestions to generate randon password.\nDo you wants to generate password?\na.YEA\nb.NO\nEnter your option here:"))
if m=="a":
 while m!="b":
    sug=input("whats your choice:\na.craete your own password\nb.get suggestion\nEnter your option here:")
    if sug=="a" or sug=="b":
        no=int(input("How many characters you want in your password:"))
        if sug=="a":
            u=input("Enter you password here:")
            if len(u)!=no:
                print("invalid password")
            elif(len(u)==no):
                if len(u) in range(1,3):
                    print("Password type:---weak---")
                elif len(u) in range(3,12):
                    print("Password type:---medium---")
                elif len(u)>=12:
                    print("Password type:---strong---")
                print("your password---",u,"---is accepted")
        elif sug=="b":
            g1=string.ascii_letters
            g2=string.punctuation
            g3=string.digits
            g4=g1+g2+g3
            P1=random.choices(g4,k=no)
            P2="".join(P1)
            print("Suggested password is:",P2)
        m=input("a.Generate another password\nb.Exit\nEnter your option here:")
    elif(sug!="a" and sug!="b"):
        print("---choose valid option---")
 print("THAKS FOR USING MY APP")
elif(m=="b"):
    print("Please use this page again when needed")
elif(m!="a" and m!="b"):
    print("choose valid option")