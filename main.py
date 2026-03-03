
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            items = (f"{index + 1}-{item}").strip("\n")
            print(items)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
    
            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ").capitalize() + "\n"
            todos[number] = new_todo

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid. Enter a number.")

            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            
            index = number - 1

            removed_todo = todos[index].strip()

            todos.pop(index)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)       

            message = f"Todo {removed_todo} was removed from the list"
            print(message)
        
        except ValueError:
            print("Your command is not valid. Enter a number.")
            continue

        except IndexError:
            print("Todo number doesn't exist.")
            continue

    elif user_action.startswith("exit"):
        break
    
    else:
        print("Command not valid")

print("Bye!")