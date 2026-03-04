def get_todos(filepath = "files/todos.txt"):
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:].capitalize() + "\n"

        todos = get_todos()

        todos.append(todo)

        write_todos("files/todos.txt", todos)

    elif user_action.startswith("show"):
        todos = get_todos()

        for index, item in enumerate(todos):
            items = (f"{index + 1}-{item}").strip("\n")
            print(items)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
    
            todos = get_todos()

            new_todo = input("Enter new todo: ").capitalize() + "\n"
            todos[number] = new_todo

            write_todos("files/todos.txt", todos)

        except ValueError:
            print("Your command is not valid. Enter a number.")

            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()
            
            index = number - 1

            removed_todo = todos[index].strip()

            todos.pop(index)

            write_todos("files/todos.txt", todos)       

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