 
 #template from David massad
 
from Constants import *
import random

class Player(object):
 
    '''
    Base class for the game player.
    '''

    def __init__( self ):
        #opponents last choice
        self.lastChoice = []
        return

    def go(self):
        '''
        Make a move.
        '''
        pass
    
    def receive_score(self, score):
        '''
        Get round result.
        '''
        pass
    
    def LastOpponentChoice(self, action):
        self.lastChoice.append(action)

class StupidPlayer(Player):
    '''
    A player which picks a given action and then plays it always.
    '''

    def __init__( self ):
        Player.__init__(self)
        randNum = random.randint(0, 2)
        self.action =  CHOICES[randNum]
        return
    
    def go(self):
        
        return self.action

 

class RandomPlayer(Player):
    '''
    A player who acts randomly every move.
    '''

    def __init__( self ):
        Player.__init__(self)
        return

    def go(self):
        '''
        Pick an action at random.
        '''
        randNum = random.randint(0, 2)
        action =  CHOICES[randNum]
     
        return action
 


#tit for tat player
class TitforTatPlayer(Player):
    '''
     does last one's move
    '''

    def __init__( self ):
         Player.__init__(self)
         return
         
    def go(self):
     
        if len(self.lastChoice) == 0:
            return CHOICES[0]
    
        action = self.lastChoice[-1]
        return action

   




#sequence player
class SequencePlayer(Player):
    '''
     plays the same sequence over and over
    '''
    def __init__( self ):
        Player.__init__(self) 
        self.location = 0
        self.sequence = []
        #choose random  list
        for i in range(0,5):
            self.sequence.append(CHOICES[random.randint(0, 2)])
         
    def go(self):
        '''
        Do the sequence list
        '''
        self.location += 1
        if self.location >= len(self.sequence):
            self.location = 0
            
        action =  self.sequence[self.location]
     
        return action
 



#human player
class HumanPlayer(Player):
    '''
     you are the player
    '''
    def __init__( self ):
        Player.__init__(self) 
        self.location = 0
        self.sequence = []
        #choose random  list
        for i in range(0,5):
            self.sequence.append(CHOICES[random.randint(0, 2)])
         
    def go(self):
       
        while True:
            var = raw_input("Enter R, P, or S: ")
            if var == "R" or var == "P" or var == "S":
                action =  var
                break
     
        return action 
    
    
    #machine learning player
class MachineLearningPlayer(Player):
    '''
     plays based on probability distribution, some help from jsbueno
    '''
    def __init__( self ): 
        self.opponentPlays = [('R',.01), ('P',.01), ('S',.01)]
        return
         
    #get the last opponent choice
    def LastOpponentChoice(self, action):
      
       tupleList = []
       for item, probality in self.opponentPlays:
            if action == item:
                probality += .01
            tupleList.append((item,probality))
            
       self.opponentPlays = tupleList
       
    #sum total probabilities
    def w_choice(self, seq):
        
        total_prob = sum(item[1] for item in seq)
        chosen = random.uniform(0, total_prob)
        cumulative = 0
    
        #get total probability and determine if next in 
        #line has cumulative more than random value
        for item, probality in seq:
            cumulative += probality
            if cumulative > chosen:
                return item
                
    def go(self):
  
        item = self.w_choice(self.opponentPlays)
        return item   

    '''
 
     
    
    (optional for beginners)
    
    MLPlayer -- uses simple machine learning to estimate probability of next move
    
    MarkovPlayer -- uses Markov processes to estimate sequence of moves for the opponent    
    '''