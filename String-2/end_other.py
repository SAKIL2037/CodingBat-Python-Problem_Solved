def end_other(a, b):
    x = a.lower()
    y = b.lower()

    if x[-3:-1] == y[-3:-1]:
        return True
    elif x[-2:-1] == y[-2:-1]:
        return True
    elif x[-1] == y[-1] and len(x) == 1:
        return True
    else:
        return False
