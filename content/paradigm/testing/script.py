def soma_cinco(number=0):
    try:
        if number == None:
            return 'Please enter number'
        return int(number)+5
    except ValueError as error:
        return error
    except TypeError as erro:
        return error
