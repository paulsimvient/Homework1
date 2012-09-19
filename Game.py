
#resolve game code from David Massad

from PayoffLoader import* 
import Constants

class Game:
   

    def __init__( self ):
       
        # load payoff matrix
        loader = PayoffLoader()
        self.payoff_matrix = loader.LoadPayoff()
       

        #daves stuff
    def resolve(self, action1, action2):
        '''
        Return a payoff pair for action1, action2

        Args:
            action1: Player1 action
            action2: Player2 action
        Returns:
            (Player1 payoff, player2 payoff)
        '''
     

        return self.payoff_matrix[(action1, action2)]

 