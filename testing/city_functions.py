
def get_city_country(city, country, population = ''):
    """ Return a string which combines a city and a country """

    if population:
        return city.title() + ', ' + country.title() + ' - population ' + str(population)
    else:
        return city.title() + ', ' + country.title()