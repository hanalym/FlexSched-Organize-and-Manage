
import datetime
from re import match
from traceback import print_exception


requirement_list = {} # Used for acessing each requirement. Keys are the due date, Values are the subject
requirement_note = {} # Used for the tip of the requirement. Keys are the due date, Values are the tips
changelist = {} #Used as a way to change any requirement/due date/note. Keys and Values vary

name = input("Input your name: ") 

print(f"Hello {name}! Welcome to FlexSched")

while True:

    print("Input a number for the function you wish to do.") # Function selection. Uses numbers for input
    print("1. Note Requirements")
    print("2. List Due Requirements")
    print("3. Edit Requirement/Due Date/Note")
    print("4. Remove a Requirement")
    print("5. Update Schedule")
    print("6. View Schedule")
    print("7. End Program")
    choice = int(input())

    if choice == 1: #Input == 1
        print("Input the subject and the type of requirement (e.g.: Science: Project)") 
        subject = input() # Requirement input
        print("Input the due date and time. (mm/dd/yyyy H:M.S; FORMAT SENSITIVE)") 
        due_time = input() #Due date input
        due_time = datetime.datetime.strptime(due_time, "%m/%d/%Y %H:%M.%S") # Converting string to datetime 

        print("Would you like to add a note?") 
        print("1. Yes")
        print("2. No")
        choice = int(input())

        if choice == 1: #Selection for note input. Originally tips, but changed to note. If user chooses 2, tip is automatically N/A
            print("Input a note:")
            note = input()
        else: 
            note = "N/A"

        requirement_list[due_time] = subject #Addition of requirement to dictionary requirement_list
        requirement_note[due_time] = note #Addition of note to requirement note.

        print(f"Requirement: {subject}")
        print(f"Due Date: {due_time}")
        print(f"Note: {note}")

        input("Press Enter to Continue")
       

    elif choice == 2: #Input == 2

        for_counter = 1
        #Iteration for outputting all requirements with due dates and notes
        for date, requirement, note_iteration in zip(requirement_list.keys(), requirement_list.values(), requirement_note.values()): 
            
            date = date.strftime("%m/%d/%Y %H:%M.%S") #Conversion of datetime to string
            print(f"{for_counter}.")
            print(f"Requirement: {requirement}")
            print(f"Due Date: {date}")
            print(f"Note: {note_iteration}")
            for_counter = for_counter + 1

        input('Press "Enter" to continue')
       
      
    elif choice == 3: #Input == 3
        
        print("What do you want to edit?")
        print("1. Requirement")
        print("2. Due Date")
        print("3. Note")
        choice = int(input())

        for_counter = 0
        change_key = "" #Variable used in case 1, 2, and 3 for storing keys.

        match choice:
            case 1: 
                for requirement in requirement_list.values():

                    for_counter = for_counter + 1
                    print(f"{for_counter}. {requirement}")
                    changelist[for_counter] = requirement

                print("Input a number to edit the requirement")
                choice = int(input())

                print(f"Unchanged: {changelist[choice]}")

                for key_reqlist, value_reqlist in zip(requirement_list.keys(), requirement_list.values()):

                    if changelist.get(choice) == value_reqlist:
                        changelist = {} #Clears entire dictionary to leave only one key and value
                        changelist[key_reqlist] = value_reqlist #Turns numerical index to match key of dictionary "requirement_list"
                        change_key = key_reqlist

                print("Input your change with the same format (Subject: Type of Requirement):")
                change = input()


                for value_reqlist in requirement_list.values():

                    if changelist[change_key] == value_reqlist:
                        requirement_list[change_key] = change

                changelist = {} #Clears changelist for future changes

                print(f"Changed Requirement: {requirement_list[change_key]}")

                input('Press "Enter" to continue')


            case 2:
                for due_time, requirement in zip(requirement_list.keys(), requirement_list.values()):
                    for_counter = for_counter + 1
                    print(f"{for_counter}. {requirement}: {due_time}")
                    changelist[for_counter] = due_time

                print("Input a number to edit the due date")
                choice = int(input())

                print(f"Unchanged: {changelist[choice]}")

                for key in requirement_list.keys():
                    if changelist[choice] == key:
                        change_key = key

                print("Input the changed due date (mm/dd/yyyy H:M.S) FORMAT SENSITIVE:")
                change = input()

                change = datetime.datetime.strptime(change, "%m/%d/%Y %H:%M.%S")

                requirement_list[change] = requirement_list.pop(change_key) #Removes old key with new key. Same with next line
                requirement_note[change] = requirement_note.pop(change_key)

                print(f"Changed Due Date On: {requirement_list[change]}")

                input('Press "Enter" to continue')

            case 3: #case 3 is similar to case 1
                for note, requirement in zip(requirement_note.values(), requirement_list.values()):

                    for_counter = for_counter + 1
                    print(f"{for_counter}. {requirement}: {note}")
                    changelist[for_counter] = note

                print("Input a number to edit the note")
                choice = int(input())

                print(f"Unchanged: {changelist[choice]}")

                for key_reqnote, value_reqnote in zip(requirement_note.keys(), requirement_note.values()):

                    if changelist.get(choice) == value_reqnote:
                        changelist = {} 
                        changelist[key_reqnote] = value_reqnote 
                        change_key = key_reqnote

                print("Input your changed note:")
                change = input()


                for value_reqnote in requirement_note.values():

                    if changelist[change_key] == value_reqnote:
                        requirement_note[change_key] = change

                changelist = {} 

                print(f"Changed Note: {requirement_note[change_key]}")

                input('Press "Enter" to continue')


    elif choice == 4: #Input == 4
        print("Feature in the works!")
        input('Press "Enter" to continue')

    elif choice == 5:
        print("Feature in the works!")
        input('Press "Enter" to continue')

    elif choice == 6:
        print("Feature in the works!")
        input('Press "Enter" to continue')

    elif choice == 7:
        break

    else: #Invalid Input Check
        print("Invalid Input")
        input('Press "Enter" to continue')

print(f"Thanks for using, {name}!")
input('Press "Enter" to end the program')


