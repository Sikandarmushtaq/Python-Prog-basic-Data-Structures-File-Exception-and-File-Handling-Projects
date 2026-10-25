 #file modes
#there are four modes
#r w a x
#r => read only 
#w => write and also create file
#a = > create and append 
#x   =>creaate new file 


#and the syntax is
# file = open("superman.text","w") 
# # we can save it in any variable
# data  = input("what you want to write in your file")
# #to write in your file we have
# file.write(data)



# newfile = open("superman.text","r")

# print(newfile.read())


with open("superman.text","a") as updatefile:
    updatefile.write(" " + " this time i am updating")

