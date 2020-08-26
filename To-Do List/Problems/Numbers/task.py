# put your python code here
def multiply(*numbers):
    for i in range(len(numbers)):
        if i == 0:
            product = numbers[i]
        else:
            product *= numbers[i]
    return product
