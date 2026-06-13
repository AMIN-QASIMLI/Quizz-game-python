import json, random

"""Necessary Files"""
qs_file=open("questions.json","r",encoding="utf-8")
qs=json.load(qs_file)
h_file=open("history.json","r",encoding="utf-8")
h=json.load(h_file)
lb_file=open("leaderboard.json","r",encoding="utf-8")
lb=json.load(lb_file)

"""Global Variables"""
correct=0
false=0
percentage=0

name="Player"

"""Function For Changing Name"""
def change_name():
    global name
    name=input(f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCurrent name: {name}\n\n\n\n\nNew name: ")
    main()

"""Function For Displaying Stats"""
def stats():
    global percentage
    percentage=correct/10*100
    input(f"\n\n\n\n\n\n\n\nPlayer {name}\n\n\n\nCorrects: {correct}\n\n\nFalses: {false}\n\n\nSuccess Percentage: {percentage}%\n\n\n\n\nPress any key to continue....")
    h.append({"name":name,"corrects":correct,"falses":false,"success_percentage":percentage})
    with open("history.json","w",encoding="utf-8") as h_file:
        json.dump(h, h_file)
    main()

"""Function For Displaying Leaderboard"""
def leaderboard():
    new=sorted(h,key=lambda x:x["success_percentage"], reverse=True)
    with open("leaderboard.json","w",encoding="utf-8") as lb_file:
        json.dump(new,lb_file)
    try:
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        place=1
        for p in lb:
            print(f"\n====================================== {place} ======================================\n")
            print(f"Name: {p["name"]}\nSucces Percentage: {p["success_percentage"]}")
            place+=1
        input("\n\n\n\n\n\n\n\nPress any key to continue")
    except SyntaxError:
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFile is unaviable...\n\n\nPress enter for backing the menu\n\n\n\n\n\n\n\n\n")
    main()

"""Function For Displaying Game Hstory"""
def history():
    try:
        print("\n\n\n\n\n\n\n\n\n\n\n\n")
        game=1
        for g in h:
            print(f"\n======================================Game {game}======================================\n")
            print(f"Name: {g["name"]}\nCorrects: {g["corrects"]}\nFalses: {g["falses"]}\nSucces Percentage: {g["success_percentage"]}")
            game+=1
        input("\n\n\n\n\n\n\n\nPress any key to continue")
    except SyntaxError:
        input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nFile is unaviable...\n\n\nPress enter for backing the menu\n\n\n\n\n\n\n\n\n")
    main()

"""Function For Displaying Question"""
def display_question(v_a,v_b,v_c,v_d,q,ans):
    global correct,false
    print(f"\n\n\n\n\n\n\n\n\n\n\n\n\n======================================Question {len(qs_id)}======================================\n")
    print(q)
    print("\n\n\n\n")
    slc_ans=input(f"1.{v_a}          2.{v_b}\n\n3.{v_c}          4.{v_d}\n\nSelect an answer: ")
    if (slc_ans=="1" and v_a==ans)or(slc_ans=="2" and v_b==ans)or(slc_ans=="3" and v_c==ans)or(slc_ans=="4" and v_d==ans):
        correct+=1
        input("\n\n\n\n\n\n\n\n\n\n\nCorrect\n\n\n\n\n\nPress any key to continue...\n\n\n\n\n\n")
        quizz()
    else:
        false+=1
        input("\n\n\n\n\n\n\n\n\n\n\nFalse!\n\n\n\n\n\nPress any key to continue...\n\n\n\n\n\n")
        quizz()

"""Function For Generating Question"""
def quizz():
    global qs_id
    if len(qs_id)==10:
        stats()
        return
    q_id=random.randint(0,19)
    if q_id in qs_id:quizz()
    else:
        qs_id.append(q_id)
        q=qs[q_id]["question"]
        options=qs[q_id]["options"]
        ans=qs[q_id]["correct_answer"]
        va_id=random.randint(0,3)
        v_a=options[va_id]
        options.pop(va_id)
        vb_id=random.randint(0,2)
        v_b=options[vb_id]
        options.pop(vb_id)
        vc_id=random.randint(0,1)
        v_c=options[vc_id]
        options.pop(vc_id)
        v_d=options[0]
        display_question(v_a,v_b,v_c,v_d,q,ans)

"""Function For Genereting Quizz"""
def start_quizz():
    global qs_id
    qs_id=[]
    quizz()

"""Function For Displaying Menu"""
def options():
    opt=input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n1.Start Quizz\n2.Leaderboard\n3.History\n4.Change Name\n0.Exit\n\nSelect an option: ")
    if opt=="1":start_quizz()
    elif opt=="2":leaderboard()
    elif opt=="3":history()
    elif opt=="4":change_name()
    elif opt=="0":
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nExiting...")
        exit(0)
    else:
        print("Write a valid option!")
        main()

"""Main Function"""
def main():
    options()

"""Running Code"""
main()
