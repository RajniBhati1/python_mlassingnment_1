def count(list1, element):
    count = 0
    for x in list1:
        if x == element:
            count += 1
    return count
list1 = [4,6,7,8,9,4,5]
element = 4
print(count(list1, element))