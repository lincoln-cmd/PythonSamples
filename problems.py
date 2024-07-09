
#12

tuple1 = (45, 45, 45, 45)

'''if len(set(tuple1)) == 1:
    print(True)
else:
    print(False)
'''

print(all(i == tuple1[0] for i in tuple1))

