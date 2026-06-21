m=input("Welcome to the Quizz App\na.Start\nb.Exit\nEnter you option here:")
if(m!="a" and m!="b"):
  print("choose valid option try again")
  m=input("a.Start\nb.Exit\nPlease select valid option to contniou:")
while m=="a":
    Totalscore=0
    q1=("What is python?\na.programing language\nb.human frindly language.\nc.theaorm.\nd.both a and c")
    q2=("Every non empty string in python is?\na.TRUR\nb.FALSE\nc.Empty\nd.Zero")
    q3=("2%2=\na.1\nb.1.0\nc.0.1\nd.0")
    questions=[q1,q2,q3]
    options=["d","a","d"]
    print("----This quiz contains",len(questions),"Questions----")
    for i in range(len(questions)):
            print(i+1,":",questions[i])
            questions[i]=input("Enter your option here:")
            if questions[i]==options[i]:
                  print("---correct---")
                  Totalscore+=1
            elif(questions[i]!="a"and questions[i]!="b"and questions[i]!="c"and questions[i]!="d"):
                while(questions[i]!="a"and questions[i]!="b"and questions[i]!="c"and questions[i]!="d"):
                  print("---invalid choice---")
                  questions[i]=input("Please chosse valid option:")
                  if questions[i]==options[i]:
                   print("---correct---")
                  Totalscore+=1
            elif(questions[i]!=options[i]):
                  print("---wrong---\n---correct option is","",options[i],"---")
    print("Total_score=",Totalscore)
    per_age=Totalscore/(len(questions))*100
    if 0<per_age<50:
        print("Percentage=",per_age,"%...fail...need improvement")
    elif 50<=per_age<=70:
          print("Percentage=",per_age,"%...Pass...average")
    elif 70<per_age<=89:
          print("Percentage=",per_age,"%...Pass...good")
    elif per_age in range(90,101):
          print("Percentage=",per_age,"%...Pass...excellent")
    m=input("a.Re_atempt\nb.Exit\nEnter you choice here:")
if m=="b":
  print("Thanks to use my app")

