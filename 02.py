def find_first_and_last(list_or_tuple):
    return tuple([list_or_tuple[0], list_or_tuple[-1]])


a = [1, 2, 3, 4, 0]
b = (4, 2, 2, 1)

print(find_first_and_last(a))
print(find_first_and_last(b))
