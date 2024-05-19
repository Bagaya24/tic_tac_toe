from art import logo, p1_won, p2_won, equality
import random

print(logo)

a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "


def tic_tac_play(choice, player):
    global a, b, c, d, e, f, g, h, i
    if choice == "a":
        a = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "b":
        b = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "c":
        c = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "d":
        d = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "e":
        e = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "f":
        f = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "f":
        f = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "g":
        g = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "h":
        h = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)
    elif choice == "i":
        i = player
        print(f"""                      {a} | {b} | {c}  
                   ---------------
                       {d}| {e} | {f} 
                   ---------------
                       {g}| {h} | {i} """)


def have_won(player1, player2):
    global a, b, c, d, e, f, g, h, i
    if a == b == c == player1 or a == d == g == player1 or a == e == i == player1 or b == e == h == player1 or c == f == i == player1 or c == e == g == player1 or d == e == f == player1 or g == h == i == player1:
        print(p1_won)
        return True
    elif a == b == c == player2 or a == d == g == player2 or a == e == i == player2 or b == e == h == player2 or c == f == i == player2 or c == e == g == player2 or d == e == f == player2 or g == h == i == player2:
        print(p2_won)
        return True


nbr_players = input("Type '1' for one player and '2' for two players: ")
if nbr_players == "2":
    players_1 = input("Make you chose between 'X' or 'O': ").upper()
    players_2 = ""
    if players_1 == "X":
        players_2 = "O"
    elif players_1 == "O":
        players_2 = "X"
    nbr = 0
    while nbr < 9:
        choice_place = input("""Play                                  a | b | c  
                                      ----------
                                      d | e | f 
                                      ----------
                                      g | h | i: """).lower()
        print("\n")
        if nbr % 2 == 0:
            tic_tac_play(choice_place, players_1)
        else:
            tic_tac_play(choice_place, players_2)
        print("\n")
        if have_won(players_1, players_2):
            break
        nbr += 1
        if nbr == 9:
            print("Equality")

elif nbr_players == "1":
    players_1 = input("Make you chose between 'X' or 'O': ").upper()
    players_2 = ""
    if players_1 == "X":
        players_2 = "O"
    elif players_1 == "O":
        players_2 = "X"
    computer_choice = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
    nbr = 0
    while nbr < 9:
        if nbr % 2 == 0:
            choice_place = input("""Play                                      a | b | c  
                                          ----------
                                          d | e | f 
                                          ----------
                                          g | h | i: """).lower()

            tic_tac_play(choice_place, players_1)
            computer_choice.remove(choice_place)

        else:
            choice_place = random.choice(computer_choice)
            tic_tac_play(choice_place, players_2)
        print("\n")
        if have_won(players_1, players_2):
            break
        nbr += 1
        if nbr == 9:
            print(equality)
