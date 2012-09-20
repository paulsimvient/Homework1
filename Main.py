

from Referee import *

'''
print "StupidPlayer player game"
Ref = Referee()
Ref.add_player(StupidPlayer())
Ref.add_player(StupidPlayer())
Ref.play_game()

print "random player game"
Ref = Referee()
Ref.add_player(RandomPlayer())
Ref.add_player(RandomPlayer())
Ref.play_game()

print "SequencePlayer player game"
Ref = Referee()
Ref.add_player(SequencePlayer())
Ref.add_player(SequencePlayer())
Ref.play_game()
'''
 

print "RandomPlayer vs machine learning game"
Ref = Referee()
Ref.add_player(MarkovPlayer())
Ref.add_player(RandomPlayer())
Ref.play_game()