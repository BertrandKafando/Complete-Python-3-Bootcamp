from deck.deck import Deck
from playerModule.player import Player


def askPlayerbet(player):
    while True:
        try:
            bet = int(input('How much do you want to bet? '))

        except:
            print('Please enter a number')
        else:
            return bet


if __name__ == '__main__':
    # Game Setup
    player1 = Player('One')
    player2 = Player('Two')
    round_num = 0
    deck = Deck()
    deck.shuffle()

    # Distribute cards
    for i in range(26):
        player1.add_cards(deck.deal_one())
        player2.add_cards(deck.deal_one())

    game_on = True

    while game_on:

        round_num += 1
        print(f'Round {round_num}')

        if len(player1.all_cards) == 0:
            print('Player One out of cards! Player Two wins!')
            game_on = False
            break
        if len(player2.all_cards) == 0:
            print('Player Two out of cards! Player One wins!')
            game_on = False
            break

        # Start a new round
        player1_cards = []
        player1_cards.append(player1.remove_one())

        player2_cards = []
        player2_cards.append(player2.remove_one())

        # compare cards
        at_war = True
        while at_war:
            if player1_cards[-1].value > player2_cards[-1].value:
                player1.add_cards(player1_cards)
                player1.add_cards(player2_cards)
                at_war = False
            elif player1_cards[-1].value < player2_cards[-1].value:
                player2.add_cards(player2_cards)
                player2.add_cards(player1_cards)
                at_war = False
            else:
                print('WAR!')
                if len(player1.all_cards) < 5:
                    print('Player One unable to declare war')
                    print('Player Two wins!')
                    game_on = False
                    break
                elif len(player2.all_cards) < 5:
                    print('Player Two unable to declare war')
                    print('Player One wins!')
                    game_on = False
                    break
                else:
                    for i in range(5):
                        player1_cards.append(player1.remove_one())
                        player2_cards.append(player2.remove_one())

    print('Game Over')
