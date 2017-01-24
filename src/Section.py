'''
Created on Jan 16, 2017

@author: Liming
'''
from src.Data_Source import Data_Source
import json

class Section:
    # each section contains subsections which are Data_Source types
    def __init__(self, name):
        self.name = name
        self.subsections = []
    
    def add_data_source(self, data_source):
        self.subsections.append(data_source)
    
    def to_string(self):
        output_title = "Section " + self.name + "\n"
        output = "\n".join(i.to_string() for i in self.subsections)
        return output_title + output
    
    def print(self):
        print(self.to_string())
    
    def get_section_display_stripped(self):
      display = self.name + "\n"
      display = display + "".join(i.display_format_stripped() for i in self.subsections)
      return display
        
    
    def get_size(self):
        return len(self.subsections)
    
    def get_name(self):
        return self.name
    
    # encodes Section object into json
    def json_encode(self):
        data = {}
        data["name"] = self.name

        # manually add all the Data_Source objects in subsection array because apparently __dict__ doens't do that recursively
        subdata = {}
        for i in self.subsections:
            subdata[i.data_type] = i.json_encode()
            
        data["subsections"] = subdata
        return json.dumps(data)
    
    # reconstructs a Section object from json
    @staticmethod
    def json_decode(json_obj):
        sec_reconstruct = json.loads(json_obj)
        section = Section(sec_reconstruct["name"])
        
        # reconstruct subsections list
        subdata = sec_reconstruct["subsections"]
        for i in subdata:
            current_data_source = Data_Source.json_decode(subdata[i])
            # current_data_source.print()
            section.add_data_source(current_data_source)
        return section
    
#     def __init__(self, txt_file):
#         line = 1
#         with open(txt_file, 'r') as f:
#             content = f.readline()
#             if (line == 1):
#                 self.section_name = content
#                 line = 2
#         return

if __name__ == '__main__':
    test_section = Section("HARDWARE")
    
    data_source_inputs = []
    camera = Data_Source("camera")
    camera.set_direct(True)
    data_source_inputs.append(camera)
    
    microphone = Data_Source("microphone")
    microphone.set_indirect(True, "wally")
    data_source_inputs.append(microphone)
    
    accelerometer = Data_Source("accelerometer")
    accelerometer.set_indirect(True)
    data_source_inputs.append(accelerometer)
    
    gyroscope = Data_Source("gyroscope")
    gyroscope.set_direct(True)
    gyroscope.set_indirect(True, "bob")
    data_source_inputs.append(gyroscope)
    
    clock = Data_Source("clock")
    data_source_inputs.append(clock)
    
    for i in data_source_inputs:
        test_section.add_data_source(i)
    
    test_section.print()
    
    json_obj = test_section.json_encode()
    print(json_obj)
    
    print("DECODE TEST")
    test_decode = Section.json_decode(json_obj)
    test_decode.print()
    
    print(test_decode.get_section_display_stripped())