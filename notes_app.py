import datetime as time
import os

def create_note():
    txtfile = open("notes.txt",'a')
    textfile = {"title" : str() , "body": list() , "creation_time" : str()}
    title_name_input = input("\nenter your new notes title:\n")
    if title_name_input in show_all_notes():
        print("this title exists try another on!\n")
        return
    textfile["title"] = title_name_input
    strinput = str()
    bodyline = 0
    while strinput != "finish body":
        bodyline +=1
        strinput = input(f"\nenter line {bodyline} and if done write finish body\n")
        if strinput != "finish body":
            textfile["body"].append(strinput)
    textfile["creation_time"] = str(time.datetime.now())
    txtfile.write("started title " + textfile["title"]+"\n")
    for i in textfile["body"]:
        txtfile.write(i + "\n")
    txtfile.write(textfile["creation_time"] + "\n")
    txtfile.write(f"finished title {textfile['title']}\n")
    txtfile.close()

def show_all_notes():
    all_notes_titles = list()
    txtfile = open("notes.txt" , 'r')
    for line in txtfile.readlines():
        if line[0:13] == "started title":
            print(line[14:-2])
            all_notes_titles.append(line[14:-2])
    return all_notes_titles
def search_in_notes():
    txtfile = open("notes.txt" , 'r')
    target_title = input("enter the title you want:\n")
    existance = 0
    for line in txtfile.readlines():
        if line[0:13] == "started title":
            if(line[14:]) == target_title+"\n":
                existance = 1
                print("your note:\n")
                print(line[14:])
                continue
        elif existance == 1:
            if line[0:14] == "finished title":
                existance = 2
                break
            else:
                print(line)
    if existance == 0:
        print("subject not found")
    elif existance == 2:
        print("well done!")

        


def delete_note():

    txtfile = open("notes.txt" , 'r')
    target_title = input("enter the title you want to delete:\n")
    existance = 0
    in_and_out_of_note = False
    temptxt = open("temp.txt",'a')
    for line in txtfile.readlines():
        if line[0:13] == "started title":
            in_and_out_of_note = True
            if(line[14:]) == target_title+"\n":
                existance = 1
                continue
            else:
                temptxt.write(line)
                continue
        
        if existance == 1:
            if line[0:14] == "finished title":
                in_and_out_of_note = False
                existance = 2
                continue
            continue
        if in_and_out_of_note:
            temptxt.write(line)
        if line[0:14] == "finished title":
            in_and_out_of_note = False

    txtfile.close()
    temptxt.close()
    if existance == 0:
        print("subject not found")
    elif existance == 2:
        os.replace("temp.txt" , "notes.txt")
        print("well done!")

def exit_program():
    exit()

while True:
    print("enter your actions number:\n1:create new note\n2:show all notes\n3:search notes by title\n4:delete note by title\n5:exit")
    action = input()
    match action:
        case "1":
            create_note()
        case "2":
            show_all_notes()
        case "3":
            search_in_notes()
        case "4":
            delete_note()
        case "5":
            exit_program()
        case _:
            print("wrong input please enter 1-5 for available actions!\n")
