import random
import pandas as pd

history =[]
positions={}
players=[]


def snake_ladder(grid, player):
    for i in range(1,player+1):
        players.append(f'Player{i}')
    positions = {p:0 for p in players}
    winner = None
    turn = 1

    while not winner:
        for player in players:
            roll = random.randint(1,6)
            old_pos = positions[player]
            new_pos = roll+old_pos
            
            if new_pos <= grid**2:
                
                for other in players:
                    if other != player and positions[other] == new_pos:
                        positions[other] = 0
                positions[player] = new_pos
                
            if new_pos > grid**2:
                new_pos = old_pos
            if new_pos == grid**2:
                winner = player
               
            history.append({
                'Player Number': player,
                'Dice Roll': roll,
                'Position': new_pos,
                'Winner Status': winner if winner else ''
            })
            
            turn += 1
            if winner:
                break

grid = int(input('Enter the grid size: '))
playerno = int(input('Enter the player number: '))

snake_ladder(grid, playerno)

df = pd.DataFrame(history)
print(df)
            
