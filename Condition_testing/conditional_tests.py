list = ['Knut', 'School', 'Python', 'Challenge']
user = 'Knut'

if user in list:
  print( user.title() +" is here!")

user = 'Karl'

if user not in list:
  print( user.title() +" is not here!")

age = 22

if age > 18:
  print("Age is larger than 18")

user = 'Knut'
age = 25

if age > 18 and user.lower() == 'knut':
    print(user.title() + " is " + str(age))


#  Other testing methods with numbers involve !=, which is not equal.
#  We have also "or", which makes it so that either of the conditions on
#  either side can be true for the condition to be True.

driver_license = True

if driver_license == False:
    print("You don't have a license")
    print("How about start to do it?")
else:
    print("Nice! Don't do any reckless driving now!")


# Admission for anyone under age 4 is free.
# Admission for anyone between the ages 4 and 18 is 50 kr.
# Admission for anyone older than 18 costs 100 kr.
age = 25

if age < 4:
    price = 0
elif age < 18:
    price = 50
else:
    price = 100

print("Your admission cost is " + str(price) + " kr.")

# One can drop the final else, and go for an elif instead.
# With that, so can we define the specific conditions we want instead of the
# uncertainty for unknown data to be sendt.
