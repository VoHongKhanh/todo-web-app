import os.path
import time

missionCompletedFile = "missionCompleted.txt"
todos = []
mission_completed = []

now_time = time.strftime("%b %d, %Y %H:%M:%S")

def read_data(data_file_name = "todos.txt"):
    if os.path.exists(data_file_name):
        with open(data_file_name, "r") as data_file:
            td = [item.strip("\n") for item in data_file.readlines()]
            return td
    else:
        return []


def write_data(td, data_file_name = "todos.txt"):
    with open(data_file_name, "w") as data_file:
        data_file.write("\n".join(td))


def print_data(message, t, td):
    if len(td) > 0:
        print(message)
        for idx, item in enumerate(td):
            print(f"{idx + 1}. {item}")
    elif t == "todo":
        print("The todo list is empty!")


def show_todo():
    print_data("Todo list:", "todo", todos)
    print_data("Mission completed:", "completed", mission_completed)


def get_order(message, min_value, max_value, error_message):
    while True:
        try:
            value = int(input(message))
            if value < min_value or max_value < value:
                print(error_message)
                continue
            return value
        except ValueError:
            print(error_message)


def normalize_todo(td):
    td = td.strip()
    return td[0].upper() + td[1:]


def init(folder=""):
    global todos, mission_completed, now_time
    print(f"It is {now_time}")
    todos = read_data((folder + "/" if folder != "" else "") + "todos.txt")
    mission_completed = read_data((folder + "/" if folder != "" else "") + missionCompletedFile)


if __name__ == "__main__":
    print(f"It is {now_time}")
    print("Hi, this is a library of Todo application")
    init("..")
    show_todo()