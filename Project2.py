# Question 1
def comp10001huxxy_score(cards):
    ''' takes a list of cards held by the player and returns the combined score
     of all the cards based on the value of each card as an integer '''
    
    # returns 0 if the list of cards are empty else will return the sum of all
    # cards in the list
    if not cards:
        return 0
    
    s = 0  # to store the sum of the card values in the list
    
    for each_card in cards:
        if each_card[0] in 'AJQK':
            if each_card[0] == 'A':
                s += 1
            elif each_card[0] == 'J':
                s += 11
            elif each_card[0] == 'Q':
                s += 12 
            else:
                s += 13
        elif each_card[0] in '23456789':
            s = s + int(each_card[0])
        elif each_card[0] == '0':
            s += 10
        else:
            s += 0
   
    return s

# Question 2

def comp10001huxxy_valid_table(groups):
    '''takes a list of lists of card groups and returns True if they are valid
    groups of RUN type or N OF A KIND type, else it returns false'''
    
    # list to store all the validity of all the individual groups present in 
    # the list of groups
    truth_table=[]
    
    # returns True if the list groups is empty as that is a valid
    # table state
    if not groups:
        return True
    
    # if groups is not empty, to check the validity of each list of cards
    # present in groups and store it in truth_table
    for group in groups:
        
        if len(group) < 3:
            # using lazy evaluation to determine if the entered groups are
            # valid by checking if the  length of any group is less than 3
            return False
            
        else:
            # check  for N of kind groups
            
            same_value_count = 0  # counts the cards of same value
            same_suit = 0  # checks if 2 or more exact same cards are present 
            
            # dictionary to store the suits and the number of times 
            # they are present
            suits = {}
            
            for cards in group:
                
                if cards[0] == group[0][0]:
                    # checks if the cards are of the same value
                    same_value_count += 1
                    
                if cards[1] not in suits:
                    # adds the suit of the card if it is not already present
                    suits[cards[1]]=1
                    
                elif cards[1] in suits:
                    # if the suit is already present the increases the count of 
                    # it by one
                    same_suit += 1
            
            if (same_value_count >= 3 and 
                (same_suit == 0 or len(suits.keys()) > 3)):
                truth_table.append(True)
                
            else:
                
                # check for run i.e continuous sequence in terms of value and 
                # alternating in colour 

                # assigns value to cards and stores them in a dictionary
                card_values={}
                for cards in group:
                    if cards not in card_values:
                        card_values[cards]=[]

                for key in card_values.keys():

                    if key[0] in 'AJQK':
                        if key[0] == 'A':
                            card_values[key].append(1)
                        elif key[0] == 'J':
                            card_values[key].append(11)
                        elif key[0] == 'Q':
                            card_values[key].append(12) 
                        else:
                            card_values[key].append(13)
                    elif key[0] in '123456789':
                        card_values[key].append(int(key[0]))
                    elif key[0] is '0':
                        card_values[key].append(10)
                
                # sorts the cards based on value
                sorted_list_of_card_values = []
                for value in card_values.values():
                    sorted_list_of_card_values.append(value)
                sorted_list_of_card_values.sort()

                sorted_card_values = {}
                for el in sorted_list_of_card_values:
                    for key, value in card_values.items():
                        if value == el:
                            sorted_card_values[key] = value[0]
                
                
                # check if cards are continuous
                
                # cont list stores True if two consequtive elements are 
                # continuous in a list else stores false
                cont = [] 
                
                # cont_value stores the value of the first card in the sorted
                # list and will be incremented by one in the for loop
                # to check for consequtive card values
                cont_value = sorted_list_of_card_values[0][0]
                
                for value in sorted_card_values.values():
                    if value == cont_value:
                        cont.append(True)
                    # using lazy evaluation to return False if Run type 
                    # is invalid
                    else:
                        return False
                    cont_value += 1
                
                # check for alt colours
                color_value = []  # stores the color values of each card
                for key in sorted_card_values.keys():
                    
                    if key[1] in 'HD':
                        color_value.append('RED')
                    else:
                        color_value.append('BLACK')
                # color list stores True if the color of consequtive cards 
                # is different
                color = []
                for i in range(0, len(color_value) - 1):
                   
                    if color_value[i] != color_value[i + 1]:
                        color.append(True)
                    # using lazy evaluation to return False if Run type 
                    # is invalid
                    else:
                        return False
                
                truth_table.append(True)
              
    for valid_states in truth_table:
        if not valid_states:
            return False
            
    return True    
   

# Question 3                 
            
# DO NOT DELETE/EDIT THIS LINE OF CODE, AS IT IS USED TO PROVIDE ACCESS TO
# THE FUNCTIONS FROM THE PREVIOUS QUESTION
from hidden import comp10001huxxy_valid_table

def comp10001huxxy_score(cards):
    ''' takes a list of cards held by the player and returns the combined score
     of all the cards based on the value of each card as an integer ''' 
    
    # returns 0 if the list of cards are empty else will return the sum of all
    # cards in the list    
    if not cards:
        return 0
    s = 0  # to store the sum of the card values in the list
    for each_card in cards:
        if each_card[0] in 'AJQK':
            if each_card[0] == 'A':
                s += 1
            elif each_card[0] == 'J':
                s += 11
            elif each_card[0] == 'Q':
                s += 12 
            else:
                s += 13
        elif each_card[0] in '23456789':
            s = s + int(each_card[0])
        elif each_card[0] == '0':
            s +=10
        else:
            s += 0
    return s

def comp10001huxxy_valid_play(play, play_history, active_player, hand, table):
    ''' takes five arguments which are play, play_history, active_player, hand
    and table. play_history contains a list of 3-tuples representing 
    all the plays that have taken plave so far, active_player is an integer 
    represents the player number whose turn it is to play, hand is list of 
    cards held by the player attempting the play and table is the list of card
    groups played to the table. The play need to be checked to see if its valid 
    using the other four arguments and the functions returns True if the play
    is valid else returns false '''
    
    # storing the player_turn, play_type and play_details by extracting them 
    # play so that they can be used later
    player_turn, play_type, play_details = play[0], play[1], play[2]
    
    # checks if the active player and player match
    if player_turn == active_player:
        # checking for valid move type 0
        if play_type == 0 and play_details is None:
            # checking the last move in the play history was not of the 
            # active player
            if len(play_history) >= 1:
                if play_history[-1][0] != active_player:
                    return comp10001huxxy_valid_table(table)
            else:
                return comp10001huxxy_valid_table(table)
        # checking for valid move type 1
        elif play_type == 1:
            try:
                card = play_details[0]
                to_group = play_details[1]
                # check if card is present in hand
                if card not in hand:
                    return False
                # check if the card has to be added to a new group
                if to_group > (len(table) - 1) and to_group == len(table):
                    table.append([])
                table[to_group].append(card)
                
                for groups in table:
                    if len(groups) == 1:
                        return True
                    elif len(groups) == 2:
                        # check for n of a kind 
                        count = 0  # stores the number of same value cards
                        same_suit = 0  # stores the number of same suit cards
                        suits = {}  # stores the card suits in a dictionary

                        for cards in groups:

                            if cards[0] == groups[0][0]:
                                count += 1
                            if cards[1] not in suits:
                                suits[cards[1]] = 1
                            elif cards[1] in suits:
                                same_suit += 1
                        # returns True if cards are of the same value and 
                        # different suit
                        if (count == 2 and same_suit == 0):
                            return True
                        else:
                            return False


                    # checks for run type
                    else:
                        return comp10001huxxy_valid_table(table)
            except:
                return False

        # checks for valid play type 2
        elif play_type == 2:
            card = play_details[0]  # stores the card
            # stores the index where the card is taken form
            from_group = play_details[1]
            # stores the index of the group where the card is to be put
            to_group = play_details[2] 
            # check if both to_group and for_group exist
            if to_group <= (len(table) - 1) and from_group <= (len(table) - 1):
                # remove card from_group
                # stores the index of the table which contains the card
                i = table[from_group].index(card)    
                del table[from_group][i]
                # add card to_group
                table[to_group].append(card)
                
                return comp10001huxxy_valid_table(table)
            else:
                return False
        elif play_type == 3:
            # checks if player history is not empty so that the game can be 
            # ended if the previous moves were made by the active player
            if len(play_history) == 0:
                return False
            # if not empty
            else:
                # check if its the first play and make sure the score is 
                # atleast 24
                if len(table) == 0:
                    return False
                elif len(table) == 1:
                    # calculates the score of group
                    score=comp10001huxxy_score(table[0])
                    if score >= 24 and comp10001huxxy_valid_table(table):
                        return True
                    else:
                        return False
                else:
                    return comp10001huxxy_valid_table(table)
    else:
        return False
        
# Question 4

def less_than_six_moves(play_history, active_player):
    ''' checks if the last six moves have been made by the active player, it 
    takes the play history and active player as arguments and returns True
    if six consequtive moves have been made else returns false'''
    recent_moves = []
    if len(play_history) >= 6:
        for i in range(-6,0,1):
            if play_history[i][0] == active_player:
                recent_moves.append(play_history[i])
        if len(recent_moves) == 6:
            return True
        else:
            return False
    else:
        return False
    
def more_than_three_moves(play_history, active_player):
    ''' checks if the last six moves have been made by the active player, it 
    takes the play history and active player as arguments and returns True
    if six consequtive moves have been made else returns false'''
    recent_moves = []
    if len(play_history) >= 3:
        for i in range(-3,0,1):
            if play_history[i][0] == active_player:
                recent_moves.append(play_history[i])
        if len(recent_moves) <= 3:
            return True
        else:
            return False
    else:
        return False
    
def first_move_of_the_game(play_history, active_player):
    ''' checks if the active player has made their first move by taking the 
    play history  and active player as arguments and returns True if the first 
    move has been made else returns false '''
    play_made_by_active_player = []
    for plays in play_history:
        if plays[0] == active_player:
            play_made_by_active_player.append(plays)
    first_move_made = False
    for plays in play_made_by_active_player:
        if plays[1] != 0:
            first_move_made = True
            break
        else:
            first_move_made = False
    return first_move_made
    
def myfunc(lst):
    '''takes a list and return a list of ranges of continuos values '''
    ret = []
    a = b = lst[0]                           # a and b are range's bounds

    for el in lst[1:]:
        if el == b+1: 
            b = el                           # range grows
        else:                                # range ended
            ret.append(a if a==b else [a,b]) # is a single or a range?
            a = b = el                       # let's start again with a single
    ret.append(a if a==b else [a,b])         # corner case for last single/range
    return ret

def card_color(card):
    '''takes a card(string) as an argument and returns its color as a string'''
    if card[1] in 'HD':
         return 'RED'
    else:
         return 'BLACK'
        
def card_value(cards):
    '''takes a card(string) as an argument and returns its value as an integer'''
    if not cards:
        return None
    
    for i in cards:
        if cards[0] in 'AJQK':
            if cards[0] == 'A':
                value = 1
            elif cards[0] == 'J':
                value = 11
            elif cards[0] == 'Q':
                value = 12 
            else:
                value = 13
        elif cards[0] in '23456789':
            value = int(cards[0])
        elif cards[0] == '0':
            value =10
        else:
            value = 0
    return int(value)

def active_player_recent_moves(play_history,active_player):
    '''  takes the play history and active player number as argument and returns
    a list of all the recent moves made by the active player'''
    if (play_history != []):
        
        recent_moves_by_active_player=[]   
        last_move_number = 0
        first_move_number = 0
        for i in range(len(play_history)-1,1,-1):
            
            if play_history[i][0] == active_player:
                last_move_number = i
                   
                break
        for i in range(last_move_number,0,-1):
            if play_history[i][0] != active_player:
                
                first_move_number = i+1
                break
            else:
                first_move_number = 0

        for i in range(first_move_number, last_move_number+1):
            if play_history[i][1] not in (0,3) and play_history[i][0] == active_player:
                recent_moves_by_active_player.append(play_history[i])    

        lst=[]
        for el in recent_moves_by_active_player:
            lst.append(el[2][0])

        return lst

def sort_hand(given_list_of_cards):
    '''sorts the given list if cards passed in descending order so that every
    move made will always get rid of a card of high value card which increases 
    chance for ranking higher if the player does not win and returns a list of 
    sorted list and a dictionary of the sorted list of cards and their values'''
    cards_dd = {}
    for cards in given_list_of_cards:
        if cards not in cards_dd:
            cards_dd[cards] = [] 
                    
    for key in cards_dd.keys():
                if key[0] in 'AJQK':
                    if key[0] == 'A':
                        cards_dd[key].append(1)
                    elif key[0] == 'J':
                        cards_dd[key].append(11)
                    elif key[0] == 'Q':
                        cards_dd[key].append(12) 
                    else:
                        cards_dd[key].append(13)
                elif key[0] in '123456789':
                    cards_dd[key].append(int(key[0]))
                elif key[0] is '0':
                    cards_dd[key].append(10)
    
    lst_to_store_sorted_card_values = []
    for value in cards_dd.values():
         lst_to_store_sorted_card_values.append(value)
    lst_to_store_sorted_card_values.sort(reverse=True)
          
    sorted_cards_dd = {}
    for el in lst_to_store_sorted_card_values:
        for key,value in cards_dd.items():
            if value == el:
                sorted_cards_dd[key]=value[0]
    sorted_list = []
    for el in sorted_cards_dd.keys():
        sorted_list.append(el)
    return (sorted_list, sorted_cards_dd)

def forming_groups(given_table):
    '''check all the groups in the table determine whether a group is RUN or 
    N_OF_A_KIND and return them'''
    
    run = []  # to store the run type groups present in the table
    n_of_a_kind = []  # to store the N of a kind groups present in the table
    groups_in_formation = []  # to store the group which is yet to be completed
    
    #forms the group in formation
    for groups in given_table:
        if len(groups) < 3:
            groups_in_formation.append(groups)
    
    #forms the n of a kind group
    for groups in given_table:
        same_suit_count = 0
        same_suit = 0
        suits = {}
            
        for cards in groups:
            
            if cards[0] == groups[0][0]:
                same_suit_count += 1
            if cards[1] not in suits:
                suits[cards[1]]=1
            elif cards[1] in suits:
                suits[cards[1]]+=1
                same_suit += 1

        if (same_suit_count >= 3 and (same_suit == 0 or len(suits.keys())==4)):
            n_of_a_kind.append(groups)
    
    #forms the run group
    for groups in given_table:
        
        #assigns value to cards
        dd={}
        for cards in groups:
            if cards not in dd:
                dd[cards]=[]
        for key in dd.keys():
             dd[key].append(card_value(key))
        
        #sorts the cards based on value
        sorted_list_of_vals=[]
        for value in dd.values():
            sorted_list_of_vals.append(value)
        sorted_list_of_vals.sort()
            
        sorted_dd={}
        for el in sorted_list_of_vals:
            for key,value in dd.items():
                if value == el:
                    sorted_dd[key]=value[0]
        
        #check if cards are continuous
        cont=[]
            
        cont_value=sorted_list_of_vals[0][0]
        for value in sorted_dd.values():
                if value == cont_value:
                    cont.append(True)
                else:
                    cont.append(False)
                cont_value += 1    

        #check for alt colours
        color_value=[]
        for key in sorted_dd.keys():
                if key[1] in 'HD':
                    color_value.append('RED')
                else:
                    color_value.append('BLACK')
        
        color=[]
        for i in range(0,len(color_value)-1):
                if color_value[i] != color_value[i+1]:
                    color.append(True)
                else:
                    color.append(False)
               
        if ((False not in cont) and (False not in color) and len(groups)>=3):
                run.append(groups)
    
    return (n_of_a_kind,run,groups_in_formation)

def play_n_group(sorted_hand_dd):
    card_values = set(sorted_hand_dd.values())
    N_type = {}
    for val in card_values:
        N_type[val] = [k for k in sorted_hand_dd.keys() 
                       if sorted_hand_dd[k] == val]
    pass_values = []
    for key,value in N_type.items():
        if len(value) >= 3:
            s = 0
            if len(value) == 3 and (value[0] != value[1]
                                    and value[1] != value[2]
                                    and value[0] != value[2]):
                s = len(value) * key
            else:
                s = len(value) * key
            if s >= 24:
                pass_values.append(key)     
    n = []            
    for vals in pass_values:
        for key,value in N_type.items():
            if vals == key:
                n.append(value)
    
    return n
    
def possible_new_groups(set_of_cards,play_history, active_player):
    '''takes a set of cards as an argument and making possible groups of N
     and R type'''
    groups = []
    sorted_hand, sorted_hand_dd = sort_hand(set_of_cards)
    first_move_made = first_move_of_the_game(play_history, active_player)
    card_values = set(sorted_hand_dd.values())
    N = {}
    for value in card_values:
        N[value] = [k for k in sorted_hand_dd.keys() if sorted_hand_dd[k] == value]
     
    for key,value in N.items():
        if len(value) >= 3:
            if first_move_made:
                groups.append(value)
            else:
                s = len(value) * key
                if s >= 24:
                    groups.append(value)
            
    continuous_values = myfunc(list(set(sorted(sorted_hand_dd.values()) )))
          
    alst=[]
    for vals in continuous_values:
                if type(vals)==list :
                    if vals[0]+1 != vals[1]:
                        alst.append(vals)
            
    a=[]
    if len(alst)!=0:

        for cont in alst:
            R = []
            for i in range(cont[0], cont[1]+1):
                for key, value in sorted_hand_dd.items():
                     if i == value:
                            R.append(key)
            a.append(R)         

            
    for possible_run in a:
        for key,value in N.items():
                    if len(value) > 1:
                        a.remove(possible_run)
                        break
            
    abc=[]
    for possible_run in a:
        flag = True
        xyz=[]
        for i in range(0,len(possible_run)-1):
                    card1=possible_run[i]
                    card2=possible_run[i+1]
                    if card_color(card1) != card_color(card2) and card_value(card1) != card_value(card2):
                        xyz.append(card1)

                    else:
                        flag =False
                    if  flag == False:
                        break

        abc.append(xyz)
        
            
        pass_sum_test = []
        for group in abc:
            s=0
            for cards in group:
                s += card_value(cards)
                if first_move_made:
                    pass_sum_test.append(group)
                elif s >= 24:
                    pass_sum_test.append(group)
            
            
        if len(pass_sum_test) != 0:
            for groups_present in pass_sum_test:
                groups.append(groups_present)
                    
    return groups

def comp10001huxxy_play(play_history, active_player, hand, table):
        
        # checks if the player has played 6 moves and if yes the returns 
        # a move of play_type 3
        exceed = less_than_six_moves(play_history, active_player)
        if exceed == True:
            return (active_player, 3, None)
        
        #sort the hand on basis of descending value
        sorted_hand, sorted_hand_dd = sort_hand(hand)   
        
        #check all the groups in the table 
        #determine whether a group is RUN or N_OF_A_KIND
        #place them in separate lists
        n_of_a_kind, run, group_in_formation = forming_groups(table)    
       
        #if this is the players first move i.e play_history for that player DNE and 
        #storing the last moves made by the active player in a list
        recent_cards_by_active_player = active_player_recent_moves(play_history, active_player)   
        #return (recent_cards_by_active_player)

        # checks if its the players first move 
        first_move = first_move_of_the_game(play_history, active_player)
        
        '''playing the active_players first move of the game if groups DNE'''
        if first_move is False :            
            
            # players first move to the table and we try to play N of a kind
            card_values = set(sorted_hand_dd.values())
            N_type = {}
            for val in card_values:
                N_type[val] = [k for k in sorted_hand_dd.keys() if sorted_hand_dd[k] == val]

            n_type = play_n_group(sorted_hand_dd)
            
            if len(n_type) >= 1:
                
                return ((active_player,1,(n_type[0][0],len(table))))

            # if its the players first move and n of kind is not possible then trying 
            # run kind

            continuous_values = myfunc(list(set(sorted(sorted_hand_dd.values()) )))
          
            alst=[]
            for vals in continuous_values:
                if type(vals)==list :
                    if vals[0]+1 != vals[1]:
                        alst.append(vals)
            
            a=[]
            if len(alst)!=0:

                for cont in alst:
                    R = []
                    for i in range(cont[0], cont[1]+1):
                        for key, value in sorted_hand_dd.items():
                            if i == value:
                                R.append(key)
                    a.append(R)         

            
            for possible_run in a:
                for key,value in N_type.items():
                    if len(value) > 1:
                        a.remove(possible_run)
                        break
            
            abc=[]
            for possible_run in a:
                flag = True
                xyz=[]
                for i in range(0,len(possible_run)-1):
                    card1=possible_run[i]
                    card2=possible_run[i+1]
                    if card_color(card1) != card_color(card2) and card_value(card1) != card_value(card2):
                        xyz.append(card1)

                    else:
                        flag =False
                    if  flag == False:
                        break

                abc.append(xyz)
                
                pass_sum_test = []
                for groups in abc:
                    s=0
                    for cards in groups:
                        s += card_value(cards)
                    if s >= 24:
                        pass_sum_test.append(groups)
                      
                if len(pass_sum_test) != 0:
                    
                    return ((active_player,1,(pass_sum_test[0][0],len(table))))
            
            if len(table) != 0 and play_history[-1][0] == active_player:
                for groups in table:
                    if len(groups) > 3:

                        # checking if the last card of the group can be used to form 
                        # a new group since this card will be the highest value
                        sorted_groups_in_table,  sorted_groups_in_table_dd = sort_hand(groups)
                        last_card = sorted_groups_in_table[-1]
                        new_hand = hand
                        new_hand.append(last_card)

                        #temp_sorted_hand, temp_sorted_hand_dd = sort_hand(new_hand)
                        possible_groups = possible_new_groups(new_hand,play_history, active_player)
                        # checks if the added card to hand helps in formation of any 
                        # groups and if it does plays that card

                        # you need to check if the last card is played then can your bot 
                        # still form those groups as if the new card was initially 
                        # added in the middle
                        for a_group in possible_groups:
                            if last_card in a_group:
                                s=0
                                for c in a_group:
                                    s= s+ card_value(c)
                                if s >= 24 and play_history[-1][1]==1:    
                                    return (active_player, 2, (last_card, table.index(groups),len(table)))

                        first_card = sorted_groups_in_table[0]
                        new_hand.remove(last_card)
                        new_hand.append(first_card)
                        possible_groups = possible_new_groups(new_hand, play_history, active_player)
                        # checks if the added card to hand helps in formation of any 
                        # groups and if it does plays that card

                        # you need to check if the last card is played then can your bot 
                        # still
                        for a_group in possible_groups:
                            if first_card in a_group:
                                s=0
                                for c in a_group:
                                    s= s+ card_value(c)
                                if s >= 24 : 
                                    if play_history[-1][1]==1 and play_history[-1][0]==active_player:
                                        return (active_player, 2, (first_card, table.index(groups), len(table)))                     

            
            
            #if no move is possible,the draw a card after adding card to hand

            return (active_player,0,None)

        ''' playing the immediate next move when the len(group_in_formation) < 3 '''
        if len(group_in_formation) != 0:
           
            if len(group_in_formation[0]) == 1:
                #check if the N group can be formed

                count = 0
                s = card_value(group_in_formation[0][0])
                for cards in sorted_hand:
                    if card_value(group_in_formation[0][0]) == card_value(cards) and group_in_formation[0][0] != cards:
                        count += 1
                        s += card_value(cards)
                for cards in sorted_hand:
                    if card_value(group_in_formation[0][0]) == card_value(cards) and count >= 2 and s >= 24:
                        return (active_player, 1, (cards, table.index(group_in_formation[0])))
                
                #check if the Run group can be formed
                #always the highest possible value will be played in my game
                high_value=card_value(group_in_formation[0][0]) + 1
                higher_value = card_value(group_in_formation[0][0]) + 2
                ss = card_value(group_in_formation[0][0])
                for i in range(0,len(sorted_hand)-1):
                    card1 = sorted_hand[i]
                    card2 = sorted_hand[i+1]
                    if higher_value == card_value(card1) and high_value == card_value(card2):
                        ss = ss + high_value + higher_value
                        if ss >= 24  and card_color(card2) != card_color(group_in_formation[0][0]):
                            return (active_player, 1, (card2, table.index(group_in_formation[0])))

            #if len is 2    
            else:

                s = card_value(group_in_formation[0][0]) + card_value(group_in_formation[0][1])      

                for cards in sorted_hand:
                    #N group
                    if card_value(group_in_formation[0][0]) == card_value(cards) and card_value(group_in_formation[0][1]) == card_value(cards):
                        if cards != group_in_formation[0][0] and cards != group_in_formation[0][1]:
                            s += card_value(cards)
                            if s >=24:
                                return (active_player, 1, (cards, table.index(group_in_formation[0])))
                    #Run group
                    else:
                        card1 = group_in_formation[0][0]
                        card2 = group_in_formation[0][1]

                        if card_value(card1)+2 == card_value(cards) and card_value(card2)+1 == card_value(cards):

                            if card_color(card1) == card_color(cards) and card_color(card2) != card_color(cards):

                                s = s + card_value(cards)
                                if s >= 24 :
                                        return (active_player, 1, (cards, table.index(group_in_formation[0])))

        #if it isnt the players first move in the game the group all the cards played
        #by the active_player before he ends his turn
        '''playing a new move which is not the first move of the game '''
    
        #checking all the N groups and playing a card to an existing N group
        if len(n_of_a_kind) != 0 :
            for groups in n_of_a_kind:
                for cards in sorted_hand:
                    if cards[0] == groups[0][0]:
                        if len(groups)>=4:
                            return (active_player, 1, (cards, table.index(groups)))
                        else:
                            #need to check if the move would be valid
                            flag=True
                            for cards_n in groups:
                                if cards_n[1] == cards[1]:
                                    flag = False
                            if flag == True:
                                return (active_player, 1, (cards, table.index(groups)))

        
        # checking all the R groups and playing a card to existing R group
        if len(run) != 0:
            print(run)
            for groups in run:
                #get the highest and lowest value cards in the group
                #assumption made: cards in groups on table will always be sorted 
                low_value = card_value(groups[0])
                low_value_color = card_color(groups[0])
                high_value = card_value(groups[len(groups)-1])
                high_value_color = card_color(groups[len(groups)-1])
                lower_value = low_value + 1
                higher_value = high_value - 1
                print(lower_value,low_value_color)
                #search for a card lower or higher card in your sorted hand 
                lst_values = []
                for cards in groups:
                    lst_values.append(card_value(cards))
                for cards in hand:
                    print(cards,card_value(cards),card_color(cards))
                    if higher_value == card_value(cards) and card_color(cards) != high_value_color:
                        if card_value(cards) not in lst_values:
                            return (active_player, 1, (cards, table.index(groups)))
                    elif lower_value == card_value(cards) and  card_color(cards) != low_value_color:
                        if card_value(cards) not in lst_values:
                            return (active_player, 1, (cards, table.index(groups)))

    #For creating a new group, consider cases of taking cards from RUN or 
    #N_OF_A_KIND to create the group'''
        if len(table) != 0:
            for groups in table:
                if len(groups) > 3 and play_history[-1][1]==1 and play_history[-1][0]==active_player:
                    
                    # checking if the last card of the group can be used to form 
                    # a new group since this card will be the highest value
                    sorted_groups_in_table,  sorted_groups_in_table_dd = sort_hand(groups)
                    last_card = sorted_groups_in_table[-1]
                    new_hand = hand
                    new_hand.append(last_card)
                    
                    possible_groups = possible_new_groups(new_hand,play_history, active_player)
                    # checks if the added card to hand helps in formation of any 
                    # groups and if it does plays that card

                    for a_group in possible_groups:
                        if last_card in a_group and more_than_three_moves(play_history, active_player) :
                            return (active_player, 2, (last_card, table.index(groups),len(table)))
                    
                    # checking if the first card of the group can be used to form 
                    # a new group since this card will be the highest value
                    first_card = sorted_groups_in_table[0]
                    new_hand.remove(last_card)
                    new_hand.append(first_card)
                    possible_groups = possible_new_groups(new_hand,play_history, active_player)
                    
                    for a_group in possible_groups:
                        if first_card in a_group and more_than_three_moves(play_history, active_player):
                            return (active_player, 2, (first_card, table.index(groups), len(table)))

                    # checks if cards can be added to existing n of a kind groups
                    if len(n_of_a_kind) != 0 :
                        for n_groups in n_of_a_kind:
                            if n_groups != groups:
                                if last_card[0] == n_groups[0][0]:
                                    if len(groups)>=4:
                                        return (active_player, 2, (last_card, table.index(groups), table.index(n_groups)))
                                elif first_card[0] == n_groups[0][0]:
                                    if len(groups)>=4:
                                        return (active_player, 2, (first_card, table.index(groups), table.index(n_groups)))                                
                    
                    # checks if cards can be added to existing run groups
                    if len(run) != 0:
                        print(run)
                        for r_groups in run:
                            #get the highest and lowest value cards in the group
                            #assumption made: cards in groups on table will always be sorted 
                            low_value = card_value(r_groups[0])
                            low_value_color = card_color(r_groups[0])
                            high_value = card_value(r_groups[-1])
                            high_value_color = card_color(r_groups[-1])
                            lower_value = low_value + 1
                            higher_value = high_value - 1
                            
                            #search for a card lower or higher card in your sorted hand 
                            lst_values = []
                            for cards in r_groups:
                                lst_values.append(card_value(cards))
                            
                            if higher_value == card_value(last_card) and card_color(last_card) != high_value_color:
                                    if card_value(last_card) not in lst_values:
                                        return (active_player, 2, (last_card, table.index(groups),table.index(r_groups)))
                            elif lower_value == card_value(last_card) and  card_color(last_card) != low_value_color:
                                    if card_value(last_card) not in lst_values:
                                        return (active_player, 2, (last_card, table.index(groups),table.index(r_groups))) 
                            elif higher_value == card_value(first_card) and card_color(first_card) != high_value_color:
                                    if card_value(first_card) not in lst_values:
                                        return (active_player, 2, (first_card, table.index(groups), table.index(r_groups)))
                            elif lower_value == card_value(first_card) and  card_color(first_card) != low_value_color:
                                    if card_value(first_card) not in lst_values:
                                        return (active_player, 2, (first_card, table.index(groups), table.index(r_groups)))                                        
                                    
        
        if len(play_history) >= 1 :
            # return play type 3 if moves of type 1 or 2 have been played    
            if (play_history[len(play_history)-1][1] != 0):
                if (play_history[len(play_history)-1][0] == active_player):
                    return (active_player, 3, None)
            # return play type 0 if no moves have been played in this turn
            if play_history[len(play_history)-1][0] != active_player: 
                return (active_player, 0 , None)        
     
   


    