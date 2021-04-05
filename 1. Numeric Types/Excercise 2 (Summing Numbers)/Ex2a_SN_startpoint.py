#using default argument here
def mysum(numbers, index=0):
    result =  0
    for num in numbers[index:]:
        result += num 

    return result

#specified index
print(mysum([12,89,0,6],2))
