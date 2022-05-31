from numpy import size


def hello ():
    print("Hello user!")

def pack (a, b, c):
    return [a, b, c]

def eat_lunch (foods):
    if not len(foods):
        return print("My lunchbox is empty!")
    for i in range(len(foods)):
        if i == 0:
            print("First I eat", foods[i])
        else:
            print("Next I eat", foods[i])

hello()
lunch = pack("apple", "sandwich", "cookie")
print("I have packed your lunch for you. Take it:", lunch)
eat_lunch(lunch)