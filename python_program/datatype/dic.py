# dictionary.py
# collection of key-value pairs
# keys are unique
# values can be duplicate
# representation through {} with comma separated key-value pairs
# indexing &  slicing not supported
# mutable in nature

d={
    2:'python',
    1:27,
    3:'B.Tech',
    
}

print(len(d)) # prints 7
print(max(d)) # prints 27
print(min(d)) # prints 'B.Tech'
print(sum(d)) # prints TypeError: sum() of dictionary is not supported
print(type(d)) # prints <class 'dict'>
print(id)

e={ 2:'python', 2:37, 3:'Happy'} # prints {2: 27, '3': 'Happy'} over loading
print(e) # prints {2: 27, '3': 'Happy'}
# print(sum(e)) # prints TypeError: sum() of dictionary is not supported
print(max(e)) # prints 27
print(min(e)) # prints 'Happy'   
print(len(e)) # prints 2
print(type(e)) # prints <class 'dict'>  

#  # methods
dict1={
    'name':'python',
    'age':227,
    'qua':'B.tech'
}

print(dict1.keys()) # prints dict_key(['name', 'age', 'qua'])
print(dict1.values()) # prints dict_values(['python', 227, 'B.tech'])
print(dict1.items()) # prints dict_items([('name', 'python'), ('age', 227), ('qua', 'B.tech')])
print(dict1.get('name')) # prints python
print(dict1.get('age')) # prints 227
# dict1.pop('age') # removes the key-value pair with key 'age'
# print(dict1) # prints {'name': 'python', 'qua': 'B.tech'}

# dict1.popitem() # removes the last inserted key-value pair
# print(dict1) # prints {'name': 'python', 'age': 227}

l=[1,2,3,'a','b','c']
d=dict.fromkeys(l) # creates a dictionary with keys from the list and values set to None
print(d) # prints {1: None, 2: None, 3: None, 'a': None, 'b': None, 'c': None}
d=dict.fromkeys(l, 0) # creates a dictionary with keys from the list and values set to 0
print(d) # prints {1: 0, 2: 0, 3: 0, 'a': 0, 'b': 0, 'c': 0}

d.setdefault('name', 'angel') # sets the default value for the key 'name' to 'angel'
print(dict1) # prints {1: 0, 2: 0, 3: 0, 'a': 0, 'b': 0, 'c': 0, 'name': 'angel'}

print(d.setdefault('name', 'angel')) # print angel

# d.clear() # removes all key-value pairs from the dictionary
# print(d) # prints {}

# c0py() - returns a shallow copy of the dictionary
d.copy() # returns a shallow copy of the dictionary
print(d) # prints {1: 0, 2: 0, 3: 0, 'a': 0, 'b': 0, 'c': 0}

# d.update() - updates the dictionary with the key-value pairs from another dictionary
d1={'name':'python', 'age':30, 'qua':'B.E'}
d.update(dict1) # updates the dictionary with the key-value pairs from d1
print(d) # prints {1: 0, 2: 0, 3: 0, 'a': 0, 'b': 0, 'c': 0, 'name': 'python', 'age': 30, 'qua': 'B.E'}