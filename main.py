
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

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)
        case "complete":
            number = int(input("Number of the todo to complete: "))

            with open("files/todos.txt", 'r') as file:
                todos = file.readlines()
            
            todos.pop(number - 1)

            with open("files/todos.txt", 'w') as file:
                file.writelines(todos)            
        case "exit":
            break

print("Bye!");