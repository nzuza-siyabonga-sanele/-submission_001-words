import unittest
import sys
import word_processor


class MyTestCase(unittest.TestCase):
    def test_string_to_list(self):
        text="The word processing program needs to offer functionality that helps determine linguistic complexity."
        result = word_processor.convert_to_word_list(text)
        self.assertEqual(type(result),list)
        
    def test_the_list_equal(self):
        text="The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        out = ["the","word", "processing", "program", "needs", "to", "offer" ,"functionality" ,"that" ,"helps" ,"determine" ,"linguistic" ,"complexity"]
        result = word_processor.convert_to_word_list(text)
        self.assertEqual(result,out)
    
    def test_longer_words(self):
        mytext = "The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        out = ["processing" ,"program" ,"functionality" ,"determine" ,"linguistic" ,"complexity"]
        result = word_processor.words_longer_than(6,mytext)
        self.assertEqual(result,out)
    
    def test_longer_one_word(self):
        mytext = "The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        out = ["functionality"]
        result = word_processor.words_longer_than(12,mytext)
        self.assertEqual(result,out)
    
    def test_type(self):
        text = "The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        result = word_processor.words_lengths_map(text)
        self.assertEqual(type(result),dict)
        
    def test_type_letters_a_to_z(self):
        text = "The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        result = word_processor.letters_count_map(text)
        self.assertEqual(type(result),dict)
    
    def test_highest_letter(self):
        text = "The word, processing program needs. to offer functionality, that helps determine linguistic complexity?"
        result = word_processor.most_used_character(text)
        self.assertEqual(result,"e")


if __name__ == '__main__':
    unittest.main()
