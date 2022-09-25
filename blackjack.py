import random

playerIn = True
dealerIn = True

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', ]

player_hand = []
dealer_hand = []


# deal the cards
def dealCards(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)
    # turn.append(deck.pop(card))
    # returns and removes the item at the given index only works for int



# calculate the total of each hand
def total(turn):
    total = 0
    aces_11s = 0
    face = ['J', 'Q', 'K']
    for card in turn:
        if card in range(11):
            total += card
        elif card in face:
            total += 10
        else:
            total += 11
            aces_11s += 1
        while aces_11s and total > 21:
            total -= 10
            aces_11s -= 1

    return total


# check for winner
def revealDealerHand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]


# game loop
for _ in range(2):
    dealCards(dealer_hand)
    dealCards(player_hand)

print(dealer_hand)
print(player_hand)

while playerIn or dealerIn:
    print(f"Dealer had {revealDealerHand()} and X")
    print(f"You have {player_hand} for a total of {total(player_hand)}")
    if playerIn:
        stayOrHit = input("1: Stay\n2. Hit\n")
    if total(dealer_hand) > 16:
        dealerIn = False
    else:
        dealCards(dealer_hand)
    if stayOrHit == '1':
        playerIn = False
    else:
        dealCards(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand) >= 21:
        break

print_msg = f"\nYou have {player_hand} for a total of {total(player_hand)} " \
            f"and the dealer has {dealer_hand} for a total of {total(dealer_hand)}"

if total(player_hand) == 21:
    print(print_msg)
    print("Blackjack! You win!")

elif total(dealer_hand) == 21:
    print(print_msg)
    print("Blackjack! Dealer wins!")

elif total(player_hand) > 21:
    print(print_msg)
    print("You bust! Dealer wins!")

elif total(dealer_hand) > 21:
    print(print_msg)
    print("Dealer busts! You win!")

elif 21 - total(dealer_hand) < 21 - total(player_hand):
    print(print_msg)
    print("Dealer wins!")

elif 21 - total(dealer_hand) > 21 - total(player_hand):
    print(print_msg)
    print("You win!")
