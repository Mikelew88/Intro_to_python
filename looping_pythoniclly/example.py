example_list = ['item1','item2','item3']

print('Not pythonic')
for i in range(len(example_list)):
    print(i)
    print(example_list[i])
print('')
print('Pythonic!')
for item in example_list:
    print(item)
