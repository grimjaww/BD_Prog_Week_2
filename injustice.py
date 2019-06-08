import random

full_deck = []
graveyard = []

global player1
global player2

global number
number = 1

#global n
n = 0

#creating deck for the players respectively
class Injustice_deck:
    
    def characterStats(self, name, strength, attack, defence, health):
        self.name = name
        self.strength = strength
        self.attack = attack
        self.defence = defence
        self.health = health
        
    def showStats(self):
        return{
            "Character name" : str(self.name) , 
            "Strength" : str(self.strength) , 
            "Attack" : str(self.attack) , 
            "Defence" : str(self.defence) , 
            "HP" : str(self.health)
            }

#decides which player begins the game
def playerTurn():
    if player1.dice_roll > player2.dice_roll:
        player1.beginGame()
    elif player1.dice_roll == player2.dice_roll:
        player1.beginGame()
    else:
        player2.beginGame()

#if player 1 begins game then player 2 card is drawn here and vice versa     
def drawCard(p):
    if p == 1:
        playCard = player1.deck.pop(0)
        graveyard.append(playCard)
        return playCard
    else:
        playCard = player2.deck.pop(0)
        graveyard.append(playCard)
        return playCard

#Checks if game is completed and displays the points respectively 
def gameOver():
    if player1.gamePoint > player2.gamePoint:
        print("\n")
        print("GAME OVER")
        print("Player 1: " + player1.name + " Wins \n")
        print("Player 1 Game Points: " + str(player1.gamePoint))
        print("Player 2 Game Points: " + str(player2.gamePoint))
    elif player1.gamePoint == player2.gamePoint:
        print("\n")
        print("GAME OVER")
        print("Draw")
    else:
        print("\n")
        print("GAME OVER")
        print("Player 2: " + player2.name + " Wins \n")
        print("Player 2 Game Points: " + str(player2.gamePoint))
        print("Player 1 Game Points: " + str(player1.gamePoint))

 
def godSpell(self):
    global n
    if (self.godFlag == 0):
        print("Please choose a card number for your opponent to use\n ")
        godNumber = int(input("Select between 0 to " + len(self.deck)-1 + " to continue the game"))
        if(self.playerNumber == 1):
            player1.godFlag = 1
            print("Player 1 has played God Card, Player 2 even you can become Jesus\n Do you wish to revive the dead?")
            choice = input("If YES press 1, If you want to be a peasent press 2: ")
            if choice == 2:
                godCard = player2.deck.pop(godNumber)
                player2.insert(0,godCard)
                player1.beginGame()                       
                    
            elif ch == 1:
                a = input("Do you want player 2 to use card from graveyard or from deck, 1. Graveyard 2.Deck")
                if a == 2:
                    godCard = player2.deck.pop(godNumber)
                    player2.insert(0,godCard)
                    player1.beginGame()
                else:
                    n = 1
                    player2.ressurection()
                
                
        else:
            player2.godFlag = 1
            print("Player 2 has played God Card, Player 1 even you can become Jesus\n Do you wish to revive the dead?")
            choice = input("If YES press 1, If you want to be a peasent press 2: ")
            if choice == 2:
                godCard = player1.deck.pop(godNumber)
                player1.insert(0,godCard)
                player2.beginGame()
                
                    
            elif ch == 1:
                a = input("Do you want player 2 to use card from graveyard or from deck, 1. Graveyard 2.Deck")
                if a == 2:
                    godCard = player1.deck.pop(godNumber)
                    player1.insert(0,godCard)
                    player2.beginGame()
                else:
                    n = 2
                    player1.ressurection()
    else:
        print("God card already used, You can be God only once greedy man")
        self.beginGame()
                    
    

def ressurection(self):
    graveCard=random.randrange(0,len(graveyard)-1)
    if(self.resSpell==0):
        if(self.playerNumber==2):
            player2.cardDeck.insert(0,graveyard[graveCard])
            self.resSpell = 1
            if(n == 1):
                player1.beginGame()                  
            else:
                player2.beginGame()
        else:
            player1.cardDeck.insert(0,graveyard[graveCard])
            self.resSpell = 1
            self.beginGame()
            if(n == 2):
                player2.beginGame()                  
            else:
                player1.beginGame()
    else:
        print("Ressurection already used, Cant review the dead.. The dead stay dead!!")
        self.beginGame()
    


#Dealing cards to players
class cardDealing:
    def __init__(self):
        self.gamePoint = 0
        dice_roll = 0
        self.deck = []
        self.playerNumber = 0
        self.godFlag = 0
        self.resFlag = 0
        #godFlag = 0
        #resFlag = 0
    
    
    def createPlayer(self, name):
        global number
        self.name = name
        self.dice_roll = random.randrange(1,6)
        self.playerNumber = number
        number = number + 1

        self.godSpell = 0
        self.resSpell = 0


        

        if(self.playerNumber == 1):
            for i in range(0, len(full_deck)):
                if(i % 2 == 0):
                    self.deck.append(full_deck[i])
        else:
            for i in range(0, len(full_deck)):
                if(i % 2 != 0):
                    self.deck.append(full_deck[i])
                                 
        print("\nPlayer Name: " + str(self.name) + "\nPlayer Number: " + str(self.playerNumber) + "\nYour Dice Number is: " + str(self.dice_roll))
        #print(self.deck[0])



    def beginGame(self):
        global n
        n = n + 1
        print("Round " + str(n) + " fight!!")
        #n = n + 1
        
        if self.playerNumber == 1:
            print(player1.deck[0])
            #print(player2.deck[0])
            card1 = player1.deck.pop(0)
            graveyard.append(card1)
            card2 = drawCard(2)
        else:
            print(player2.deck[0])
            #print(player1.deck[0])
            card2 = player2.deck.pop(0)
            graveyard.append(card2)
            card1 = drawCard(1)
    
    
        print("You have two options... Play the card or Use the spells")
        print("Option 1-4 are for Character Stats and Option 5 & 6 are for spells")
        print("Select Your Stats \nPress : 1->Strength \n2->Attack \n3->Defence \n4->HP \n5-> God Spell \n6->Ressurection ")
        choice = int(input("You selected: "))
        if (choice == 1):
            if (card1['Strength'] > card2['Strength']):
                print("Player 1 WINS")
                player1.gamePoint = player1.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player1.beginGame()
                else:
                    gameOver()
            elif (card1['Strength'] < card2['Strength']):
                print("Player 2 WINS")
                player2.gamePoint = player2.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player2.beginGame()
                else:
                    gameOver()
                
        elif choice == 2:
            if (card1['Attack'] > card2['Defence']):
                print("Player 1 WINS \n")
                player1.gamePoint = player1.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player1.beginGame()
                else:
                    gameOver()
            elif (card1['Attack'] < card2['Defence']):
                print("Player 2 WINS \n")
                player2.gamePoint = player2.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player2.beginGame()
                else:
                    gameOver()

        elif choice == 3:
            if (card1['Defence'] > card2['Attack']):
                print("Player 1 WINS \n")
                player1.gamePoint = player1.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player1.beginGame()
                else:
                    gameOver()
            elif (card1['Defence'] < card2['Attack']):
                print("Player 2 WINS \n")
                player2.gamePoint = player2.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player2.beginGame()
                else:
                    gameOver()
        elif choice == 4:
            if (card1['HP'] > card2['HP']):
                print("Player 1 WINS\n")
                player1.gamePoint = player1.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player1.beginGame()
                else:
                    gameOver()
            elif (card1['HP'] < card2['HP']):
                print("Player 2 WINS \n")
                player2.gamePoint = player2.gamePoint + 1 
                if(len(player1.deck) and len(player2.deck) > 0):
                    player2.beginGame()
                else:
                    gameOver()
        elif choice == 5:
            godSpell()
        elif choice == 6:
            ressurection()
        else:
            print("Invalid Choice")
        
    
        
list_of_awesome_heroes = ['aquaman', 'superman', 'batman', 'wonder women', 'night wing', 'swamp thing']
n = len(list_of_awesome_heroes)

for hero in list_of_awesome_heroes:
    name = hero
    hero = Injustice_deck()
    hero.characterStats(name,random.randrange(1000, 5000),random.randrange(1000, 5000),random.randrange(1000, 5000),random.randrange(1000, 5000))
    full_deck.append(hero.showStats())



player1 = cardDealing()
player2 = cardDealing()
player1.createPlayer('Goku')
player2.createPlayer('Vegeta')

playerTurn()
#let_the_battle_begin()



