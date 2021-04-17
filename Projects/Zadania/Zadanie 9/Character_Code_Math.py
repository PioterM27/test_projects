# b="abc"
# str_nbr=''
# int_nbr=0
# for index in b:
#     str_nbr+=str(ord(index))

def calc(s):
    str_nbr = ''
    str_nbr7to1 = ''
    num1 = 0
    num2 = 0
    for index in s:
        str_nbr += str(ord(index))
        for char in str(ord(index)):
            if (char == '7'):
                num1 += 7
                num2 += 1
            else:
                num1 += int(char)
                num2 += int(char)

    return num1 - num2

    # str_nbr7to1=str_nbr.replace('7','1')


# print(calc('ABCDabcd'))
# list=[23,1001,2,3,4,34,5,6]
# print(list.sort())
# list.pop()
# print(list)
def duplicate_nums(nums):
    new_list = []
    for number in range(0, len(nums)):
        temp = nums.pop()
        if temp in nums:
            new_list.append(temp)
    if len(new_list) == 0:
        return None
    else:
        return sorted(new_list)


print(duplicate_nums([1, 2, 3, 4, 5, 6, 9, 9, 3, 4]))
