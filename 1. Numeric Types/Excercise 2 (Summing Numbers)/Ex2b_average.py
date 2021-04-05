#using the splat * operator here
def myavg(*numbers):
    result = count = 0
    for num in numbers:
        result += num 
        count += 1
    return result//count

print(myavg(12,89,0,6))
#prefacing the argument list with a * splits it into separate arguments
print(myavg(*[12,89,0,6]))
