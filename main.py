import random

cards = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_total = 0
dealer_total = 0


def make_deck() -> list:
    list = []
    for i in range(2):
        list.append(random.choice(cards))
    return list


def deal_cards():
    while True:
        player_total = calc_total(player_deck)

        print("Your cards:", end=" ")
        print(*player_deck)
        print(player_total)

        user_input = input("Do you want to hit(h) or stop(s)?\n-> ")

        check_winner()

        if user_input == 'h':
            player_deck.append(random.choice(cards))
            print(player_total)

        if user_input == 's':
            print("Dealer's turn.")

            break


def calc_total(list_deck: list):
    solution_1 = 0
    solution_2 = 0

    for card in list_deck:
        if card == 'A':
            solution_1 = 1 + solution_1
            solution_2 = 11 + solution_2

        elif card != 'A':
            solution_1 = solution_1 + card
            solution_2 = solution_2 + card

    # print(solution_1)  # Printing just for keeping log
    # print(solution_2)

    if (solution_1 < 21 and solution_1 >= solution_2) or solution_1 == 21:
        return solution_1

    elif (solution_1 < 21 and solution_2 > solution_1) or solution_1 == 21:
        return solution_2

    elif (solution_1 and solution_2) > 21:
        return min([solution_1, solution_2])


# if the dealer's cards total is less than 17 he has to hit
# if it is more than 17 he stops
# if it is equal to 21 he wins
# if it is more than 21 he loses


def dealer_cards():
    dealer_total = calc_total(dealer_deck)

    while True:
        print("Dealer's cards:", end=" ")
        print(*dealer_deck)
        print(dealer_total)

        if dealer_total < 17:
            dealer_deck.append(random.choice(cards))
            dealer_total = calc_total(dealer_deck)

        elif dealer_total == 21:
            print("You lose!")
            final_score()
            break

        elif dealer_total < 21:
            check_winner()
            break

        else:
            print("Dealer Busts. You win!")
            final_score()
            break


def final_score():
    player_total = calc_total(player_deck)
    dealer_total = calc_total(dealer_deck)
    print("Your cards:", end=" ")
    print(*player_deck)
    print(f"Your total: {player_total} ")
    print("Dealer's cards:", end=" ")
    print(*dealer_deck)  # * removes brackets
    print(f"Dealer's total: {dealer_total} ")


def check_winner():
    print("Yahallo!")
    # TODO not complete lol


player_deck = make_deck()
dealer_deck = make_deck()

print(player_deck)
print(dealer_deck)

deal_cards()
dealer_cards()
check_winner()
final_score()
