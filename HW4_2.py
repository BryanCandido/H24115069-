import random

cardnum = {
    "ACE": 11,
    "KING": 10,
    "QUEEN": 10,
    "JACK": 10,
    "10": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}
cardtype = ["HEART", "DIAMOND", "CLUB", "SPADE"]

def create_deck():
    deck = []
    for card_type in cardtype:
        for card_num in cardnum:
            deck.append((card_num, card_type))
    random.shuffle(deck)
    return deck

def handvalue(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[0] == "ACE": 
            aces += 1
        value += cardnum[card[0]]
    while value > 21 and aces > 0:
        value -= 10
        aces -= 1
    return value

def blackjack():
    while True:
        deck = create_deck()
        
        # Deal the initial cards
        playerhand = [deck.pop(), deck.pop()] 
        dealerhand = [deck.pop(), deck.pop()]
        
        # Show the hands
        print("Your current value is {}".format(handvalue(playerhand)))
        print("with the hand: ", end="")
        print(", ".join("{}-{}".format(card[0], card[1]) for card in playerhand))
        choice = input("\nHit or stay? (Hit = 1, Stay = 0): ")

        while choice == "1":
            new_card = deck.pop()
            playerhand.append(new_card)
            print("You draw {}-{}".format(new_card[0], new_card[1])) 
            print("\nYour current value is {}".format(handvalue(playerhand)))
            print("with the hand: ", end="")
            print(", ".join("{}-{}".format(card[0], card[1]) for card in playerhand))
            if handvalue(playerhand) > 21:
                print("\n*** Dealer wins! ***")
                break
            choice = input("\nHit or stay? (Hit = 1, Stay = 0): ")

        if handvalue(playerhand) <= 21:
            print("\nDealer's hand: ", end="")
            print(", ".join("{}-{}".format(card[0], card[1]) for card in dealerhand))
            print("Dealer's current value is {}".format(handvalue(dealerhand)))
            while handvalue(dealerhand) < 17:
                dealerhand.append(deck.pop())
                print("\nDealer draws {}-{}".format(dealerhand[-1][0], dealerhand[-1][1])) 
                print("\nDealer's current value is {}".format(handvalue(dealerhand)))
                print("with the hand: ", end="")
                print(", ".join("{}-{}".format(card[0], card[1]) for card in dealerhand))
            if handvalue(dealerhand) > 21:
                print("\n*** You beat the dealer! ***") 
            elif handvalue(playerhand) > handvalue(dealerhand):
                print("\n*** You beat the dealer! ***")
            elif handvalue(playerhand) == handvalue(dealerhand):
                print("\n*** You tied the dealer, nobody wins. ***")
            else:
                print("\n*** Dealer wins! ***")

        choice = input("\nWant to play again? (y/n): ")
        if choice.lower() != "y":
            break

blackjack()