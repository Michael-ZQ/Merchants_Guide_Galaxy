from roman_numerals import RomanNumerals

class MerchantRobot:
    words_book = {}
    prices_book = {}

    default_answer = ""
    def __init__(self, default_answer):
        self.default_answer = default_answer

    def build_words_book(self, galactic_words):
        # with words: glob is I
        # return the error messages in words
        error_messages = []
        for item in galactic_words:
            patterns = item.split()
            # print(patterns) -> ['glob', 'is', 'I'] ... ... 
            
            if len(patterns) == 3 and patterns[1] == 'is':
               if patterns[0] not in self.words_book:
                    self.words_book.update({patterns[0]: patterns[2]})
                
            else:
                # bad pattern 
                error_messages.append(item)
        return error_messages
    
    def build_prices_book(self, prices_words):
        # prices_words: glob glob Silver is 34 Credits
        # return the error_messages in prices_words
        error_messages = []
        for item in prices_words:
            patterns = item.split(' ')
            # find the position of name and price by unit
            try:
                pattern_price = int(patterns[-2])
            except ValueError:
                print("That's not an int:", patterns[-2])
                error_messages.append(item)
            
            metal_name = patterns[-4]
            
            amount_arabic = self.translate_to_arabic(patterns[:-4])

            

            if amount_arabic:
                # price by unit
                unit_price = float(pattern_price)/amount_arabic

                # print(pattern_price, amount_arabic)
                if metal_name not in self.prices_book:
                    self.prices_book.update({metal_name: unit_price})
                
            else:
                print('Error while updaing prices dict with:', metal_name, amount_arabic)
                error_messages.append(item)
        return error_messages

    def translate_to_arabic(self, galactic_words_list):
        # convert amount pattern to abrabic
        roman_nums = []
        # print(galactic_words_list)
        for item in galactic_words_list:
            if item in self.words_book:
                
                roman_nums.append(self.words_book[item])
                # print(roman_nums)
            else:
                print('Error amount pattern', item)
                return None
        # ''.Join -> Concatenate any numbres of string 
        return RomanNumerals.to_arabic(''.join(roman_nums))

    def learning_data(self, galactic_words, prices_messages):
        error_messages = []
        # in case of error
        error_messages.extend(self.build_words_book(galactic_words))
        error_messages.extend(self.build_prices_book(prices_messages))
        return error_messages

    def answer_questions(self, questions):
        # answer the questions
        answers = []
        for item in questions:

            # how much is pish tegj glob glob ?
            if 'how much is' in item:
                                                        #  pish tegj glob glob
                answer_num = self.translate_to_arabic(item.split()[3:-1])

                answers.append(" ".join(item.split()[3:-1]) + ' is ' + str(answer_num))
                # pish tegj glob glob is 42

            # how many Credits is glob prok Silver ?
            elif 'how many Credits' in item:

                metal_name = item.split()[-2]
                                                        # glob prok
                amount = self.translate_to_arabic(item.split()[4:-2])

                if amount is not None and metal_name in self.prices_book:
                    
                    price = int(amount * self.prices_book[metal_name])

                    answers.append(" ".join(item.split()[4:-1]) + ' is ' + str(price) + ' Credits')
                    # glob prok Silver is 68 Credits
                else:
                    answers.append(self.default_answer + ": " + " ".join(item.split()[4:-1]))
            else:
                answers.append(self.default_answer)
        return answers