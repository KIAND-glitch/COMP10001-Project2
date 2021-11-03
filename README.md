# COMP10001-Project2

Project 2 for foundations of Computing required implementing a player participating in a new type of card game tournament, and marks for this assignment were giving based on how the program performed in comparisions to other students programs participating in the tournament.

The project was built around 4 questions which required functions, which provided us with a step by step build up for the game.

The included calculating score, checking for valid table, checking if a particular play was valid and finally to put the game together a play function which allowed the player to participate in the tournament.

```
>>> comp10001huxxy_score([])
0
>>> comp10001huxxy_score(['AC'])
1
>>> comp10001huxxy_score(['4C', '2H', 'KS'])
19
```

```
>>> comp10001huxxy_valid_table([])
True
>>> comp10001huxxy_valid_table([['AC']])
False
>>> comp10001huxxy_valid_table([['AC', '2S']])  # run too short
False
>>> comp10001huxxy_valid_table([['AC', '2S', '3H']]) # run doesn't alternate in colour
False
>>> comp10001huxxy_valid_table([['AC', '2S', '4H']]) # values not adjacent
False
>>> comp10001huxxy_valid_table([['AC', '2H', '3S']])
True
>>> comp10001huxxy_valid_table([['3C', 'AS', '2H']]) # test unsorted run
True
>>> comp10001huxxy_valid_table([['0C', 'JH', 'QS', 'KH', '9D']])
True
>>> comp10001huxxy_valid_table([['2C', '2H']]) # n-of-kind too short
False
>>> comp10001huxxy_valid_table([['2C', '2H', '2C']]) # same suit twice for 3-of-kind
False
>>> comp10001huxxy_valid_table([['2C', '2H', '2S', '2C']]) # same suit twice for 4-of-kind
False
>>> comp10001huxxy_valid_table([['2C', '2H', '2S']])
True
>>> comp10001huxxy_valid_table([['2C', '2H', '2S', '2D']])
True
>>> comp10001huxxy_valid_table([['2C', '2H', '2S', '2D', '2S']])
True
>>> comp10001huxxy_valid_table([['2C', '2H', '2S', '2D', '2S'], ['0D', '9C', '8H']])
True
```

```
>>> comp10001huxxy_valid_play((0, 0, None), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
True
>>> comp10001huxxy_valid_play((0, 1, ('KC', 0)), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
True
>>> comp10001huxxy_valid_play((0, 1, ('KC', 1)), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
False  # invalid group no.
>>> comp10001huxxy_valid_play((0, 1, ('AC', 0)), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
False  # can't play card you don't hold
>>> comp10001huxxy_valid_play((0, 1, ('KH', 0)), [(0, 1, ('KC', 0))], 0, ['3S', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [['KC']])
True
>>> comp10001huxxy_valid_play((0, 1, ('KD', 0)), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C', 'KD'], [['KC', 'KH']])
True
>>> comp10001huxxy_valid_play((0, 2, ('KS', 1, 0)), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C', 'KD'], [['KC', 'KH']])
False  # group/card don't exist
>>> comp10001huxxy_valid_play((0, 3, None), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0)), (0, 1, ('KD', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C'], [['KC', 'KH', 'KD']])
True
>>> comp10001huxxy_valid_play((0, 3, None), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
False  # attempt to end turn without any plays to table
>>> comp10001huxxy_valid_play((0, 3, None), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C', 'KD'], [['KC', 'KH']])
False  # table state not valid
>>> comp10001huxxy_valid_play((0, 3, None), [(0, 1, ('AC', 0)), (0, 1, ('AH', 0)), (0, 1, ('AD', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C'], [['AC', 'AH', 'AD']])
False  # insufficient points for opening turn
>>> comp10001huxxy_valid_play((0, 1, ('KS', 0)), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0)), (0, 1, ('KD', 0)), (0, 3, None), (1, 0, None), (2, 0, None), (3, 0, None), (0, 0, None), (1, 0, None), (2, 0, None), (3, 0, None)], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C', 'KS'], [['KC', 'KH', 'KD']])
True
>>> comp10001huxxy_valid_play((0, 3, None), [(0, 1, ('KC', 0)), (0, 1, ('KH', 0)), (0, 1, ('KD', 0)), (0, 3, None), (1, 0, None), (2, 0, None), (3, 0, None), (0, 0, None), (1, 0, None), (2, 0, None), (3, 0, None), (0, 1, ('KS', 0))], 0, ['3S', '8C', '3S', '8S', '4H', '2C', '6S', '5H', '8C'], [['KC', 'KH', 'KD', 'KS']])
True
>>> comp10001huxxy_valid_play((1, 0, None), [], 0, ['3S', 'KC', '8C', '3S', '8S', 'KH', '4H', '2C', '6S', '5H', '8C', 'KD'], [])
False  # wrong player
```

```
>>> comp10001huxxy_play([(0, 1, ('KC', 0)), (0, 1, ('KC', 0)), (0, 1, ('KS', 0)), (0, 1, ('KH', 0)), (0, 1, ('KD', 0))], 0, ['3S', '8S', '4H', '2C', '6S', '5H', '8C'], [['KC', 'KC', 'KS', 'KH', 'KD']])
(0, 3, None)
```

# Result

Final Mark - 80 %
