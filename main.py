import lib

# Hardcoded lists of numbers
list1 = [1, 2, 3, 4, 5]
list2 = [3, 5, 6, 7, 8]
list3 = [3, 5, 9, 10, 11]

my_lists = [list1, list2, list3]  # This is the list of lists

common_count = lib.count_common_elements(my_lists)

if common_count != 0:  # Check for error return
    print("Common elements:", common_count)