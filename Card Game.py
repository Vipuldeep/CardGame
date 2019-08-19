import random

def main():
    # The main function does not take any input parameters or return any output
    # It gets the player name, plays game based on Starting Balance and at the end displays final balance and result.

    playerName = getPlayerName()
    STARTINGBALANCE = 100                                                     #Declaring a constant for starting balance
    finalBalance = playGame(STARTINGBALANCE)
    wonLost, wonLostAmount = decideWonLost(STARTINGBALANCE, finalBalance)     # Defining two variables wonLost and wonLostAmount as the two respective values returned by function decideWonLost
    print("Your final balance is $" + str(finalBalance) + ". Overall you " + wonLost + " $" + str(wonLostAmount) + ".\nHave a good day, " + playerName + "!")

def playGame(balance):
    #The playGame function takes balance (starting balance) as input parameter and returns the updated balance (final balance)
    #This function allows to play game based on starting balance, and updates the balance based on bet and round results
    #The game will only quit when player decides to quit or runs out of balance

        continueOrQuit = "C"            #continueOrQuit is initialised with "C" so that the round begins for the first time
        while continueOrQuit.upper() == "C":
            betAmount = getBetAmount(balance)
            playerCard = random.randint(1, 13)          #Generates a random card from 1 to 13
            playerCardName = getCardName(playerCard)
            computerCard = random.randint(1, 13)        #Generates a random card from 1 to 13
            computerCardName = getCardName(computerCard)
            print("Your card is " + str(playerCard) + " (" + playerCardName + ").")
            playerGuess = getValidChoice("Is the computer’s card higher (H) or lower (L)?", "highLow")
            print("The computer's card is " + str(computerCard) + " (" + computerCardName + ").")
            winAmount = calculateRoundResult(playerCard, computerCard, playerGuess, betAmount)
            balance = balance + winAmount
            if balance == 0:                            #Quits game if player runs out of balance
                print("Your balance is $0. Game over!")
                break
            else:                                       #Else, asks the player to continue or quit
                continueOrQuit = getValidChoice("Continue (C) or Quit (Q)?", "continueQuit")
        return balance

def getCardName(cardNumber):
    #The getCardName function takes cardNumber as input parameter and returns nameOfCard based on the cardNumber
    #This function takes the random card number from the playRounds function and assigns a card name to that number from a list of cards.

    cards = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]    #A list of all the card names
    nameOfCard = cards[cardNumber - 1]                  #'-1' because the list has index from 0 to 12, and cardNumber is in the range from 1 to 13
    return nameOfCard

def calculateRoundResult(pCard, cCard, guessInput, bet):
    #The roundResult function takes pCard (player card), cCard (computer card), guessInput (player guess) and bet as input parameters and returns winAmount
    #It decides whether the player has won or lost the round based on the guess and cards generated, and calculates the amount won based on bet

    winAmount = 0                       #Initialising the winAmount
    # Tie condition
    if pCard == cCard:
        print("It's a tie!")
        winAmount = 0
    #Win condition
    elif (((guessInput.upper() == "L") and (cCard != 1 and (pCard == 1 or ((pCard != 1) and pCard > cCard))))) or ((guessInput.upper() == "H") and ((pCard != 1) and (cCard == 1 or (cCard != 1 and cCard > pCard)))):
        print("Well done, you guessed right! You get your $"+str(bet)+" back and you win $"+str(bet)+" extra!")
        winAmount = bet
    #Lose condition
    else:
        print("Sorry, better luck next time! You lost $" + str(bet) + ".")
        winAmount = 0 - bet
    return winAmount

def decideWonLost(amount1, amount2):
    # The decideWonLost function takes two different amounts as input, and returns two values wonLost and wonLostAmount
    # This function decides whether the player has won or lost overall, and by what amount

    wonLostAmount = 0               #Initialising the wonLostAmount
    if amount2 < amount1:           #Overall lost condition
        wonLost = "lost"
        wonLostAmount = amount1 - amount2
    else:                           #Overall won condition
        wonLost = "won"
        wonLostAmount = amount2 - amount1
    return wonLost, wonLostAmount    # Returning two values from this function

def getPlayerName():
    #The getPlayerName function takes no input parameters and returns the correct inputName
    #This function gets and validates the player name
    #If the name input is blank or something other than alphabets, then it asks again for name until correctly entered

    inputName = input("Hello! What is your name?")
    while (len(inputName.replace(' ','')) < 1) or (inputName.replace(' ','').isalpha() != True):
        if len(inputName.replace(' ','')) < 1:                        #replace function removes all the spaces (replaces spaces with blanks)
            errorMessage = "Don't be shy. Please enter your name."
        elif inputName.replace(' ','').isalpha() != True:             #isalpha function does not return true if there is space, hence spaces are removed with replace function again
            errorMessage = "It is unlikely your name is " + inputName + "! Please enter your name."
        inputName = input(errorMessage)
    inputName = inputName.strip(' ').title()      #strip function will remove all spaces from extreme left and rights, and title function will capitalise first letter of every word
    print(inputName + ", welcome to the Card Guessing Game!")

    #This function validates name in such a way that it accepts spaces and alphabets only, and allows to enter full name
    #For example, you can enter full name like "Meet Gorasia"
    return inputName


def getBetAmount(balance):
    #The getBetAmount function takes balance as input and returns integer of bet
    #It gets bet amount from the user and validates it

    bet = input("Your balance is $" + str(balance) + ". How much do you want to bet?")
    while (len(bet.replace(" ","")) == 0 or (bet.lstrip('-').replace('.','',1).isdigit() != True) or float(bet) <= 0 or float(bet) % 5 != 0 or float(bet) > balance):
        if len(bet.replace(" ","")) == 0:
            errorMessage = "Don't be shy. Please enter your bet amount."
        elif bet.lstrip('-').replace('.','',1).isdigit() != True:
                                            # The "-" sign is stripped just from left side and decimal "." is removed once from the input to validate as a valid number
                                            # For example, "-5.6" is a valid number (but its isdigit() is not true)
                                            # Whereas, "5.6.3" or "5-6" or "6-" are not valid numbers
            errorMessage = "Invalid bet! Please enter bet amount as a number."
        elif float(bet) <= 0:
            errorMessage = "Invalid bet! Please enter a positive bet amount."
        elif float(bet) > balance:
            errorMessage = "Invalid bet! Please enter a bet amount less than or equal to your balance."
        elif float(bet) % 5 != 0:
            errorMessage = "Invalid bet! Please enter bet amount in multiples of 5."
        bet = input(errorMessage)
    return int(float(bet))
    #Returns int(float(bet)) so that input like "25.00" can also be accepted as valid and converted to "25"

def getValidChoice(prompt, menu):
    #The getValidChoice function takes prompt and menu as input parameters and returns a valid choice
    #It takes the user input for choice and validates it based on the menu he is in

    if menu == "highLow":           #assigns valid choices to validChoices in highLow menu
        validChoices = ["H","L"]
        errorMessage = "Invalid input! Please choose (H) for Higher or (L) for Lower."
    elif menu == "continueQuit":    #assigns valid choices to validChoices in continueQuit menu
        validChoices = ["C","Q"]
        errorMessage = "Invalid input! Please enter (C) for continuing or (Q) for quitting the game."
    choice = input(prompt)
    while choice.upper() not in validChoices:           #upper function will capitalise the input
        choice = input(errorMessage)
    return choice

main()