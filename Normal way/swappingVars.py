x = 5
y = 10

z = x
x = y
y = z

print(f'The value of x is {x} and y is {y}')

# Result
# The value of x is 10 and y is 5

#without using third variable

x=5
y=10

x=x+y
y=x-y
x=x-y

print(x,y)
