def item_score(item):
    score = {
        'rock': 1,
        'paper': 2,
        'scissor': 3
    }

    return score[item]

# scores based on item1 -> item2
def combat_score(item1, item2):
    if item1 == item2:
        return 3

    if (item1, item2) == ('rock', 'paper'):
        return 0
    
    if (item1, item2) == ('rock', 'scissor'):
        return 6

    if (item1, item2) == ('paper', 'scissor'):
        return 0
    
    if (item1, item2) == ('paper', 'rock'):
        return 6

    if (item1, item2) == ('scissor', 'rock'):
        return 0
    
    if (item1, item2) == ('scissor', 'paper'):
        return 6

def get_strategy_item(item, strategy):
    win_map = {
        'rock': 'paper',
        'paper': 'scissor',
        'scissor': 'rock'
    }
    lose_map = {v: k for k, v in win_map.items()}

    if strategy == 'Y': # draw
        return item

    if strategy == 'X': # lose
        return lose_map[item]
    elif strategy == 'Z': # win
        return win_map[item]

column_item_map = {
    'A': 'rock',
    # 'X': 'rock',

    'B': 'paper',
    # 'Y': 'paper',

    'C': 'scissor',
    # 'Z': 'scissor'
}

total_player_score = 0
path = './input.txt'

with open(path) as fp:
   for line in fp:
    c1, c2 = line.split()
    
    item1 = column_item_map[c1]
    item2 = get_strategy_item(item1, c2)

    player2_score = combat_score(item2, item1) + item_score(item2)
    # print(item1, item2, player2_score)
    total_player_score += player2_score

print(total_player_score)


