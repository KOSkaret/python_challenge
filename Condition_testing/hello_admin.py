users = []

# 'Jane', 'Morgan', 'admin', 'Tim'

if users:
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see a status report?")
        else:
            print("Hello " + user + ", and thanks for using our services")
else:
    print('We need users!')
