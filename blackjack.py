"""
    Date created: 24/07/2024
    Last modified: 24/07/2024
    Python Version: 3.12
"""

import random
import os
from art import logo


def clear():
  """Clears the console screen based on the operating system."""
  os.system("cls" if os.name == "nt" else "clear")


def deal_card():
  """Returns a random card from the deck. Ace (11) and face cards (10) are included."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  x = random.choice(cards)
  return x


def calculate_score(cards):
  """
    Calculates the score of the given hand.
    Returns 0 if the hand is a Blackjack (two cards totaling 21).
    Converts an Ace from 11 to 1 if the hand's total score exceeds 21.
    """
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  while 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)


def compare(user_score, computer_score):
  """
    Compares the scores of the user and the computer and prints the result.
    A score of 0 indicates a Blackjack.
    """
  if user_score == computer_score:
    print("\nDraw! 🙃")
  elif computer_score == 0:
    print("\nOpponent wins with a Blackjack! 😱")
  elif user_score == 0:
    print("\n You win with a Blackjack! 😎")
  elif user_score > 21:
    print("\nYou're busted! You lose! 😭")
  elif computer_score > 21:
    print("\n Opponent busted! You win! 😁)")
  elif user_score > computer_score:
    print("\nYou win! 😃")
  else:
    print("\nOpponent wins! 😤")


def main():
  while True:
    clear()
    print(logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not game_over:
      print(f"Your cards {user_cards}, current score: {user_score}")
      print(f"Computer's first card: {computer_cards[0]}")

      # Check for Blackjack or busts
      if user_score == 0 or computer_score == 0 or user_score > 21:
        game_over = True
      else:
        deal = input("\nDo you want to deal another card? Type 'y' or 'n': ")
        if deal in ["y", "yes"]:
          user_cards.append(deal_card())
          user_score = calculate_score(user_cards)

        elif deal in ["n", "no"]:
          game_over = True

    # Keep drawing computer cards if it has score lass than 17
    while computer_score != 0 and computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)

    # Display final hands and scores
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, score: {computer_score}")
    compare(user_score, computer_score)

    restart = input(
        "\nDo you want to play another game of Blackjack? Type 'y' or 'n': "
    ).lower()
    if restart in ["n", "no"]:
      break

    elif restart in ["y", "yes"]:
      continue


main()
