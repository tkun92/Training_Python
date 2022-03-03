def is_even(number):
    if number%2==0:
        return True
    else:
        return False

def sum_negatives(list):
    sum = 0
    for item in list:
        if item<0:
            sum+=item
    return sum

def to_minutes(hours):
    return hours*60

def input_number_func():
    input_string = input("adj egy szöveget,gondolom számot")
    return int(input_string)

def annotate_every_even_number(list):
    for i,item in enumerate(list):
        if i%2==0:
            print(item)
        else:
            print(" " + str(item))


input_number = int(input("adj egy számot"))
print(is_even(input_number))
print(sum_negatives([1,54,-13,2,-4,0,-6]))
print(to_minutes(4))
print(input_number_func())
annotate_every_even_number([0,1,2,3,4,5,6,7])
