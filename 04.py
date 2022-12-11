def find_boundaries(any_list):
    list_without_strings = []

    for element in any_list:
        if type(element) == int:
            list_without_strings.append(element)

    if len(list_without_strings) == 0:
        return

    return min(list_without_strings), max(list_without_strings)


print(find_boundaries(["Koń", 2, 3, 4, "Krowa"]))
print(find_boundaries([]))
