#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        value = 0
        try:
            value1 = my_list_1[i]
            value2 = my_list_2[i]
            value = value1 / value2
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        except IndexError:
            print("out of range")
            value = 0
        except TypeError:
            print("wrong type")
            value = 0
        finally:
            result.append(value)
    return result
