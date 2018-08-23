import unittest
from city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """ Tests for city_functions.py """

    def test_city_country(self):
        """Does Santiago, Chile work?"""
        formatted_sentence =  get_city_country('santiago', 'chile')
        self.assertEqual(formatted_sentence,'Santiago, Chile')

    def test_city_country_population(self):
        """Does Santiago, Chile - population 5000000 work?"""
        formatted_sentence = get_city_country('santiago','chile', population=5000000)
        self.assertEqual(formatted_sentence,'Santiago, Chile - population 5000000')

unittest.main()