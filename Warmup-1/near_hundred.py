def near_hundred(n):
    if n <= 110:
        temp1 = abs(n - 100)
        if temp1 <= 10:
            return True
        else:
            return False

    elif n <= 210:
        temp2 = abs(n - 200)
        if temp2 <= 10:
            return True
        else:
            return False

    else:
        return False

