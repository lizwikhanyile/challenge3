def fn (a):
    if a[0] == a[-1]:
        return (a, sum(a))
    else:
        return fn(a[1:-1])
    
print(fn([1, 2, 3, 4, 5, 6, 3, 9, 7]))

