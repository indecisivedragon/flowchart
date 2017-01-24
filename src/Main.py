'''
Created on Jan 17, 2017

@author: Liming
'''

from src.Section_Collector import Section_Collector

if __name__ == '__main__':
    question_block = Section_Collector("Questionnaire_Data/section_hardware.txt")
    question_block.ask_section()
    f = open("section_json", "w")
    f.write(question_block.section.json_encode())