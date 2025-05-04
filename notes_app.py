import datetime as time
txtfile = open("notes.txt","w")
jsonfile = open("notes.json")
def create_note():
    title = input("enter the title of your new note: \n")
    body = input("enter the body of your new note:\n")
    date_of_creation = time.time()
    txtfile.writelines(title + "\n")
    txtfile.writelines(body + "\n")
    #txtfile.writelines(date_of_creation)
def show_all_notes():
    return
def search_in_notes():
    return
def delete_note():
    return
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
