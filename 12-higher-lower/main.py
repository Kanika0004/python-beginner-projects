import random
import art
import game_data

def higher_lower_game():
    game_on=True
    data = game_data.data
    score = 0
    right_ans=""
    perA = random.choice(game_data.data)
    perB = random.choice(game_data.data)

    while game_on :
        print(art.logo)
        if perA["follower_count"] > perB["follower_count"]:
            right_ans = "A"
        else:
            right_ans = "B"
        print(f"Compare A: {perA["name"]}, a {perA["description"]}, from {perA["country"]}.")
        print(art.vs)
        print(f"Against B: {perB["name"]}, a {perB["description"]}, from {perB["country"]}.")
        ans=input("Who has more followers? Type 'A' or 'B': ")
        if ans == right_ans:
            score += 1
            print("\n" * 20)
            print(f"You're right! Current score: {score}.")
            if right_ans == "B":
                perA = perB
            perB = random.choice(game_data.data)

        else :
            game_on = False
            print("\n" * 20)
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")

higher_lower_game()



