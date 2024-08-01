

'''
    try:
    except:
    else:
    finally:

'''

def demo_fn():
    num1 = 100
    num2 = 'a'
    # num2 = 10
    result = 0
    try:
        result = num1/num2
    except ZeroDivisionError as zd:
        print(zd)
        return 'Incorrect division'
    except TypeError as te:
        print(te)
        return 'Incorrect data type'
    else:
        print('No exception thrown')
    finally:
        print('End of function')
    # except Exception as ex:
    #     print(ex)

    return result

# print(demo_fn())


def dem_fn(num1,num2):

    try:
        if(num2 == 0):
            raise ZeroDivisionError("Number2 is 0")
        print(num1/num2)
    except ZeroDivisionError as zde:
        print(zde)

dem_fn(10,0)