d = {}
d1 = dict()
d2 = {'name':'codegnan',
      'branch':'hyd',
      'batch':'pfs66',
      'no_students':51,
      'subject':'python'}
print(type(d),type(d1),type(d2))
print(d2['name'])
print(d2['branch'])
t = (1,2)
print(t)
print(*t)
print(d2['subject'])
print(d2)
d2.popitem()
print(d2.keys())
print(d2.values())
print(d2.items())