lst = [1,2,3,4,5,6]
count = len(lst)
if count % 2 == 0:
    print([lst[:count // 2],lst[count // 2:]])
elif count % 2 == 1:
    print([lst[:count // 2 + 1], lst[count // 2 + 1:]])