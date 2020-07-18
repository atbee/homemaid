a = 1
print(a)

b = 2

c = 'hello'
print(c)

if a == 1:
    print('1')

    if b == 2:
        print('2')
elif a is None:
    print('a is None')
else:
    pass

if a:
    pass

if a is not None:
    pass

def say():
    print('hello')

say()

# prefer this
def say1(number):
    print(f'hi {number}')

say1(32)

# not recommended
def say2(number: int):
    pass

