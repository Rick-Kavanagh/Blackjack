import random
from art import logo
import os


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(hand):
    """Calculate score of a given hand. If over 21, converts Aces to 1"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    else:
        if 11 in hand and sum(hand) > 21:
            hand.remove(11)
            hand.append(1)
            return sum(hand)
        else:
            return sum(hand)


def compare(user_hand_value, cpu_hand_value, user_hand, cpu_hand):
    """Takes user and cpu hands and determines a winner"""
    if cpu_hand_value == 0:
        print(f"Your final cards: {user_hand}, your final score: {sum(user_hand)}")
        print(f"CPUs final cards: {cpu_hand}, CPUs final score: BLACKJACK")
    elif user_hand_value == 0:
        print(f"Your final cards: {user_hand}, your final score: BLACKJACK")
        print(f"CPUs final cards: {cpu_hand}, CPUs final score: {cpu_hand_value}")
    else:
        print(f"Your final cards: {user_hand}, your final score: {user_hand_value}")
        print(f"CPUs final cards: {cpu_hand}, CPUs final score: {cpu_hand_value}")

    if user_hand_value == cpu_hand_value and cpu_hand_value != 0:
        print("Push!")
    elif cpu_hand_value == 0:
        print("CPU has blackjack, you lose!")
    elif user_hand_value == 0:
        print("You have blackjack, you win!")
    elif user_hand_value > 21:
        print(f"You busted with {user_hand_value}, you lose!")
    elif cpu_hand_value > 21:
        print(f"CPU busted with {cpu_hand_value}, you win!")
    else:
        if user_hand_value > cpu_hand_value:
            print(f"Your {user_hand_value} beats the CPUs {cpu_hand_value}, you win!")
        else:
            print(f"Your {user_hand_value} loses to the CPUs {cpu_hand_value}, you lose!")


def blackjack():
    user_hand = []
    cpu_hand = []
    user_hand_value = 0
    os.system('cls')
    print(logo)
    for _ in range(2):
        user_hand.append(deal_card())
        cpu_hand.append(deal_card())
    print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
    print(f"Computer's first card: {cpu_hand[0]}")

    if calculate_score(cpu_hand) == 0:
        cpu_hand_value = 0
        user_hand_value = sum(user_hand)
    elif calculate_score(user_hand) == 0:
        user_hand_value = 0
    else:
        while True:
            if calculate_score(user_hand) > 21:
                user_hand_value = calculate_score(user_hand)
                break
            another = input("Would you like another card? Type 'y' or 'n': ")
            if another.lower() == "y":
                user_hand.append(deal_card())
                print(f"Your cards: {user_hand}, current score: {calculate_score(user_hand)}")
                print(f"Computer's first card: {cpu_hand[0]}")
            else:
                user_hand_value = calculate_score(user_hand)
                break

    while True:
        if 0 < calculate_score(cpu_hand) < 17:
            cpu_hand.append(deal_card())
        else:
            cpu_hand_value = calculate_score(cpu_hand)
            break

    compare(user_hand_value, cpu_hand_value, user_hand, cpu_hand)
    again = input("\nWould you like to play again? Type 'y' or 'n'")
    if again == 'y':
        blackjack()


play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play.lower() == "n":
    exit()
else:
    blackjack()
