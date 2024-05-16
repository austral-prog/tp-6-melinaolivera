
def remove_elements(list_to_remove_elements):
    if list_to_remove_elements == []:
        return list_to_remove_elements
    del list_to_remove_elements[0]

    if len(list_to_remove_elements) > 3:
        del list_to_remove_elements[3]
    else:
        return list_to_remove_elements

    if len(list_to_remove_elements) > 3:
        del list_to_remove_elements[3]
        return list_to_remove_elements
    else:
        return list_to_remove_elements

list_to_remove_elements = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(remove_elements(list_to_remove_elements))
def add_elements(list_to_add_elements):
    return ["Pink"] + list_to_add_elements + ["Yellow"]

list_to_add_elements = ['Red', 'Green', 'White', 'Black']
print(add_elements(list_to_add_elements))
def is_empty(list_to_check):
    if list_to_check == []:
        return True
    else:
        return False
list_to_check = ['Black', 'Pink', 'Yellow', 'Red', 'Green', 'White']
print(is_empty(list_to_check))

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) > 2 and len(list_to_compare2) > 2:
        if (list_to_compare1[2] == list_to_compare2[2]):
            return True
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    lista1 = list_of_lists_to_modify[0][0:2]
    lista2 = list_of_lists_to_modify[1][1:4]
    lista3 = list_of_lists_to_modify[2][-2:]

    return [lista1, lista2, lista3]
list_of_lists_to_modify = [[1, 2, 3], [4, 5, 6, 7, 8], [9, 10, 11, 12]]
print(list_of_lists(list_of_lists_to_modify))
