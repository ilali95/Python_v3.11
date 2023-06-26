# def dubl_del(список):
#     return list(set(список))


# my_list = [1, 2, 2, 3, 4, 4, 5]
# new_list = dubl_del(my_list)
# print(new_list)

def find_duplicates(lst):
    return list(set([x for x in lst if lst.count(x) > 1]))

my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1, 4]
duplicates = find_duplicates(my_list)
print(duplicates)
