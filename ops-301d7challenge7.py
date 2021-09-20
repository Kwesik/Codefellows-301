#!/bin/bash/python3
#Script:     os.walk
#Author:     Kwesik
#Last rev:   20210919
 


import os

# Read user input here into a variable
var1 =input("Please enter a file path: ")

# Prints from bottom up all dir, sub dir, and files
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

#End
