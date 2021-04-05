#using the splat * operator here
def myavg(*numbers):
    """returns average of numbers supplied"""
    result = count = 0
    for num in numbers:
        result += num
        count += 1
    return result//count

def string_summary(l):
    len_list = [len(x) for x in l]
    return(min(len_list), max(len_list), myavg(*len_list))

if __name__=='__main__':
    word_list = input("Enter a sentence : ").split()
    print(f'Lengths (Shortest, Longest, Average) : {string_summary(word_list)}')
