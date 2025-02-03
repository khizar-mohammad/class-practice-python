#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class OutputString:
  species = "word"
  def __init__(self):
    self.text = ''
  def InputText(self):
    self.text = input()
  def PrintString(self):
    return self.text.upper()

if __name__== "__main__":
  test = OutputString()
  print("This is a " + test.species)
  test.InputText()
  textUpper = test.PrintString()
  print(textUpper)

