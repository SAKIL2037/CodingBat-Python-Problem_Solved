def parrot_trouble(talking, hour):
    if talking == True and (0 <= hour < 7 or 23 >= hour > 20):
        return True

    else:
        return False
