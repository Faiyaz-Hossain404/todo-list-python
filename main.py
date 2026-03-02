
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if "add" in user_action:
        todo = user_action[4:] + "\n"

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        todos.append(todo)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)

    elif "show" in user_action:
        file = open("files/todos.txt", "r")
        todos = file.readlines()
        file.close()

        with open("files/todos.txt", "r") as file:
            todos = file.readlines()

        for index, item in enumerate(todos):
            items = (f"{index + 1}-{item}").strip("\n")
            print(items)
    elif "edit" in user_action:
        number = int(user_action[5:])
        number = number - 1
 
        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ").capitalize()
        todos[number] = new_todo

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)
    elif "complete" in user_action:
        number = int(user_action[9:])

        with open("files/todos.txt", 'r') as file:
            todos = file.readlines()
        
        index = number - 1

        removed_removed = todos[index].strip()

        todos.pop(index)

        with open("files/todos.txt", 'w') as file:
            file.writelines(todos)       

        message = f"Todo {removed_removed} was removed from the list"
        print(message)  
    elif "exit" in user_action:
        break
    
    else:
        print("Command not valid")

print("Bye!");