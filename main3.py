list1 = [2, 5, 6, 7, 1, 7]


def remove_all_after(list_, border_element_):
    new_list = []
    if len(list_) == 0:
        return list_
    elif list_.count(border_element_) == 0:
        return list_
    else:
        for i in list_:
            new_list.append(i)
            if i == border_element_:
                return new_list


print(remove_all_after(list1, 6))
