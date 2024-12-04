#!/usr/bin/env python3

class MyString:
  def __init__(self,value):
    self.value = value 
  
  #get the value
  @property
  def value(self):
      return self._value 
      
  #set the value property to value 
  #class verify that value is a string 
  @value.setter 
  def value(self,value = ""):
    if isinstance(value,str):
      self._value = value 
    else:
      print("The value must be a string.")
    
  def is_sentence(self,value):
    #sets the value true if value ends in period and false using the endswith method of dir(str)
    return self.value.endswith(".")
    
  
#print(dir(str)) # method string.endswith
  
  def is_question(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
    count = self.value.count("3") 

  

#   print(dir(str))
    

    
  
