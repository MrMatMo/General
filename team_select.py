import random


def print_protocol(t1, t2):
    print(" ")
    print("-------------------")
    print(" ")
    print(f"[ {t1} ] Vs. [ {t2} ]" )
    print(" ")


seed_1 = ["paris", "Barca", "Real Madrid", "Man United",
          "Man City", "Chelsea", "Arsenal", "Bayern Munich", "Inter"]
seed_2 = ["Monaco", "Totenham", "Leverkusen",
          "Durtmond", "RB Leipzig", "Juve", "Milan", "Roma"]

seed_preference = input("Do you have a prefered seed ? (y/n)")

if seed_preference == "y":
    prefered_seed = int(input("Prefered seed ? (1,2)"))
    if prefered_seed == 1:
        team_1 = random.choice(seed_1)
        seed_1.remove(team_1)
        team_2 = random.choice(seed_1)
        print_protocol(team_1, team_2)
    elif prefered_seed == 2:
        team_1 = random.choice(seed_2)
        seed_2.remove(team_1)
        team_2 = random.choice(seed_2)
        print_protocol(team_1, team_2)


elif seed_preference == "n":
    team_1 = random.choice(seed_1 + seed_2)
    seed_boundries = input("seed Boundries ? (y/n)")

    if seed_boundries == "y":
        if team_1 in seed_1:
            seed_1.remove(team_1)
            team_2 = random.choice(seed_1)
            print_protocol(team_1, team_2)
        elif team_1 in seed_2:
            seed_2.remove(team_1)
            team_2 = random.choice(seed_2)
            print_protocol(team_1, team_2)
    elif seed_boundries == "n":
        if team_1 in seed_1:
            seed_1.remove(team_1)
        elif team_1 in seed_2:
            seed_2.remove(team_1)
        team_2 = random.choice(seed_1 + seed_2)
        print_protocol(team_1, team_2)
    else:
        print("** WRONG INPUT **")
else:
    print("** WRONG INPUT **")
