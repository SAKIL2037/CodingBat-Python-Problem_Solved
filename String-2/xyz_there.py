def xyz_there(str):
    if str.count('xyz') > 0:
        if str.count('.xyz') >= str.count('xyz'):
            return False
        else:
            return True
    else:
        return False
