sum = 2 + 2
# print(sum)

#LIST
# you can put a list within a list... this is a list like an array
my_list = ["hello", "world", 2, True, [1,2,3], {"name": "Fred"}]
my_list.append("Stevo")
my_list.insert(2,124)
my_list.append("Leah")
my_list.extend (["Mary", "Matthew", "cohort 9"])
# print(my_list)

#my_list.append (do a dot after and see everything that comes up)
#append is the new push
#append allows u to add ONE THING
#expent allows us to add multiple things (doesn't add a nested list, it is looping over and adding each one individually)

my_new_list = list("hey")
# print(my_new_list)




this_list = ["hey","birthday", "False", 4]
# print(this_list)

this_list.extend (["hola", "heyHey"])
this_list.insert(1, "Karla")

#removes the last thing on the list
# print(this_list.pop())


numbered_list = [1, 2, 3, 4, 5]
# following code will reverse the order of the list.
numbered_list.reverse()
# print("Reversed List", numbered_list)

rev = numbered_list.reverse()

# print(my_new_list.count(2))

#Dictionary
my_pairs = {
    "name":"Fred",
    "age":46
#    3: "wtf",
#    True: "practice"
}
# print(my_pairs)

# no dot notation to reference a key in a diccionary (Object)
name = my_pairs["name"]
# print(name)

my_pairs["last"] = "Jones"
# print(my_pairs)

my_pairs["address"] = {"street": "123 Sesame St", "zip": 34567}
# print(my_pairs)

# print(my_pairs["address"]["zip"])

#you get a list of a collection - Tuples
# print("items", my_pairs.items())
# print("values", my_pairs.values())

#how to iterate over stuff? FOR LOOP***** for in

#in python WHITE SPACE MATTERS - it won't run it if not indented
# in JS you use {}, in python to be in the scope is with indent/space, it's up to me to indent, format wont work. White space matters

for foo in my_pairs.values():
    print(foo)

for key, value in my_pairs.items():
    print(value)

for key, value in my_pairs.items():
    print(f"This came from my_pairs:{value}")

print(f"Hello, my name is {my_pairs['name']}")

#diccionaries and sets are both enclosed in curly brackets
#a set is a different collection

my_set = {"fred", 3, 12, True, "Jones", 3}

# print("set", my_set)
#my set cannot have duplicate values, it won't read the duplicate

#empty set
my_list = set()

# my_list= {}




#this below got rid of all the duplicates and turned it back into a list
my_dupes = [1, 2, 3, 2, 4, 5, 1]
my_dupes = set(my_dupes)
print(list(my_dupes))

#you can also do
my_dupes = list(set(my_dupes))

#no order in a set when you add something to it.
my_set.add("hellow C33")
print(my_set)

print(set(my_pairs)) #you cannot have duplicate keys with set in a dicctionary.

#Tuples - funky little beasts, it doesn't care if you have dups, or anything in it. A locked down collection, its a volt, you can't take anything out of it and can't add anything to it, its immutable, it you want a collection of stuff that will never be mutated.. then use a tuples. Tuple no curly brackets... it uses paranthesis ()
#tuple = list with a lock

my_tup = ("1", 1, 3, "Hello", True, 3)
print(my_tup)

print(my_tup.count(3))

print(my_tup.index("Hello"))

#you have to tell it its a tuple by adding a comma after it like below.

# sayMyName(("fred",))

#conditionals - no () or {} , triple equals is not a thing, indent matters, there is no type cohersion in python, we do double ==

name = "Stebe"
if name == "Steve":
    print("I feel good")
elif name == "Joe":
    print("Joe is the King of the World")
else:
    print("I have a cold")

# instead of == you can use "is", or "is not" != ! + =


# name = "Stebe"
# if name is "Steve":
#     print("I feel good")
# elif name is not "Joe":
#     print("Joe is the King of the World")
# else:
#     print("I have a cold")















/Users/kgallegos/py101/intro.py