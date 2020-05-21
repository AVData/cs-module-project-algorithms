'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(nums):
    # Your code here
    # arr.sort()
    # print(arr)
    # for k, v in enumerate(arr):
    #     if arr[k] == True:
    #         continue
    #     elif arr[k + 1] == v:
    #         print(v, arr[k])
    #     else:
    #         print(arr[k])

    #
    # first-pass solution
    # we'll keep an array, call it `no_dups` to hold numbers we see in the nums
    # array
    no_dups = []
    # iterate through nums
    # using an array to hold the dups and then searching through it
    # one thing that arrays are not great are is searching for a particular
    # value in the worst case, that's going to be O(n)
    # what are other data structures that better suited to being searched?
    for x in nums:  # O(n)
        # check to see if the number is already in the `no_dups` array
        if x not in no_dups:  # O(n)
            no_dups.append(x)
        # if it is, remove it from the `no_dups` array
        else:
            no_dups.remove(x)  # O(n)
    # when we're done iterating, the only number in our `no_dups` array is the
    # odd number out
    # return it
    return no_dups[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
