#-----------------Answer to question 2----------------#
def reverse(num_array):
    return num_array[::-1]

def sorted(num_array):
    list_len = len(num_array)
    if list_len <=1:
        return num_array
    else:
        pivot = num_array.pop()
    greater_list = []
    smaller_list = []

    for item in num_array:
        if item>pivot:
            greater_list.append(item)
        else:
            smaller_list.append(item)
    sorted_list = sorted(smaller_list) + [pivot] + sorted(greater_list)
    return sorted_list

if __name__ == "__main__":
    print("Enter numbers separated by space:")
    num_array = num_arr = list(map(int,input().split()))
    ans = sorted(num_array)
    print("Sorted array:",ans,"\n","Reversed array:",reverse(ans))
