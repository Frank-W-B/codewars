

def two_sort(array):
    return "***".join(sorted(array)[0]) 

if __name__ == '__main__':
    #Test.assert_equals(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')
    array = ["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]
    sorted_arr = sorted(array)
    first = sorted_arr[0]
    return_str = "***".join(first)
    print(two_sort(array))
