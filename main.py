import sys
import os

from file_reader import read_file
from merchant_robot import MerchantRobot

DEFAULT_ANSWER = "I have no idea what you are talking about"

def learn_and_answer(input_file):
    info = read_file(input_file)
    error_messages = info['error_messages']
    
    
    if len(info['galactic_words']) > 0:
        # init the robot with default answer
        robot = MerchantRobot(DEFAULT_ANSWER)

        # build the robot's galactic words book
        result = robot.learning_data(info['galactic_words'], info['price_messages'])
        if result:            
            error_messages.extend(result)
            
        # use to robot to answer questions
        result = robot.answer_questions(info['questions'])
        if result:
            print("\n".join(result))
        if error_messages:
            print("\n".join(error_messages))
    else:
        print("no ref words found")

if __name__ == '__main__':
    input_file = 'input.txt'    
    learn_and_answer(input_file)