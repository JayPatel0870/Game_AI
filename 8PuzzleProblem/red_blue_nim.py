import math
import sys

class Node:
    def __init__(self,move,marbles):
        self.move = move
        self.marbles = marbles

    def get_children(self):
        marbles_red = {}
        marbles_red['red'] = self.marbles['red']-1
        marbles_red['blue'] = self.marbles['blue']
        self.red_child  = Node(move='red',marbles=marbles_red)
        marbles_blue = {}
        marbles_blue['red'] = self.marbles['red']
        marbles_blue['blue'] = self.marbles['blue']-1
        self.blue_child = Node(move='blue',marbles=marbles_blue)

        self.children = [self.red_child,self.blue_child]
        return self.children

    def leaf_score(self):
        return -(self.marbles['red']*2 + self.marbles['blue']*3)

    def stop_play(self):
        if (self.marbles['red']<=0 or self.marbles['blue']<=0):
            return True
        return False

def minimax(node, alpha, beta, maximizingPlayer):
    if node.stop_play():
        return node.leaf_score()

    if maximizingPlayer:
        max_value = -math.inf
        for child in node.get_children():
            child.value = minimax(child,alpha,beta,False)
            max_value = max(max_value,child.value)
            alpha = max(alpha, child.value)
            if beta <= alpha:
                break
        return max_value
    else:
        min_value = math.inf
        for child in node.get_children():
            child.value = minimax(child, alpha, beta, True)
            min_value = min(min_value,child.value)
            beta = min(beta, child.value)
            if beta <= alpha:
                break
        return min_value

def minmaxfunc(blue,red):
    marbles = {'red':red,'blue':blue}
    node = Node(move='root',marbles=marbles)
    minmax_val = minimax(node, alpha=-math.inf, beta=math.inf, maximizingPlayer=True)
    for child in node.children:
        if child.value == minmax_val:
            move = child.move
    return move

def user_move():
    move = input("Pick blue or red: ")
    return move

def display_stack(red,blue,turn):
    print("\nTurn:",turn)
    print(f"Stack:: red: {red}  blue: {blue}\n")

def print_winner(winner,red,blue):
    print("\n################################################\n")
    print(f"Winner: {winner}, score: {red*2+blue*3}")
    print("\n################################################\n")

red = int(sys.argv[1])
blue = int(sys.argv[2])
player = sys.argv[3]

display_stack(red,blue,player)

while blue != 0 and red != 0:
    if player == 'computer':
        move = minmaxfunc(blue,red)
        print(f"Move: {move}")
        if move == 'red':
            red -= 1
        elif move == 'blue':
            blue -= 1
        player = 'human'
    else:
        move = user_move()
        while move.lower() not in ['red','blue']:
            move = user_move()
        if move.lower() == 'blue':
            blue -= 1
        else:
            red  -= 1
        player = 'computer'

    display_stack(red,blue,player)
print_winner(player,red,blue)
