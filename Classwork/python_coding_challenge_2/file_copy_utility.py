#  File Copy Utility 
# Problem Statement 
# Sample Input/Data 
# Source File (notes.txt) 
# Python supports file handling. 
# Functions improve code reusability. 
# Dictionaries store data in key-value pairs. 
# Tasks 
# 1. Read the contents of the source file.  
# 2. Copy the entire content to another file named backup.txt.  
# 3. Display a success message.  
# 4. Verify whether both files contain the same number of lines.  
# Sample Output 
# File copied successfully. 
 
# Source File Lines: 3 
 
# Backup File Lines: 3 
 
# Verification Status: Successful 

#--------------------------------------------------
# Task 1: Read the Contents of Source File
#--------------------------------------------------

source_file = open("notes.txt", "r")
content = source_file.read()
source_file.close()


#--------------------------------------------------
# Task 2: Copy Content to backup.txt
#--------------------------------------------------

backup_file = open("backup.txt", "w")
backup_file.write(content)
backup_file.close()


#--------------------------------------------------
# Task 3: Display Success Message
#--------------------------------------------------

print("File copied successfully.")


#--------------------------------------------------
# Task 4: Verify Number of Lines in Both Files
#--------------------------------------------------

source_file = open("notes.txt", "r")
source_lines = source_file.readlines()
source_file.close()

backup_file = open("backup.txt", "r")
backup_lines = backup_file.readlines()
backup_file.close()

print("\nSource File Lines:", len(source_lines))
print("\nBackup File Lines:", len(backup_lines))

if len(source_lines) == len(backup_lines):
    print("\nVerification Status: Successful")
else:
    print("\nVerification Status: Failed")
