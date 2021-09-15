import os
# Declaration of variables 

#Declaration of functions

# main

File1 = open("myfile.txt", "w")
L = ["This is Delhi \n", "This is Paris \n", "This is London"]
File1.writelines(L)
File1.close()
  
# Append-adds at last
File1 = open("myfile.txt", "a")  
  
# writing newline character
File1.write("\n")
File1.write("Today")
  
# without newline character
File1.write("Tomorrow")
  
  
File1 = open("myfile.txt", "r")
print("Output of Readlines after appending")
print(File1.read())
print()
File1.close()


#End
