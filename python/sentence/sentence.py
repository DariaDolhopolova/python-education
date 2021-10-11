"""There are 3 classes:
Sentence - container class, takes only one sentence
SentenceIterator - iterates over words in Sentence
MultipleSentenceError - error class for multiple sentence case"""


class MultipleSentenceError(Exception):
    """Exception for multiple sentences"""
    print('The message consists of more than one sentence.')


class SentenceIterator:
    """SentenceIterator class implements iteration for Sentence class"""
    def __init__(self, text_wo_other_char):
        self.text_wo_other_char = text_wo_other_char
        self.start = 0
        self.space_index = self.text_wo_other_char.find(" ")
        self.turns = self.text_wo_other_char.count(" ")

    def __getitem__(self, item):
        """Should get item by index using split method on text"""
        if isinstance(item, int):
            if self.text_wo_other_char.split()[item]:
                return self.text_wo_other_char.split()[item]
            else:
                raise KeyError("Key is out of range")
        else:
            raise TypeError("Wrong key type")

    def __next__(self):
        """Implements iteration by words in text"""
        if self.turns > 0:
            word = self.text_wo_other_char[self.start:self.space_index]
            self.start = self.space_index
            self.space_index = self.text_wo_other_char.find(" ", self.space_index + 1)
            self.turns -= 1
            return word
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Sentence:
    """Container class takes a sentence as an input.
    You can iterate over it, look how many words and other characters there are."""
    def __init__(self, text: str):
        self.text = text
        self._errors()
        self.text_wo_other_char = self._remove_other_char()
        self.other_chars_counter = len(self.other_chars)
        self.words_counter = len(self.words)

    def _errors(self):
        """Checks for all errors, though Multiple error doesn't work for now"""
        if self._type_error():
            raise TypeError
        if self._end_error():
            raise ValueError
        if self._multiple_error():
            raise MultipleSentenceError

    def _type_error(self):
        """Checks if text in object is str
        :return: is_error
        """
        is_error = False
        if not isinstance(self.text, str):
            is_error = True
        return is_error

    def _end_error(self):
        """
        Checks if text ends with . ! ?
        :return: is_error
        """
        correct_endings = ['.', '!', '?']
        is_error = True
        if self.text[-1] in correct_endings:
            is_error = False
        return is_error

    def _multiple_error(self):
        """Should check if there is one or more sentences in text
        Not sure why it's not working correctly"""
        correct_endings = ['.', '!', '?']
        is_error = True
        ending_counter = 0
        for symbol in correct_endings:
            ending_counter += self.text.count(symbol)
        if ending_counter <= 1:
            is_error = False
        return is_error

    def _remove_other_char(self):
        """Removes all nonspace and nonalphabetic characters from the text"""
        text_w_letters_spaces = ''
        for symbol in self.text:
            if symbol.isalpha() or symbol == ' ':
                text_w_letters_spaces += symbol
        return text_w_letters_spaces

    def __repr__(self):
        return f"<Sentence(words={self.words_counter}, other_chars={self.other_chars_counter})>"

    def __iter__(self):
        return SentenceIterator(self.text_wo_other_char)

    def _words(self):
        """Returns lazy iterator for taking words one by one"""
        return (word for word in self.text_wo_other_char.split())

    @property
    def words(self):
        """Property that has a list of words"""
        words_list = []
        for word in self._words():
            words_list.append(word)
        return words_list

    @property
    def other_chars(self):
        """Property that has list of nonalphabetic characters"""
        other_chars_list = []
        for symbol in self.text:
            if not symbol.isalpha():
                other_chars_list.append(symbol)
        return other_chars_list


if __name__ == '__main__':
    TEXT = 'Hello my friend where have you been?'
    iter_word = Sentence(TEXT)
    print(f'Test sentence: {TEXT}')
    print(f"Test 1, __repr__ : {iter_word}")
    # print(f"Test 4, slice[1:8:2]: {Sentence(TEXT)[1:8:2]}")
    print(f"Test 5, index[4]: {SentenceIterator(TEXT)[4]}")
    print('Test 6, cycle :')
    for r in iter_word:
        print(r)
    print(f'Test 7, words: {iter_word.words}')
    print(f'Test 8, non_ite: {iter_word.other_chars}')
