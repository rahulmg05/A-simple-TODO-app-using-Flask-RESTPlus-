import pprint
todo_collection = [
    {
        "username": "rahulmg05",
        "todos": [
            {
                "description": "Complete writting tutorial notes for Flask-RESTPlus by EOD",
                "name": "Complete Flask RESTPlus"
            },
            {
                "description": "Complete writting your medium blog",
                "name": "Medium Blog"
            }
        ]
    },
    {
        "username": "oldmonk",
        "todos": [
            {
                "description": "Get Groceries by 6 PM today.",
                "name": "Shopping"
            },
            {
                "description": "Search for tyre deals in pep boys and good year",
                "name": "Tyre Deals"
            }
        ]
    },
    {
        "username": "sam1234",
        "todos": [
            {
                "description": "Get a birthday cake for your brother",
                "name": "Cake"
            }
        ]
    }
]


def get_todos():
    global todo_collection
    return todo_collection


def get_users():
    users_list = [user['username'] for user in todo_collection]
    return users_list


def get_todos_user(username):
    todos_user = [user['todos'] for user in todo_collection if user['username'] == username]
    #The above is list comprehension. Now, todos is already a list in the todo_collection, so the above would return a list of lists which is not necessary
    #The todos_user will always have a single element(list) in the list or to put it in simple words, todos_user is a list of lists with a single list. So, we just return todos_user[0]
    return todos_user[0]


def is_user_present(username):
    if username in get_users():
        return True
    else:
        return False


def is_todo_present(username, todoname):
    todos = get_todos_user(username)
    # if todos is empty
    if not todos:
        return False

    if todoname in [t['name'] for t in todos]:
        return True
    else:
        return False


def add_todo(todo):
    print("Adding Todo: {}".format(todo))
    #Check if the user exists
    username = todo['username']
    todos = todo['todos']
    if username not in get_users():
        todo_collection.append(todo)
        return 'Successfully added todos', 0
    else:
        result, err = add_todos_user(username, todos)
        if not err:
            return 'Successfully added todos', 0
        else:
            return "Todos: " + str(result) + " already exist", -1


def add_todos_user(username, todos):
    global todo_collection
    todos_exist = [t['name'] for t in todos if is_todo_present(username, t['name'])]
    if not todos_exist:
        #if none of the todos exist, get the current todos list of the user and merge them with the new list
        todos_current = get_todos_user(username)
        todos_current.extend(todos)

        temp_todo_collecton = [{"username":obj["username"], "todos":todos_current} if obj["username"] == username else obj for obj in todo_collection]
        todo_collection = temp_todo_collecton

        return todos, 0
    else:
        return todos_exist, -1


def update_todo(username, todos):
    global todo_collection
    #check if the user is present
    if is_user_present(username):
        #Check if the todos exist. If they don't exist return error.
        todos_current = get_todos_user(username)
        todos_new = todos

        todos_current_names = [t['name'] for t in todos_current]
        todos_new_names = [t['name'] for t in todos_new]

        todos_not_exist = []
        for t in todos_new_names:
            if t not in todos_current_names:
                todos_not_exist.extend(t)

        #Update
        if not todos_not_exist:
            temp_todo_collecton = [{"username": obj["username"], "todos": todos} if obj["username"] == username else obj for obj in todo_collection]
            todo_collection = temp_todo_collecton
        else:
            return "TODOS: " + str(todos_not_exist) + " donot exist", -1
    else:
        return "User does not exist", -1

    return todos, 0


def delete_todo(username, todos_delete):
    global todo_collection
    todos = get_todos_user(username)
    todos = [t for t in todos if t['name'] not in todos_delete]
    temp_todo_collecton = [{"username": obj["username"], "todos": todos} if obj["username"] == username else obj for obj in todo_collection]
    todo_collection = temp_todo_collecton
    return "Successfully deleted.", 0

