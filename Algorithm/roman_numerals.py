class RomanNumerals:
    CURRENCY = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    @staticmethod
    def to_arabic(symbols):
        """
        Convert roman numerals to arabic numbers:
        Numbers are formed by combining symbols together and adding the values. 
        For example, MMVI is 1000 + 1000 + 5 + 1 = 2006. Generally, symbols are 
        placed in order of value, starting with the largest val
        ues. When smaller 
        values precede larger values, the smaller values are subtracted from the 
        larger values, and the result is added to the total. For example 
        MCMXLIV = 1000 + (1000 − 100) + (50 − 10) + (5 − 1) = 1944.
        """
        # print(symbols)
        numbers = [ RomanNumerals.CURRENCY[s] for s in symbols  ]
        #print(numbers)
        # print(type(numbers))
        

        for i in range(len(numbers)-1):
            
            if numbers[i] < numbers[i+1]:
                
                numbers[i] = -numbers[i]

        
        return sum(numbers)