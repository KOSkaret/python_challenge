magicians = ['hoodini','penn','teller','merlin']

def show_magicians(mages):
    for mage in mages:
        print("Welcome to " + mage.title())

def mage_great(mages):
    for i in range(len(mages)):
        mages[i] += " the great"
    return mages

great_magicians = mage_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
