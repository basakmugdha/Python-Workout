#using the splat * operator here
def mysum(*numbers):
    result = 0
    for num in numbers:
        result += num 
    return result

print(mysum(12,89,0,6))
#prefacing the argument list with a * splits it into separate arguments
print(mysum(*[12,89,0,6]))
