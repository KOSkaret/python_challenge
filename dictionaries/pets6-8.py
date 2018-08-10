pets = {
    'Rex':{
        'animal':'Cat',
        'owner':'Cathrine',
        },
    'Doggy':{
        'animal':'dog',
        'owner':'Baby',
        },
    'Terry':{
        'animal':'Tyrannosauros rex',
        'owner':'[owner not found]',
        },
    }

for pet, pet_data in pets.items():
    print(pet + ' is a ' + pet_data['animal'] +
        ' and is owned by ' + pet_data['owner']
        )
