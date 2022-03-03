print("Gondolj egy számra")
min = 1
max = 10
answer = "x"
while answer != "e":
    guess = (min + max)//2
    print("a tippem: ", guess)
    answer = input("k/e/n")
    if answer == "k":
        max = guess - 1