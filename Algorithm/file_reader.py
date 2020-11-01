"Funtion for read input file"

def read_file(input_file):
    """
        read the file contents and split them into 3 modules:
        galactic_words: glob is I
        price_messages: glob glob Silver is 34 Credits
        questions: how much is pish tegj glob glob ?
        error_messages: not understandable messages
    """
    galactic_words=[]
    price_messages=[]
    questions=[]
    error_messages=[]

    info={'galactic_words':galactic_words,
          'price_messages':price_messages,
          'questions':questions, 
          'error_messages':error_messages}

    with open(input_file) as f:
        for line in f:
            # separate messages into galactic_words, price_messages and questions
            message = line.strip()
            # for test
            split_message = message.split()
            if split_message[-1] == '?':
                questions.append(message)
            elif split_message[-1] == 'Credits' and 'is' in message:
                price_messages.append(message)
            elif split_message[-1] in 'IVXLCDM' and 'is' in message:
                galactic_words.append(message)
            else:
                error_messages.append(message)

    return info



