# set () 
# unordered collection of unique elements
# representation through {} with comma (,) separated values 
# indexing not supported
# slicing not supported
# mutable in nature


#example
set1={1,2,3,4,'a','b','c'}
print(set1) # prints {1, 2, 3, 4, 'a', 'b', 'c'}
print(id(set1)) # prints the memory address of the set



# methods for set
print(len(set1)) # prints 7 replace duplicate with unique
# print(max(set1)) # prints 4
# print(min(set1)) # prints 1
print(type(set1)) # prints <class 'set'>
# print(sum(set1)) # prints TypeError: sum() of set is not supported


# In-built methods
s={1,2,3,4,'a','b','c'}
s.add(5) # adds 5 to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5}

s.update([6,7,8]) # adds 6, 7, 8 to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8}

s.update((9,10,'angel'), 'python') # adds 9, 10, 'angel' to the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10, 'angel', 'python'}

s.pop() # removes the last inserted element from the set
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10, 'angel'}

s.remove('angel') # removes 'angel' from the set .... if ther is no elemet then it give the error also
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10}
s.discard('11') # removes the element if available , if there is no elemet then it will not remove the element and didn't give the error also
print(s) # prints {1, 2, 3, 4, 'a', 'b', 'c', 5, 6, 7, 8, 9, 10}

# s.clear() # clears the set
# print(s) # prints set()

s1=s.copy() # creates a shallow copy of the set
print(s,s1)
print(id(s), id(s1)) # prints the memory address of the set and its copy

s1={1,2,3,4,5}
s2={4,5,6,7,8}

# Returns a new set conating all the unique elemnte from the booth sets
print(s1.union(s2)) # prints {1, 2, 3, 4, 5, 6, 7, 8}

# Retuns a new set only with the common element
print(s1.intersection(s2)) # prints {4, 5}

# It will remove the common element and return the uncommon element only in the first set
print(s1.difference(s2)) # prints {1, 2, 3} in the set

# It will remove all the common element
print(s1.symmetric_difference(s2)) # prints {1, 2, 3, 6, 7, 8}

# keep only element found in the both set
# s1.intersection_update(s2)
# print(s1) # prints {4, 5}
# print(s2) # prints {4, 5, 6, 7, 8}

# It is used to remove all the element from the calling set that are present in the one or more other sets
s1.difference_update(s2)
print(s1) # prints {1, 2, 3}
print(s2) # prints {4, 5, 6, 7, 8}

# remove cpmmon elements and add the unique element 
s1.symmetric_difference_update(s2)
print(s1) # prints {1, 2, 3, 6, 7, 8}   
print(s2) # prints {4, 5, 6, 7, 8}


# Checks if all the elements of one set are present in the other set 
print(s2.issubset(s1))  # print True
print(s1.issubset(s2))  # print False

# it contains all the set of other elements
print(s1.issuperset(s2))      # print True
print(s2.issuperset(s1))     # print False

# Two sets are differnt if they are completely different no overlap
print(s1.disjoint(s2)) # print False 

