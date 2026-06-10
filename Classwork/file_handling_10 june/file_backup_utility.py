# : File Backup Utility 
# An organization wants to create backups of important text files to prevent accidental data loss. You have been 
# asked to develop a utility that creates an exact copy of an existing file. 
# Requirements 
# Write a Python program that reads the entire contents of a source file and copies them into another 
# destination file. 
# The program should: 
# 1. Accept the names of the source file and destination file from the user.  
# 2. Read the complete contents of the source file.  
# 3. Write the contents into the destination file.  
# 4. Display a success message after the copying process is completed.  
# Sample Source File (notes.txt) 
# Functions help in code reusability. 
# File handling enables persistent storage. 
# Python provides various modes to work with files. 
# Expected Output 
# Enter Source File Name      : notes.txt 
# Enter Destination File Name : backup.txt 
 
# File copied successfully. 
# All contents from 'notes.txt' have been copied to 'backup.txt'.

f1 = open('file3.txt', 'r')
f2 = open('file4.txt', 'w')

data = f1.read()
f2.write(data)

f1.close()
f2.close()

print("File copied successfully")
