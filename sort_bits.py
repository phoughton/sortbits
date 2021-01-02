
# Given an integer array arr, sort the integers in arr in ascending order by the number of 1’s in their binary representation and return the sorted array.
# 
# Examples: 
# $ sortBits([0,1,2,3,4,5,6,7,8])
# $ [0,1,2,4,8,3,5,6,7]


def sort_bits(num_list):
    nums_counted = {}
    miny = 0
    maxy = 0
    for num in num_list:
        if num > maxy:
            maxy = num
        if num < miny:
            miny = num

        ones = (str(bin(num))).count('1')
        if ones in nums_counted:
            nums_counted[ones].append(num)
        else:
            nums_counted[ones] = [num]

    output_list = []
    for key in range(miny, maxy+1):
        if key in nums_counted:
            output_list.extend(nums_counted[key])
    return output_list


assert sort_bits([0,1,2,3,4,5,6,7,8]) == [0,1,2,4,8,3,5,6,7], f"Did not sort correctly, was not:  [0,1,2,4,8,3,5,6,7]"
assert sort_bits([8,7,6,5,4,3,2,1,0]) == [0,8,4,2,1,6,5,3,7], f"Did not sort correctly, was not:  [0,8,4,2,1,6,5,3,7], it was: {sort_bits([8,7,6,5,4,3,2,1,0])}"
assert sort_bits([0,0,1,2,3,4,5,6,7,8]) == [0,0,1,2,4,8,3,5,6,7], f"Did not sort correctly, was not:  [0,0,1,2,4,8,3,5,6,7]"
assert sort_bits([0,1,2,3,4,5,6,7,8, 256, 256]) == [0,1,2,4,8,256,256,3,5,6,7], f"Did not sort correctly, was not: [0,1,2,4,8,256,256,3,5,6,7]"
assert sort_bits([0,1,2,3,4,5,6,7,8, 256, 7]) != [0,1,2,4,8,256,7,3,5,6,7], f"Did not sort correctly, should have failed: [0,1,2,4,8,256,7,3,5,6,7]"
assert sort_bits([]) == [], f"Did not sort correctly, should have been []"
