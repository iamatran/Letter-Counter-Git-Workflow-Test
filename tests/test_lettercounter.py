import unittest
import unittest.mock #This will let us use mock inputs
from letter_counter import *

class TestLetterCounter( unittest.TestCase ):
    
    #Testing if the counter works with predefined phrases and expected outputs
    #we can make subtests for this function, if one subtest fails, then all fails
    #both subtests will show up as one test
    def test_getTotalOccurrences(self):

        with self.subTest( "phrase has all letters"):
            result = getTotalOccurrencesOfLettersToCount("aabbaacc", "abc")
            self.assertEqual(result, 8) 
        with self.subTest( "phrase has no letters"):
            result = getTotalOccurrencesOfLettersToCount("aabbaacc", "xyz")
            self.assertEqual( result, 0)

    #When testing, it sucks to type in input functions everytime
    #this test will automate the entering the input in the console with a mock input
    def test_inputPhrase(self):
        with unittest.mock.patch('builtins.input', return_value = "the phrase"):
            self.assertEqual( getInputPhrase(), "the phrase")