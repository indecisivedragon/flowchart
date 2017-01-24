'''
Created on Jan 16, 2017

@author: Liming
'''
from src.Section import Section
import json

x = Section('test.txt')
x.print()

print ("hello this is a test")

with open("Data/test.txt", 'r') as f:
    content = f.read()
    '''print(content) '''
    myobj = json.loads(content)
    print(myobj["hardware"]["secondary"])


''' 
modules
- user identification
- data types + checklist

'''
