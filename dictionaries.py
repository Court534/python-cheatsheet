# A dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

my_dict = {'key1':'value1','key2':'value2'}

print(my_dict) # prints {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1']) # prints value1

prices_lookup = {'apple':2.99,'oranges':1.99,'milk':5.80}
print(prices_lookup['apple']) # prints 2.99

d = {'k1':123,'k2':[0,1,2],'k3':{'insideKey':100}} 
print(d['k2']) # prints [0, 1, 2]
print(d['k3']['insideKey']) # prints 100

d = {'key1':['a','b','c']}
print(d) # prints {'key1': ['a', 'b', 'c']}
my_list = d['key1']
print(my_list) # prints ['a', 'b', 'c']
letter = my_list[2]
print(letter) # prints c

# Statement below does the same as the code above in one line
print(d['key1'][2]) # prints c

d = {'k1':100,'k2':200}
print(d) # prints {'k1': 100, 'k2': 200}
d['k3'] = 300
print(d) # prints {'k1': 100, 'k2': 200, 'k3': 300}
d['k1'] = 'NEW VALUE'
print(d) # prints {'k1': 'NEW VALUE', 'k2': 200, 'k3': 300}

d = {'k1':100,'k2':200,'k3':300}
print(d.keys()) # prints dict_keys(['k1', 'k2', 'k3'])
print(d.values()) # prints dict_values([100, 200, 300])
print(d.items()) # prints dict_items([('k1', 100), ('k2', 200), ('k3', 300)])