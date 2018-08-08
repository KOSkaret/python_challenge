current_users = ['JOHN','CARolina','Xx_quixScope_xX']
new_users = ['john', 'carolina', 'ted', 'chippy']

def compareWithUsers(new_user, users):
    # Using a list comprehension to make a new list
    # where all values are in lower case, and then
    # compare that list with the new_user.
    users_temp = [user.lower() for user in current_users]
    message = 'An user already has the name "' + new_user + '", try with a new one.'
    if user.lower() not in users_temp:
        print('The username is available')
    else:
        print(message)

for user in new_users:
    compareWithUsers(user, current_users)
