def FizzBuzz(first, last):
    list = []
    
    for i in range(first, last + 1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("fizzbuzz")
        elif i % 3 == 0:
            list.append("fizz")
        elif i % 5 == 0:
            list.append("buzz")
        else:
            list.append(i)

    return list