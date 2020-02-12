### START FUNCTION
def square_odd(pylist):
    odds_squared = [ x**2 for x in pylist if x % 2 == 1]
    return odds_squared
### END FUNCTION
print(square_odd([100, 200, 300, -2]))