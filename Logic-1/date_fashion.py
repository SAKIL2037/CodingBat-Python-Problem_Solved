def date_fashion(you, date):
    sm = 0
    bg = 0
    if you > date:
        bg = you
        sm = date
    else:
        bg = date
        sm = you

    if sm <= 2:
        return 0
    elif bg <= 2:
        return 0
    elif bg >= 8:
        return 2
    else:
        return 1
