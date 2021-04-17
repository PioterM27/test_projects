"""Create a function that takes a list lst and a number N and returns a list of two integers from lst whose product equals N.

Examples
two_product([1, 2, -1, 4, 5], 20) ➞ [4, 5]

two_product([1, 2, 3, 4, 5], 10) ➞ [2, 5]

two_product([100, 12, 4, 1, 2], 15) ➞ None"""


def two_product(lst, n):
    for i in lst:
        # print(i)
        temp = n / i
        if temp in lst:
            return round(temp),i
        else:
            continue
    return None

def two_product2(lst,n):

    temp=set(map(lambda x:n/x,lst))
    temp2=set(lst) & temp

    return temp2 if len(temp2)!=0 else None

# print(isinstance((39/3),int))

a = two_product2([1, 2, 3, 4, 13, 5], 39)
print(a)  # print(b)
