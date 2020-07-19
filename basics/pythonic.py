# Idiomatic Python code

# 1. Avoid comparing directly to `True`, `False`, or `None`
a = True
if a is True:
    print('a is true')

# Do this
if a:
    print('a is true')

if not a:
    print('not a')

# 2. Avoid repeating variable name in compound if statement
a = 1
if a == 1 or a == 2 or a == 4:
    print('a: ', a)

# Do this instead
if a in [1, 2, 3, 4]:
    print('a: ', a)

# 3. 3. Use `in` to iterate over iterable
l = [1, 2, 3, 4]
for item in l:
    print(item)

# 4. Use default parameter of `dict.get`
a = {
    'name': 'Atb',
}
print(a['name'])

if 'name' in a:
    print(a['name'])

# Do this
print(a.get('name', None))

# 5. Use `enumerate` function in loops
names = ['Atb', 'Kan', 'Odds']
count = 1
for name in names:
    print(f'{count}. {name}')

# Do this instead
for index, name in enumerate(names):
    print(f'{index+1}. {name}')

# 6. Use `_` for data that should be ignored
names = ['Atb', 'Kan', 'Odds']
for _, name in enumerate(names):
    print(f'{name}')

# 7. Use (for) `else` after iterator is exhausted!
check = False
for name in names:
    if name != 'Atb':
        check = True
        break

if check:
    print('yes')

# Do this
for name in names:
    # Do something
    # ถ้า loop ไม่โดน break จำทำ else
else:
    print('yes')

# 8. List comprehension to create a transformed list
names = []
for i in range(10):
    names.append(i)

# Do this
names = [i for i in range(10)]

# 9. Use context manager to ensure resources are managed
f = open('file')
...
f.close()

# Do this
with open('file') as f:
    ...

# 10. Use generator to lazily load infinite sequences
