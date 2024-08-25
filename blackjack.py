import random

pattern = ['Diamond', 'Club', 'Heart', 'Spade']
card = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deckCard = [card[i] + ' ' + pattern[x] for i in range(len(card)) for x in range(len(pattern))]

userCard = []
compCard = []

def shuffle(deckCard):
  random.shuffle(deckCard)

def printCard(card):
  for x in card:
    print(x)

def getCard(deckCard, playerCard):
  c = deckCard[0]
  playerCard.append(c)
  deckCard.pop(0)
  return c

#allows user to request card or stop
def option():
  valid = True
  while valid:
    choice = input("\nUser's choice - Enter 1 for REQUEST CARD or 2 for STOP:")
    try:
      choice = int(choice)
      if choice == 1 or choice == 2:
        valid = False
      else:
        print('Invalid input. Please enter only 1 or 2 for your choice according to the instruction.')
    except:
        print('Invalid input. Please enonly 1 or 2 for your choice according to the instruction.')
  return choice

#this option should appear after cards are divided and checked by user
def optionAce():
  valid = True
  while valid:
    choiceAce = input("\nPlease choose value for Ace with 1 or 11:")
    if choiceAce == '1' or choiceAce == '11':
      valid = False
    else:
      print('Invalid input. Please enter only 1 or 11 for your choice according to the instruction.')
  return choiceAce

#convert Ace to 1 or 11 after making option in optionAce()
def checkNconvertAce(playerCard): 
  for i in range(len(playerCard)):
    if playerCard[i][0] == 'A':
      numAce = optionAce()
      playerCard[i] = numAce + playerCard[i][1:]

def countTotal(playerCard):
  sum = 0
  for card in playerCard:
    number, suit = card.split()
    if number in ['J', 'Q', 'K']:
      number = 10
    elif number == 'A':
      continue
    else:
      number = int(number)
    sum += number
  return sum

#add one card when input 1 to option() per time and stop when input 2 to option()
#when user's total card is 5, user is forced to show the cards taken
#involve getCard()
def userMove():
  checkNconvertAce(userCard)
  print("User's total:", countTotal(userCard))
  userChoice = option()
  extraCardcount = 0
  if userChoice == 1:
    count = 3
    while count > 0:
      count -= 1
      extraCardcount += 1
      extraCard = getCard(deckCard, userCard)
      print('\nUser get:', extraCard)
      checkNconvertAce(userCard)
      print("User's total:",countTotal(userCard))
      if count == 0:
        break
      userChoice = option()
      if userChoice == 2:
        break
  else:
    print("User done managing card.")
  print('\nUser gets', extraCardcount ,'extra cards.')
  print("User's total:",countTotal(userCard))
   
#involve getCard()
def compMove():
  print('\n')
  count = 3
  ace = 0
  sum = countTotal(compCard)
  for card in compCard:
    if 'A' in card:
      ace += 1
  if ace == 2:
    sum = 21
  elif ace == 1:
    sum += 11
    if sum > 21:
      sum -= 10
  while sum < 17 and count > 0:
    extraCard = getCard(deckCard, compCard)
    print('Computer gets: ?')
    sum = countTotal(compCard)
    if 'A' in extraCard:
      sum += 11
      if sum > 21:
        sum -= 10
    count -= 1
  print("Computer done managing card.")
  return sum

def checkBust(uS, cS):
  bust = 0
  if uS>21 and cS>21: 
    bust = 2 #both busted
  elif uS<=21 and cS<=21:
    bust = 0 #no busted
  else:
    bust = 1 #one is busted
  return bust

def checkWinner(uS, cS):
  bustNum = checkBust(uS, cS)
  print('\n')
  if bustNum == 2:
    print('Both players are busted. Game is tie.')
  elif bustNum == 1:
    if uS>21:
      print('Game over!')
      print('User is busted. Computer wins the game.')
    else:
      print('Computer is busted. User wins the game.')
  elif bustNum == 0:
    if uS>cS:
      print('User wins the game.')
    elif cS>uS:
      print('Game over!')
      print('Computer wins the game.')
    else:
      print('Both players have equal point. Game is a tie.')

def blackjack(playerCard):
  if 'A' in playerCard[0] or 'A' in playerCard[1]:
    return ('10' in playerCard[0] or '10' in playerCard[1]
            or 'J' in playerCard[0] or 'J' in playerCard[1] 
            or 'Q' in playerCard[0] or 'J' in playerCard[1] 
            or 'K' in playerCard[0] or 'J' in playerCard[1])


def main():
  print('----------------BLACKJACK FOR 1 PLAYER------------------')
  #shuffle deck
  shuffle(deckCard)

  #get 2 cards each
  for x in range(2):
      getCard(deckCard, userCard)
      getCard(deckCard, compCard)
  print('\nUser card:')
  printCard(userCard)

  #check for blackjack
  if blackjack(userCard) and blackjack(compCard):
    print('Game is a tie. Both players have blackjack.')
  elif blackjack(userCard):
    print('User wins. User gets a blackjack.')
  elif blackjack(compCard):
    print('Computer wins. Computer gets a blackjack.')
  else:
    #All players do not have blackjack
    userMove()
    compSum = compMove()
    userSum = countTotal(userCard)
    print('\nComputer card:')
    printCard(compCard)
    print("\nUser's total:", userSum)
    print("Computer's total:", compSum)

    #check for winner
    checkWinner(userSum, compSum)

main()