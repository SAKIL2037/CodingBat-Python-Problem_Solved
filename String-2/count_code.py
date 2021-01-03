def count_code(str):
    temp = 0
    for a in range(97, 123):
        s = 'co' + chr(a) + 'e'
        temp = temp + str.count(s)

    return temp
