
while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ").capitalize() + "\n"

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)

        case "show" | "display":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            with open("files/todos.txt", "r") as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                items = (f"{index + 1}-{item}").strip("\n")
                print(items)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()

            new_todo = input("Enter new todo: ").capitalize()
            todos[number] = new_todo

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            
            index = number - 1

            removed_removed = todos[index].strip()

            todos.pop(index)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)       

            message = f"Todo {removed_removed} was removed from the list"
            print(message)  
        case "exit":
            break

print("Bye!");