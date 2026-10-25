## python k andr error ur exception bilkul donu dfferent cheezy hai 

#exception error ju hai vo pythn ey ek cencepy ki trha hai yani vo error ju syntax galt huny k vaja
#sy ni blky kouch glt input lyna ya etc

#divisionbyzero error
#type wrror 
#value error


#ham exception error ko handle kar skty hai by using these things lik
#try except else finally raise 

#try => har ek error ko catch karta hai ur agr indentation hai to masal aye ga lakin agr 
#aisy erros hao ju apko ni pata k aye gy tu ham try laga skty hai ur try ju b erro aye ga vo 
# try and ecxept ka estemal akrnys ey hamara code ruky ga ni balky dykhy ga k erro kya aya 
#kis vaja sey aya hai ur then aggy wala code chly ga 
#except ko dy dy ga so then the syntax is 
#else ju k except k bad use hu ga ur agr except na chla tu else chly ga 
#finally vo hai ju ju k koi erro aye ya na aye y chly ga hei chly ga 
#raise = > is ka matlab ap khoud sey b koi exception dy skty hu
a = int(input("please enter the 1st number"))
b = int(input("please enter the 2nd number"))
try:
    print(a/b)
except Exception as err:
    print(f"sorry{err} ")
else:
     print("no error happend ")
finally:
       print("i will run i do not stop no matter errors happen or not")


 #raise = > e smey kafi erro hutti hai jaisy value erro type error 
a = int(input("Please enter your age: "))

if a < 18:
    raise ValueError("You are not eligible")


print("You are eligible")