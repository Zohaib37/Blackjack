import random
from replit import clear

def give_cards(card_list):
  return random.choice(card_list)


def total_score(cards_list):
  total = 0
  for i in range(len(cards_list)):
    if cards_list[i] == 11 and total > 10:
      cards_list[i] = 1
    total += cards_list[i]
  return total  

def generate_computer_cards(computer_cards, card_list):
  while total_score(computer_cards) < 17:
    computer_cards.append(random.choice(card_list))

def check_winner(user_score, computer_score):
  if user_score > 21:
    print("Bust!")
  elif computer_score > 21:
    print("Computer went over 21, you win!")
  elif computer_score > user_score:
    print("You lose!")
  elif user_score > computer_score:
    print("You win!")
  else:
    print("Draw")      

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_of_game = False
while not end_of_game:
  user_cards = []
  computer_cards = []

  end_of_user_turn = False

  for i in range(2):
    user_cards.append(give_cards(cards))
    computer_cards.append(give_cards(cards))

  user_total = total_score(user_cards)
  if user_total == 21:
    print(f"Your final hand: {user_cards}\nBlackjack!")
    break

  print(f"Your cards: {user_cards}, Total: {user_total}")
  print(f"Computer's first card: {computer_cards[0]}")

  while not end_of_user_turn:
    pick_again = input("Type 'y' to get another card, type 'n' to pass. ")
    if pick_again == "y":
      user_cards.append(give_cards(cards))
      user_total = total_score(user_cards)
      print(f"Your cards: {user_cards}, Total: {user_total}")
      if user_total > 21:
        break
    else:
      end_of_user_turn = True   

  generate_computer_cards(computer_cards, cards)

  computer_total = total_score(computer_cards)    

  print(f"Your final hand: {user_cards}, Total score: {user_total}\nComputer's final hand: {computer_cards}, Total score: {computer_total}")

  check_winner(user_total, computer_total)
  run_again = input("Do you want to continue? Type 'y' or 'n'. ")
  if run_again == "y":
    clear()
  else:
    end_of_game = True


