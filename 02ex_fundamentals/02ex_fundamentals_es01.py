x = 5

def f(alist):
    x = 5
    new_list = alist.copy()
    for i in range(x):
        new_list.append(i)
    return new_list

alist = [1, 2, 3]
ans = f(alist)
print(ans)
print(alist) # alist has been changed
