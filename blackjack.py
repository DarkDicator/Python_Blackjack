import random

from scipy import rand


deck_value = {
    "Spade Ace" : 11,
    "Diamond Ace" : 11,
    "Club Ace" : 11,
    "Heart Ace" : 11,
    "Spade Two" : 2,
    "Diamond Two" : 2,
    "Club Two" : 2,
    "Heart Two" : 2,
    "Spade Three" : 3,
    "Diamond Three" : 3,
    "Club Three" : 3,
    "Heart Three" : 3,
    "Club Four" : 4,
    "Heart Four" : 4,
    "Spade Four" : 4,
    "Diamond Four" : 4,
    "Club Five" : 5,
    "Heart Five" : 5,
    "Spade Five" : 5,
    "Diamond Five" : 5,
    "Club Six" : 6,
    "Heart Six" : 6,
    "Spade Six" : 6,
    "Diamond Six" : 6,
    "Club Seven" : 7,
    "Heart Seven" : 7,
    "Spade Seven" : 7,
    "Diamond Seven" : 7,
    "Club Eight" : 8,
    "Heart Eight" : 8,
    "Spade Eight" : 8,
    "Diamond Eight" : 8,
    "Club Nine" : 9,
    "Heart Nine" : 9,
    "Spade Nine" : 9,
    "Diamond Nine" : 9,
    "Spade Ten" : 10,
    "Diamond Ten" : 10,
    "Club Ten" : 10,
    "Heart Ten" : 10,
    "Spade King" : 10,
    "Diamond King" : 10,
    "Club King" : 10,
    "Heart King" : 10,
    "Spade Queen" : 10,
    "Diamond Queen" : 10,
    "Club Queen" : 10,
    "Heart Queen" : 10,
    "Spade Jack" : 10,
    "Diamond Jack" : 10,
    "Club Jack" : 10,
    "Heart Jack" : 10,
}

deck = list(deck_value.keys()) * 10
chips = 100

while chips > 0:
    dealer = []
    dealer_second_card = ""
    dealer_point = 0
    player = []
    player_point = 0
    try:
        bet = int(input("Input your bet (Chips remaiing :" + str(chips) + "): "))
    except:
        while True:
            try:
                bet = int(input("Invalid input, Please input a valid numbera (Chips remaiing :" + str(chips) + "): "))
                break
            except ValueError:
                pass
    

    while bet > chips:
        bet = int(input("You don't have enough chips (Chips remaiing :" + str(chips) + "): "))

    chips -= bet

    for _ in range(2):
        card = random.choice(deck)
        if _ == 1:
            dealer_second_card = card
        else:
            dealer.append(card)
            dealer_point += deck_value[card]
        deck.remove(card)
        card = random.choice(deck)
        player.append(card)
        player_point += deck_value[card]
        deck.remove(card)

    win = False

    if player_point == 21:
        win = True
        chips += (bet * 2) + bet / 2

    else:
        while True:
            print("Player cards" + str(player) + str(player_point))
            print("Dealer cards" + str(dealer) + str(dealer_point))
            action = input("What is your action? (hit/fold/open): ")
            if action == "hit":
                card = random.choice(deck)
                player.append(card)
                player_point += deck_value[card]
                deck.remove(card)

                if player_point > 21:
                    break


            elif action == "fold":
                break


            elif action == "open":
                dealer.append(dealer_second_card)
                dealer_point += deck_value[dealer_second_card]
                while dealer_point <= 17:
                    card = random.choice(deck)
                    dealer.append(card)
                    dealer_point += deck_value[card]
                    deck.remove(card)

                if dealer_point > 21 or dealer_point < player_point:
                    win = True
                break

            else:
                print("invalid input")


        print("Player cards" + str(player))
        print("Dealer cards" + str(dealer))


    if win == False:
        print("You lose")
    else:
        print("You win")
        chips += bet * 2


