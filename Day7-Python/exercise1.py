# using '+'
list1 = ['Kim', 'John', 'Peter', 'Nick']
list2 = ['June', 'July', 'August']

list3 = list1+list2
print(list3)

# using append()
# for s in list1:
#   list3 = list1.append(list2)

# print(list3)
# using extend()
list1.extend(list2)
print(list1)

# using .insert()
list1.insert(1, 'Mwangemi')
print(list1)

print(list3[2:4])
print(list3[-4:-1])
print(list3[3:])
print(list3[:3])

list3.clear()
print(list3)
