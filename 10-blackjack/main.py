import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score,c_score):
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def blackjack():
    game=input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
    if game!="y":
        return
    print(art.logo)
    ur_card = [deal_card(),deal_card()]
    comp_card = [deal_card(),deal_card()]
    ur_score=0
    comp_score=0
    game_over = False

    while not game_over :
        ur_score = calc_score(ur_card)
        comp_score = calc_score(comp_card)
        print(f"Your cards: {ur_card}, current score: {ur_score}")
        print(f"Computer's first card: {comp_card[0]}")

        if ur_score==0 or comp_score==0 or ur_score>21:
            game_over=True

        else :
            cont=input("Type 'y' to get another card, type 'n' to pass:")
            if cont == "y":
                ur_card.append(deal_card())
                ur_score = calc_score(ur_card)
            else :
                game_over = True

    while comp_score !=0 and comp_score <17 :
        comp_card.append(deal_card())
        comp_score = calc_score(comp_card)

    print("\n")
    print(f"Your final hand: {ur_card}, final score: {ur_score}")
    print(f"Computer's final hand: {comp_card}, final score: {comp_score}")
    print(compare(ur_score,comp_score))

blackjack()