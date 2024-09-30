def get_average():
    with open(r"C:\Users\kotla\Desktop\Coding\python-megacourse\001 - todo app\files\data.txt", "r") as file:
        data = file.readlines()
    values = [float(i) for i in data]
    return sum(values) / len(values)


print(get_average())