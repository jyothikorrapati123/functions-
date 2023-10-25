#String Transform Functions

#capitalize
#Syntax:variable.capitalize()

name="jyothi"
print(name.capitalize())

#Title
#syntax:variable.title()

name="jyothi korrapati"
print(name.title())

#upper
#syntax:variable.upper()

name="jyothi"
print(name.upper())

#lower
#syntax:variable.lower()

name="JYOTHI"
print(name.lower())

#casefold
#syntax:variable.casefold()

name="JYOTHI"
print(name.casefold())

#swapcase
#syntax:variable.swapcase()

name="jyothi"
print(name.swapcase())


#String Check Functions

#isnumeric
#syntax:variable.isnumeric()
number="1255666666"
print(number.isnumeric())

#isalphanumeric
#syntax:variable.ialnum()

num="768682638233682"
print(num.isalnum())

#isdecimal
#syntax:variable.isdecimal()

num="Jyothi"
print(num.isdecimal())

#isdigit
#syntax:variable.isdigit()

num="1555555555"
print(num.isdigit())

#isascii
#syntax:variable.isascii()

num="abc"
print(num.isascii())

#isupper
#syntax:variable.isupper()

num="jyothi"
print(num.isupper())

#islower
#syntax:variable.islower()

num="JYOTHI"
print(num.islower())

#isspace
#syntax:variable.isspace()

num=" "
print(num.isspace())

#isidentifier
#syntax:variable.isidentifier()

num="@"
print(num.isidentifier())

#isprintable
#syntax:variable.isprintable()

num="Jyothi"
print(num.isprintable())

#istitle
#syntax:variable.istitle()

num="jyothi korrapati"
print(num.istitle())


#String Search Functions

#index
#syntax:variableName.index(string/char)

email="jyothi@gmail.com"
print(email.index("@"))

#rindex
#syntax:variableName.rindex(string/char)

email="jyothi@gmail@.com"
print(email.rindex("@"))

#rfind
#syntax:variableName.rfind(string/char)

email="jyothi@gmail@.com"
print(email.rindex("@"))

#startswith
#syntax:variableName.startswith(string/char)

name="Jyothi"
print(name.startswith("Jyothi"))

#endswith
#syntax:variableName.endswith(string/char)

name="Jyothi"
print(name.endswith("Jyothi"))


#list methods

#Append
#syntax:lst.append()

a=[]
print(a.append("Jyothi"))
print(a)

#insert
#syntax:lst.insert(index,item)

a=["Jyothi","vasu"]
print(a.insert(1,"abhi"))
print(a)

#Extend
#syntax:lst.extend(lst1)

name=["jyothi","sumathi"]
name1=["vasu","abhi"]
name.extend(name1)
print(name)

#count
#syntax:lst.count(item)

name=["Jyothi","sumathi","sumathi"]
print(name.count("sumathi"))



#pop
#syntax:lst.pop()

name=["jyothi","sumathi","venky"]
print(name.pop())

#remove
#syntax:lst.remove()

name=["Jyothi","sumathi"]
print(name.remove("Jyothi"))
print(name)

#clear
#syntax:lst.clear(item)

name=["Jyothi","Sumathi","venky"]
print(name.clear())
print(name)

#sort
#syntax:lst.sort()

a=[1,2,5,3]
a.sort()
print(a)

#reverse
#syntax:lst.reverse()

a=[1,2,5,3]
a.reverse()
print(a)


#Tuple Methods

#count
#syntax:tpl.count(item)

tpl=tuple((1,4,3,5,4))
print(tpl.count(4))

#index
#syntax:tpl.index(item)

tpl=tuple((1,2,3,))
print(tpl.index(1))

#set methods

#add
#syntax:variable.add()

a={'a','v','s'}
a.add('y')
print(a)

#update
#syntax:variable.update(setvariable)

a={'a','b','c'}
b={'b','c','d'}
a.update(b)
print(a)

#remove
#syntax:variableName.remove(item)

a={'a','b','c'}
a.remove('b')
print(a)

#discard
#syntax:variableName.discard(item)

a={'a','b','c'}
a.discard('c')
print(a)

#pop
#syntax:variableName.pop()

a={'a','b','c'}
a.pop()
print(a)


#frozenset methods

#union
#syntax:variableName.union(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.union(b))

#intersection
#syntax:variableName.intersection(variable)

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection(b))

#intersection update
#yntax:set1.intersection_update

a={'a','b','c'}
b={'b','c','d'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint
#syntax:set1.isdisjoint(set2)

a={'a'}
b={'b'}
print(a.isdisjoint(b))

#difference
#syntax:set1.difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.difference(b))

#symmetric difference
#syntax:set1.symmetric difference(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference(b))

#symmetric difference update
#syntax:set1.symmetric difference update(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset
#syntax:set1.issubset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issubset(b))

#issuperset
#syntax:set1.issuperset(set2)

a={'a','b','c'}
b={'b','c','d'}
print(a.issuperset(b))