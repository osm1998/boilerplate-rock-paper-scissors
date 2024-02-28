import random
def player(prev_play, opponent_history=[]):
    
    counter = {"P":"S","R":"P","S":"R"}
    
    if not prev_play :
        
        prev_play = random.choice(list(counter.keys()))
    
    opponent_history.append(prev_play)
    
    guess = counter[prev_play]
    
    
    n=5
    
    if len(opponent_history)> 4 : 
    
        Combination = "".join(opponent_history) # creates a string out of the sequence of played moves
        
        
        
        possible_plays = ["".join(opponent_history[-n:] + [v]) for v in ["R","P","S"]]  # List of possible plays ( Sequence of 5 last moves + Possible Play) | number of element of the sequence was arbitrary picked and tweeked after tests to be able to beat all bots ( Found it the number that wins against all the bots in a very convincing way )
        
        proba = [Combination.count(element) for element in possible_plays] # gets How many times the same sequence happened 
        
        Probabilities_dict = {}
        
        Probabilities_dict = dict(zip(possible_plays, proba)) # creates a dict to map each sequence and how many times it h appened before 
        
        #to predict the move that can be played by the bot , we base our thinking on the simple fact that the sequence that happened the most is more probable to be played than other sequences
        
        
        
     
        if sum(proba) == 0 : 
            
            guess = random.choice(list(counter.keys()))
            
        else    :
            
            Predict_play = next(key for key, value in Probabilities_dict.items() if value == max(proba))[-1] #guets the most probable squence and gets the last element of it and that will be the element that the bot is most probable to play 
            guess = counter[Predict_play] # now we just use the counter disct to return the the mouvement that counters the mouvement the bot is probably going to play 

    
    
    return guess



