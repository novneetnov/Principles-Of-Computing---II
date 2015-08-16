def merge(list1, list2):
    answer = []
    while list1:
        if not list2:
            answer.extend(list1)
            return answer
        elem1 = list1[0]
        elem2 = list2[0]
        if elem1 < elem2:
            answer.append(list1.pop(0))
        elif elem2 < elem1:
            answer.append(list2.pop(0))
        else:
            answer.append(list1.pop(0))
            answer.append(list2.pop(0))
    answer.extend(list2)
    return answer


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    if len(list1) <= 1:
        return list(list1)
    else:
        sub_list1 = merge_sort(list1[0:len(list1) / 2])
        sub_list2 = merge_sort(list1[len(list1) / 2:])
        sorted_list = merge(sub_list1, sub_list2)
        return sorted_list


def run_example():
    list1 = [4, 7, 9, 10, 78]
    list2 = [56, 93, 100]
    print "merging -", list1, "and", list2
    print "sorted :", merge(list1, list2)

run_example()