# sum should be 36
the_array_3 = [1, 2, 3, "4", None, [6, [False]], "", 5, 7, 8, "33ABC"]

# sum should be 31
evans_array = [2, 4, 6, True, ["8", ""], "Hire Me", 10, None]

# function to sum array
def sum_array(an_array):
    total_nums = 0
    # loop over every element of array
    for item in an_array:
        # if item in array is int, add it to total
        if type(item) == int:
            total_nums += item
        # if item in array is a list, repeat the function to loop over list again
        if type(item) == list:
            total_nums += sum_array(item)
        # if item in array is a str and can be converted to an int, convert and add to total.
        # isnumeric() will only convert if all characters in string are numeric 
        if type(item) == str and item.isnumeric():
            str_to_int = int(item)
            total_nums += str_to_int
        # if item in array is a bool, convert to an int and add to total
        if type(item) == bool:
            bool_to_int = int(item)
            total_nums += bool_to_int
    return total_nums

## I feel like there's a simpler way to do this without as many lines of code
print("Total Sum: ", sum_array(the_array_3))
print("Total Sum: ", sum_array(evans_array))

