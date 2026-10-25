#data structure type-> this is n built data structures in python there are some other data structure hai ur 
#un k algorithms hai like linked list queue list hash map etc en k algorithm ki sudy ko DSA khty hai
#1 lists
#2 tuple
#3 set dictonary
#


# list is ordered    2 mutable(kis b cheez ko change kar skty hu )  =>dublicate



a = [1,2,3,4,5,6,7,8,9,0]



# traversing on index
for i in a:
    print(i)


#traversing on value
for j in range(0,len(a)):
   print(a[j])


#list methods
#a.append("helo")   #add value at the last 
#a.insert(0,"first")   #list mey khib kouch dalny k liya insert use kary y index lyta hai ur kya add karna hai vo
# a.pop()   # es mey index b dy skty hai lakin agr ni diya tu by defaut last wala remove hu jaye ga 
#ur pop ju item remove karta hai vo pop mey hei return hu jati hai 
#a.remove(3)  #remove mey value dyni huti hai ur y phli value ko hatata hai agr list mey two abr 3 hu ga tu ju 
#ju 3 phly aye ga vo remove hu jaya ga 



arr = [3,-1,4,5,-2,-3]

pos = []
neg = []

for i in arr:
    if(i > 0):
       pos.append(i)
    else:
      neg.append(i)

    print(pos)

    print(neg)

arr = [10,20,30,40]
mean = 0

for i in arr:
     mean+= i/4

print(mean)


#tuple data structure is a immutable list created with ()

# we ca change alist in tuple
#like a = []  => b = tuple(a)  => so after that a list converted into tuple

#tuple has two methods index()  and count()


#set   {}   => unique values only 
#covert list or tuple in set => set()
#set sey ap ju b create karty hu tu oski ek hash value create hutti hai 
#we can use hash() function  to see the hash value of aany set values
#set do not allow to store list[] in it because list is the thing which is mutable and can change 
#ham set mey index pata ni kar skty so we can not know konsy index par konsi value rakhi huvi hai 
# there is no order in set we can only use loop like for i in set we can not not use range 
#method of sets
#set.add() add an elemnt in set 
#set.discard() to remove a specified element 
#set.pop() remove an random element from the set 
#set.remove() to remove the specified element 

#set operations
# (1)
 #if we have two set and we want to check the diffrence between two set so we use:
 # we can use difference() or we can use minus - as well for same work
# set1 = {1,2,3,4,5}
# set2 = {1,2,3,7,8}

# print(set1.difference(set2))


#(2) differnce and update
#y ju valyue 1 set b hu gi ur dsry mey b un ko dykhy ka minus kar dey ga ur update b akr dey ga yani
#we cans ay remove hu jaye gi 
#not use the same keys because it pick the first key of the same name
# s = {1,2,3,4}
# s2 = {1,2,3,4,5,6}

# s -= s2
# print(s)


# (3)
#intersection() and we can also use intersection_update() to find values which are same in two set then
#  we use it and we can also update it 
# symbol: & for only intersection and &= for update 
# s1 = {1,2,3}
# s2 = {1,2}
# s1&= s2

# print(s1&s2 )

# (4)
#issubset() to check if all the items of ones set is present in other set return true or false
#is ka matlab y hai agr ek sey mey 4 value hai ur dsry mey b 4 hu agr 2 valye 2srty set mey hai lalkin vo 
#do values phly set sey match karti hai then second set return true 
# symbol = <=

# s = {1,2,3,4,5,6,7}
# s2 = {1,2,3,4,5,6,7}
# s3 = {1,2,3,4,5,8}

# print(s3.issubset(s))

# (5)
#issuperset() return true i fall the all items of one set is present in another set,same working like is
#same working like issubset 
#symbol >= 

# s = {1,2,3,4,5}
# s2 = {1,2}

# print(s>=s2)


# (6)
#symmetric_difference() to check the values which are different in two set and also update
#symbo : ^   and ^= 

# s1 = {1,2,3,4}
# s2 = {1,2,5,6}

# print(s1.symmetric_difference(s2))

# (7)
# union() we use it when we need all the value same unsame so we use union we also can update using update()
# symbol: | and to update |=    

# s1 = {1,2,3,4,}
# s2 = {1,2,3,4,5,6}

# print(s1.union(s2))




# #Dictonary   {} and value store in the way and that way is key and value pair 
#yaha par ju keys hutti hai vahi role play karti hai indexing ka 
# syntax is:
# d = {1:20,"name":"sikandar"}
#so here 1 is key and 20 is value 
# print(d["name"])


# vanilla python
#crud operation
#c = create  we use d[50] = 40 
#so we are creating an key with 50 and value with 40 
#r = read we can use print(d[50]) so we are technically redaing a dictionary 
#u = update we can update any already exit keys values by using d[50] = 70
#D = delete we can delete any already exits key and their values by using


# methods of dictionary
#(1) = >fromkeys()
#y hmy purni dictionary sey ek nayi dictinary return karta hai asal dictionary mey koi changing ni karta 
#ur yaha ham phli dictionary mey majood keys ki values ko chnage kar skyty hai
#  ur nayi key and valye b dal skrty hai 

# d ={ 1:2,2:3,3:4}
# q= d.fromkeys([1,],100)

# print(q)
# print(d)

#(2)get() y kisi b dictiinary mey kis b specified key ki value ko get karny k liya hutta hai 

# d = {"name":"sikandar"}
# print(d.get(name))

#(2)
# # items() => y kisi b dictionary par lagany sey ek list dy ga ur os list mey har key and oski value
#ko ek tuple mey rakha jaye ga jitni b keys hu gi utni hei tuples bny gi
# d= {1:2,2:3,4:5,"name":"sikandar"}
# print(d.items())

#(3)
# keys() and values()
# keys()y=>  kisi b dictinary mey jitni b keys hu unki list return kary ga 
#values => y kisi b dictionarymey majood values ko return kary ga ek list ki shakl mey 
# d= {1:2,2:3,4:5,"name":"sikandar"}
# print(d.keys())
# print(d.values())

# (4)=>pop()
# remove the value wit the specified key
# d = {1:2,"name":"sikandar"}
# print(d.pop("name"))
# print(d)

#(5) => popitem() remove the last inserted key and value
# d = {1:2,2:3,4:5 }
# d.popitem()
# print(d)


#(6)=>setdefault() y age value exit karti hai dictioanry mey to oski value ko update ni kary ga 
#balky osi key ju value hu gi vo return kar dey ga ur agr key exit ni karti tu nayi key k sath ju
#value ham de gy vo add kar dey ga 

d = {"name":"sikandar","age":23}
print(d.setdefault("age", 24))
print(d.setdefault("role", "developer"))
print(d)


#(7) update({}) tu yaha ham kisi exiting key ki valye ko update b kar skty hai
#ur nayi value b dal skty hai 
d = {"name":"sikandar","age":23,}
d.update({"name":"sikandar Mushtaq"})
d.update({"role":"developer"})
print(d)

#loops on dictionary 

data = {"name":"sikandar","age":23,"role":"developer"}
# if we wants to print only keys
for i in data:
   print(i)
# #if we want to print both keys and values then the loop will be
for values in data:
     print(f"the key is {values} and the value is {data[values]}")
  





