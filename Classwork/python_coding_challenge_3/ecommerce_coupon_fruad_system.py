#  E-Commerce Coupon Fraud Detection 
# Problem Statement 
# A file named coupons.txt contains coupon usage records. 
# SAVE50 
# WELCOME20 
# SAVE50 
# FESTIVE10 
# SAVE50 
# WELCOME20 
# NEWUSER 
# FESTIVE10 
# SAVE50 
# NEWUSER 
# Tasks 
# 1. Count the usage frequency of each coupon.  
# 2. Identify coupons used more than 3 times.  
# 3. Create a set of unique coupons.  
# 4. Display the most frequently used coupon.  
# 5. Save suspicious coupon records into fraud_report.txt.  
# Sample Output 
# Coupon Usage Frequency: 
# SAVE50 : 4 
# WELCOME20 : 2 
# FESTIVE10 : 2 
# NEWUSER : 2 
# Suspicious Coupons: 
# SAVE50 
# Unique Coupons: 
# {'SAVE50', 'WELCOME20', 'FESTIVE10', 'NEWUSER'} 
# Most Frequently Used Coupon: 
# SAVE50 
# resources = { 
# "Warehouse1": ["Food", "Medicine", "Blankets"], 
# Fraud Report Generated Successfully. 

#--------------------------------------------------
# Task 1: Count the Usage Frequency of Each Coupon
#--------------------------------------------------

file = open("coupons.txt", "r")
coupons = file.read().splitlines()
file.close()

frequency = {}

for coupon in coupons:
    if coupon in frequency:
        frequency[coupon] += 1
    else:
        frequency[coupon] = 1

print("Coupon Usage Frequency:")

for coupon, count in frequency.items():
    print(coupon, ":", count)


#--------------------------------------------------
# Task 2: Identify Coupons Used More Than 3 Times
#--------------------------------------------------

suspicious_coupons = []

for coupon, count in frequency.items():
    if count > 3:
        suspicious_coupons.append(coupon)

print("\nSuspicious Coupons:")

for coupon in suspicious_coupons:
    print(coupon)


#--------------------------------------------------
# Task 3: Create a Set of Unique Coupons
#--------------------------------------------------

unique_coupons = set(coupons)

print("\nUnique Coupons:")
print(unique_coupons)


#--------------------------------------------------
# Task 4: Display the Most Frequently Used Coupon
#--------------------------------------------------

most_used_coupon = max(frequency, key=frequency.get)

print("\nMost Frequently Used Coupon:")
print(most_used_coupon)


#--------------------------------------------------
# Task 5: Save Suspicious Coupon Records into fraud_report.txt
#--------------------------------------------------

file = open("fraud_report.txt", "w")

for coupon in suspicious_coupons:
    file.write(coupon + "\n")

file.close()

print("\nFraud Report Generated Successfully.")
