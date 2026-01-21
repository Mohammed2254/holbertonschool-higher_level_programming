#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)  # نضيف البديل
        else:
            new_list.append(item)  # نضيف العنصر الأصلي
    return new_list
