import json, random,time

qs=open("questions.json", "r")
qs=json.load(qs)
h=open("history.json", "r")
h=json.load(h)

def history():
    try:
        pass
    except FileNotFoundError,SyntaxError:print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFile is unaviable...\n\n\nPress enter for backing the menu"),input(),main()

def quizz():
    q=random.randint(1,21)

def start_quizz():
    quizz()

def options():
    opt=input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1.Start Quizz\n2.History\n0.Exit\n\nSelect an option: ")
    if opt=="1":start_quizz()
    elif opt=="2":history()
    elif opt=="0":
        print("Exiting...")
        exit(0)
    else:
        print("Write a valid option!")
        main()

def main():
    options()

main()
