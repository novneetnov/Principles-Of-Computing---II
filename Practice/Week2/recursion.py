def triangular_sum(num):
    "Base Case"
    if num == 0:
        return 0
    else:
        return triangular_sum(num - 1) + num

#print triangular_sum(10)


def number_of_three(num):
    if num == 0:
        return 0
    else:
        unit_digit = num % 10
        if unit_digit == 3:
            return 1 + number_of_three(num / 10)
        else:
            return number_of_three(num / 10)

#print number_of_three(35354399043063)


def is_member(my_list, elem):
    if not my_list:
        return False
    else:
        last_item = my_list[-1]
        if last_item == elem:
            return True
        return is_member(my_list[:-1], elem)

#print is_member(["a", "4", 5, 76], "4")


def remove_x(my_string):
    if not my_string:
        return my_string
    else:
        last_letter = my_string[-1]
        rest_removed = remove_x(my_string[:-1])
        if last_letter == "x":
            return rest_removed
        else:
            return rest_removed + last_letter

#print remove_x("caxtxxdoxgxxratx")


def insert_x(my_string):
    if len(my_string) <= 1:
        return my_string
    else:
        rest_string = insert_x(my_string[:-1])
        return rest_string + "x" + my_string[-1]

#print insert_x("catdog")


def list_reverse(my_list):
    if len(my_list) <= 1:
        return list(my_list)
    else:
        first_item = my_list[0]
        rest_reverse = list_reverse(my_list[1:])
        rest_reverse.append(first_item)
        return rest_reverse

#print list_reverse([1, 2, 3, 4, 5])


#Following are difficult ones Challenges
def gcd(num1, num2):
    """
    By Euclid's Algorithm
    """
    if num1 == num2:
        return num1
    else:
        if num1 > num2:
            return gcd(num1 - num2, num2)
        else:
            return gcd(num2 - num1, num1)

#print gcd(34, 12)


def slice_1(my_list, first, last):
    if first == 0 and last == len(my_list):
        return my_list
    elif first == 0 and last < len(my_list):
        my_list.pop(len(my_list) - 1)
        return slice_1(my_list, first, last)
    elif first > 0 and last == len(my_list):
        my_list.pop(0)
        return slice_1(my_list, first - 1, last - 1)
    else:
        my_list.pop(0)
        my_list.pop(len(my_list) - 1)
        return slice_1(my_list, first - 1, last - 1)

print slice_1(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2, 5)


def slice_2(my_list, first, last):
    """
    Takes a list my_list and non-negative integer indices
    satisfying 0 <= first <= last <= len(my_list)
    Returns the slice my_list[first : last]
    """
    if my_list == []:
        return []
    else:
        first_elem = my_list.pop(0)
        if first > 0:
            rest_sliced = slice_2(my_list, first - 1, last - 1)
            return rest_sliced
        elif last > 0:
            rest_sliced = slice_2(my_list, 0, last - 1)
            return [first_elem] + rest_sliced
        else:
            return []

print slice_2(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 2, 5)

