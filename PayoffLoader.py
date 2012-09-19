#!/usr/bin/env python
import xml.etree.cElementTree as et 
import ast
   
#parse the song information
def ParseFloats( stringData ):
    floats = [float(x) for x in stringData.split()]
    return floats
    
#Loads the agent data
class PayoffLoader:
    def __init__(self): 
        self.loaded = False 
     
     #load agent data from xml file, store as agent list      
    def LoadPayoff(self):
        
        '''
        self.payoff_matrix = {
              ("R", "P"): (0, 1),
              ("P", "S"): (0, 1),
              ("S", "R"): (0, 1) }
        '''
   
        #payoff matrix
        self.payoff_matrix = {}
        
        inFile = "RPS.xml" 
        tree = et.parse(inFile) #etree.parse() opens and parses the data        
    
        payoff_matrix = {}
        #get agent item from xml
        for el in tree.findall('payoff'):
            for ch in el.getchildren(): 
                str = ch.text
                str = str.replace("\n", "")
                str = str.replace(" ", "")
                self.payoff_matrix = ast.literal_eval(str)

     
        return self.payoff_matrix
      

 