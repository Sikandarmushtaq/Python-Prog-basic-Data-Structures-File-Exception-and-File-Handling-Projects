from pathlib import Path
import os


def createfile():
    try:
        name = input("Enter your file name:-")
        path = Path(name)
        if not path.exists():
            data  = input("Enter something to your file:-")
            with open(path,"w") as fs:
                fs.write(data)
                print("file created sucessfully")
        else:
            print("File already exits")
    except Exception as err:
        print(f"Some error occured due to {err}")


def readfile():
    try:

        name = input("Enter the filename you want to read:-")
        path = Path(name)
        if path.exists():
            with open(path,"r") as fs:
                print(fs.read())
        else:
             print("File does not exits sorry")
    except Exception as err:
             print(f"Some error occured due to {err}")
           



def updatefile():
    try:

        name = input("Enter the file name you want to update:-")
        path = Path(name)
        if path.exists():
            data = input("Enter something to update your file:-")
            with open(path,"a") as fs:
                fs.write(" " + data)
                print(f"{path} is updated sucessfully")
        else:
            print("File does not exits")        
    except Exception as err:
          print(f"Some error occured due to {err}")

def deletefile():
    try:
        name =  input("Enter the file name you wnat to delete:-")
        path = Path(name)
        if path.exists():
            path.unlink()
            print(f"{path} is deleted sucessfully")
        else:
            print("File does not exits sorry")
    except Exception as err:
        print(f"Some err happed due to {err}")





print("press 1 to create file")
print("press 2 to read file")
print("press 3 to update file")
print("press 4 to delete file")

response = int(input("Enter you response:-"))

if response == 1:
    createfile()

if response == 2:
    readfile()
if response == 3:
    updatefile()
if response == 4:
    deletefile()