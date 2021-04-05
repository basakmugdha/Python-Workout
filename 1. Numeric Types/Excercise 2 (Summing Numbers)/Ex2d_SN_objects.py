def is_int(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False
        
def sum_objects(*numbers):
    result = 0
    for num in numbers:
        if is_int(num):
            result += int(num)
    return result


if __name__ == '__main__':
    print(sum_objects(9,'90','blah',5.8))