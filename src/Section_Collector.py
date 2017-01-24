'''
Created on Jan 17, 2017

@author: Liming
'''
from src.Section import Section
from src.Data_Source import Data_Source

# generates questions for each section and stores responses
class Section_Collector:
	
	# read in the current thing we're asking about
	def __init__(self, filename):
		# read in data types from the source file for questioning
		with open(filename, 'r') as f:
			content = f.readlines()
			self.section = Section(content[0].strip())
		# self.section.print()
		for i in range(1, len(content)):
			self.section.add_data_source(Data_Source(content[i].strip()))
		# self.section.print()
	
	def ask_section(self):
		ask_user = "Is " + self.section.get_name() + " data collected?\n"
		if self._ask_boolean(ask_user):
			for i in self.section.subsections:
				self._ask_subsection(i)
		self.section.print()
	
	# set subsection (ex: individual hardware data) responses
	def _ask_subsection(self, current):
		ask_user = "Is " + current.data_type + " " + self.section.name + " data collected?\n"
		response = self._ask_boolean(ask_user)
		if response:
			ask_user_direct = "...directly?"
			if (self._ask_boolean(ask_user_direct)):
				current.set_direct(True)
			else:
				current.set_direct(False)
			
			ask_user_indirect = "...by a third party?"
			if (self._ask_boolean(ask_user_indirect)):
				if self._ask_boolean("known?"):
					third_party = self._ask_string("name of third party?")
					current.set_indirect(True, third_party)
				else:
					current.set_indirect(True)
			else:
				current.set_indirect(False)
	
	# input validation
	def _ask_boolean(self, q_str):
		while (1):
			response = input(q_str)
			if response == "y":
				return True
			elif response == "n":
					return False
			else:
				print("bad input")				
				
	def _ask_string(self, q_str):
		return input(q_str)
	
	# write to file
	def store_responses(self, folder):
		json_obj = self.section.json_encode()
		filename = folder + "/" + self.section.name + "_responses.txt"
		f = open(filename, "w")
		f.write(json_obj)
	
if __name__ == '__main__':
	example = Section_Collector("Data/section_location.txt")
	example.ask_section()
	print(example.section.json_encode())
	example.store_responses()
# 	
# 	print("hello")
# 	f = open("section_responses.txt", "r")
# 	obj = f.read()
# 	example = Section.json_decode(obj)
# 	example.print()
	