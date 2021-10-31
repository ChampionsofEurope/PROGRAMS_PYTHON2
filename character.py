
test_list = ['Chelsea', 'is', 'best', 'team in', 'Prem']


print("The original list is : " + str(test_list))

res = [sub.replace('C', '+').replace('h', 'p').replace('m', '1') for sub in test_list]


print("List after performing character swaps : " + str(res))
