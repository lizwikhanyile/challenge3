def sym(a):
    while a and a[0] != a[-1]:
        _, *a, _ = a
        return (a, sum(a))
    
print(sym([1, 2, 3, 4, 5, 6, 3, 9, 7]))