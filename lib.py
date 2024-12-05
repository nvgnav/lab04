def count_common_elements(lists):

    # Input validation: Check if the input is a list of lists
    if not isinstance(lists, list):
        print("Error: Input must be a list of lists.")
        return 0

    if not lists:
        print("Error: Input list cannot be empty.")
        return 0

    for lst in lists:
        if not isinstance(lst, list):
            print("Error: Input must be a list of lists.")
            return 0
        if not all(isinstance(item, (int, float)) for item in lst):
            print("Error: Lists must contain only numbers.")
            return 0

    # Use the first list as a reference set
    common_elements = set(lists[0])

    # Reduce the reference set by intersecting with subsequent lists
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))

    return len(common_elements)


# Example usage (you should replace this with your own code that creates the lists):
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 5, 6, 7, 8]
    list3 = [3, 5, 9, 10, 11]
    list4 = [3, 5]  # Example with a shorter list

    lists_to_check = [list1, list2, list3, list4]

    common_count = count_common_elements(lists_to_check)

    if common_count != 0:
        print("Number of common elements:", common_count)
