for i in range(0,5):
    print("hello world")

name = input("add meg a nevedet")
repeat = int(input("mennyiszer szeretnéd látni a nevedet"))

for i in range(repeat):
    print(str(i+1) + ". " + name)