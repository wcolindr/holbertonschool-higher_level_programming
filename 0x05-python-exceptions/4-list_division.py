#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    jeff = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except:
            print("wrong type")
            result = 0
        except:
            print("division by 0")
            result = 0
        except:
            print("out of range")
            result = 0
        finally:
            jeff += [result]
    return jeff
