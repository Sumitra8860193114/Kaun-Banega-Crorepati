Questions=[["Which language was used to create fb?","Python","French","JavaScrip","Php",4],
           ["type of Programming does Python support?","Wick van Rossum","Rasmus Lerdorf","Guido van Rossum","Niene Stom",3],
           ["Which type of Programming does Python support?","object-oriented programming","structured programming","functional programming","all of the mentioned",4],
           ["Is Python case sensitive when dealing with identifiers?","no","yes","machine dependent","none of the mentioned",2],
           ["Which of the following is the correct extension of the Python file?",".python",".pl",".py",".p",3],
           ["Is Python code compiled or interpreted?","Python code is both compiled and interpreted","Python code is neither compiled nor interpreted","Python code is only compiled","Python code is only interpreted",1],
           ["What is the maximum possible length of an identifier?",16,32,64,"None of these above",4],
           ["Who developed the Python language?","Zim Den","Guido van Rossum","Niene Stom","Wick van Rossum",2],
           ["In which year was the Python language developed??",1995,1972,1981,1989,4],
           ["In which language is Python written?","English","PHP","C","All of the above",3],
           ["In which year was the Python 3.0 version developed?",2008,2000,2010,2005,1],
           ["What do we use to define a block of code in Python language?","Key","Brackets","Indentation","None of these",3],
           ["Which character is used in Python to make a single line comment?","/","//","#","!",3],
           ["What is the method inside the class in python language?","Object","Function","Attribute","Argument",2],
           ["Which of the following declarations is incorrect?","_x = 2","__x = 3","__xyz__ = 5","None of these",4],
           ["Which of the following is not a keyword in Python language?","val","raise","try","with",1]
           ]
Levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]

Money=0

for i in range(0,len(Questions)):
    Question=Questions[i]
    print(f"\n\n\nQuestion for Rs. {Levels[i]}")
    print(f"Question {i+1} = {Question[0]}")
    print(f"a . {Question[1]}          b. {Question[2]}")
    print(f"c . {Question[3]}          d. {Question[4]}")

    Reply=int(input("Enter your Answer (1-4) or 0 to quit:\n"))
    
    if (Reply==0):
        Money=Levels[-1]
        break
    if (Reply == Question[-1]):
        print(f"correct Answer, you have won Rs. {Levels[i]}")
        if (i==4):
            Money=10000
        elif (i==9):
            Money=320000
        elif (i==14):
            Money=5000000
        elif (i==15):
            Money=10000000
        elif (i==16):
            Money=70000000
    else:
        print("Wrong Answer!")
        break

print(f"Your take  home money if {Money}")