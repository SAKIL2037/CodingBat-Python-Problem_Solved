def caught_speeding(speed, is_birthday):
    if is_birthday == True:
        spd = speed - 5
        if spd <= 60:
            return 0
        elif 61 <= spd <= 80:
            return 1
        else:
            return 2

    else:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        else:
            return 2
