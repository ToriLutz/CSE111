x = 42
y = 0 


try:
    print(x/y)
except ZeroDivisionError as e:
    print('not allowed')
else:
    print('oops')
finally:
    print('clean up code')