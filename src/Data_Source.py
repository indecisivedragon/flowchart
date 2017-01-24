'''
Created on Jan 16, 2017

@author: Liming
'''

import json

class Data_Source:
  def __init__(self, data_type):
    self.data_type = data_type
    # app collects the data itself
    self.direct = False
    # app collects the data from a third-party provider
    self.indirect = False
    self.third_party = None

  def set_direct(self, has_direct):
    self.direct = has_direct
  
  # returns whether or not we collect data directly
  def get_direct(self):
    return self.direct
    
  def set_indirect(self, has_indirect, third_party=None):
    self.indirect = has_indirect
    if (has_indirect is True):
      if (third_party is not None):
        self.third_party = third_party
      else:
        self.third_party = "unknown"
    else:
      self.third_party = None
  
  # returns only whether indirect source exists, not name
  def get_indirect(self):
    return self.indirect
  
  # returns name of indirect source
  # will be None if none exists, or "unknown" if it exists but we don't know who
  def get_third_party(self):
    return self.third_party
  
  def to_string(self):
    output = self.data_type + " collection:"
    if (self.direct == True):
      output = output + " [app]"
    if (self.indirect == True):
      output = output + " [third party " + self.third_party + "]"
    if (self.direct == False and self.indirect == False):
      output = output + " [not collected]"
    return output
    
  def print(self):
    print(self.to_string())
  
  # show only if the data is actually being collected
  # either directly or indirectly
  def display_format_stripped(self):
    if (self.direct == True or self.indirect == True):
      return self.data_type + "\n"
    else:
      return ""
    
  # encode as a json object
  def json_encode(self):
    return json.dumps(self.__dict__)
  
  @staticmethod
  def json_decode(json_object):
    decode = json.loads(json_object)
    data_type = decode["data_type"]
    
    # create new data_source object from decoded json
    data_source_decoded = Data_Source(data_type)
    direct = decode["direct"]
    data_source_decoded.set_direct(direct)
    
    indirect = decode["indirect"]
    data_source_decoded.set_indirect(indirect, decode["third_party"])
    
    return data_source_decoded

if __name__ == '__main__':
  test_data = Data_Source("hardware")
  test_data.set_direct(True)
  test_data.set_indirect(True, "axiom")
  test_data.set_indirect(False)
  test_data.print()
  
  encode = test_data.json_encode()
  print(encode)
  # decode = json.loads(encode)
  # print(decode)
  test2 = Data_Source.json_decode(encode)
  test2.print()
  
  print(test2.get_indirect())
  print(test2.get_third_party())