import random

class Deck:
    def __init__(self):
        cards = []

class Card:

    def __init__(self, value):
        self.value = value
            
class Dealer:
    def __init__(self):
        self.hand = 0
        self.cards = []
        self.hasAce = False
        self.stay = False
        self.money = 0

    def add_card(self):
        x = random.randrange(0, len(deck.cards) - 1)
        card = deck.cards[x]
        if card == 'Ace':
            self.hasAce = True
        self.cards.append(card)
        del deck.cards[x]

class Player:
    def __init__(self):
        self.hand = 0
        self.cards = []
        self.hasAce = False
        self.stay = False
        self.money = 0
    
    def add_card(self):
        x = random.randrange(0, len(deck.cards) - 1)
        card = deck.cards[x]
        if card == 'Ace':
            self.hasAce = True
        self.cards.append(card)
        del deck.cards[x]

dealer = Dealer()
player = Player()
deck = Deck()
game_continue = True

def setup_deck():
    deck.cards = []
    for x in range(0, 4):
        for y in range(1, 14):
            if y == 1:
                deck.cards.append('Ace')
            elif y >= 10:
                new_card = Card(10)
                deck.cards.append(new_card.value)
            else: 
                new_card = Card(y)
                deck.cards.append(new_card.value)

    print("Deck setup complete.")

def setup_game():
    setup_deck()

    for x in range(0, 2):
        dealer.add_card()
        player.add_card()

    total_hands()
    play_game()

def play_game():

    while(game_continue):

        print(f"Dealer's Hand: {dealer.hand}")
        print(f"Player's Hand: {player.hand}")
        print(f"Player's Cards: {player.cards}")

        if not player.stay:
            player_choice = input("What would you like to do? (H)it / (S)tay: ")

            if player_choice.lower() == 'h':
                player.add_card()
            elif player_choice.lower() == 's':
                print("You have chosen to stay.")
                player.stay = True

        if not dealer.stay:
            if (18 <= dealer.hand <= 21):
                print("Dealer has chosen to stay.")
                dealer.stay = True
            elif (14 <= dealer.hand <= 17):
                hit_or_stay = random.randrange(0, 1)
                if hit_or_stay == 0:
                    dealer.add_card()
                else:
                    print("Dealer has chosen to stay.")
                    dealer.stay = True
            else:
                dealer.add_card()

        if player.stay and not dealer.stay:
            input("Press Enter to continue...")
        
        if dealer.stay and player.stay:
            if dealer.hand > player.hand:
                print("Dealer's hand is better than yours. You Lose!")
                break
            elif player.hand > dealer.hand:
                print("Your hand is better than the Dealer's. You Win!")
                break
            else:
                print("The game is a Draw!")
                break

        total_hands()

        if dealer.hand > 21:
            dealer_lose()
            break
        elif player.hand > 21:
            player_lose()
            break
        else:
            continue
    
    choice = True

    while(choice):
        
        play_again = input("Would you like to play again? (Y)es / (N)o: ")

        if play_again.lower() == 'y':
            reset_game()
            break
        elif play_again.lower() == 'n':
            choice = False
            break
        else:
            print("Invalid choice.")

    return

def total_hands():
    dealer.hand = 0
    player.hand = 0
    for card in dealer.cards:
        if card == 'Ace':
            card = 10
            dealer.hand += card
        else:
            dealer.hand += card
        
    if dealer.hand > 21 and dealer.hasAce:
        dealer.hand = 0
        for card in dealer.cards:
            if card == 'Ace':
                card = 1
                dealer.hand += card
            else:
                dealer.hand += card

    for card in player.cards:
        if card == 'Ace':
            card = 10
            player.hand += card
        else:
            player.hand += card
        
    if player.hand > 21 and player.hasAce:
        player.hand = 0
        for card in player.cards:
            if card == 'Ace':
                card = 1
                player.hand += card
            else:
                player.hand += card

def reset_game():
    dealer.hand = 0
    player.hand = 0
    dealer.cards.clear()
    player.cards.clear()
    dealer.stay = False
    player.stay = False
    dealer.hasAce = False
    player.hasAce = False
    setup_game()

def dealer_lose():
    print(f"Dealer's Hand: {dealer.hand}")
    print(f"Player's Hand: {player.hand}")
    print(f"Player's Cards: {player.cards}")
    print("Dealer's Hand exceeds 21. Player Wins!")
    game_continue = False

def player_lose():
    print(f"Dealer's Hand: {dealer.hand}")
    print(f"Player's Hand: {player.hand}")
    print(f"Player's Cards: {player.cards}")
    print("Your hand exceeds 21. You lose!")
    game_continue = False

def main():
    setup_game()

    return

if __name__ == '__main__':
    main()