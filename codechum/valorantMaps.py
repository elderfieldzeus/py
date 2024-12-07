# Ascent - 2 Initiators
# Haven - 2 Duelists
# Split - 2 Controllers
# Bind - 2 Sentinels

from collections import Counter

maps = {"Ascent": 'I', "Haven": 'D', "Split": 'C', "Bind": 'S'}

roles = input("Enter the different roles: ")
selected_map = input("Enter map: ")

teams = 0
c = Counter(roles)

if selected_map in maps:
    min_role = maps[selected_map]

    while all(i > 0 for i in c.values()):
        for i in c:
            c[i] -= 1
        
        if c[min_role] > 0:
            teams += 1
            c[min_role] -= 1

else:
    while all(i > 0 for i in c.values()):
        for i in c:
            c[i] -= 1
        teams += 1


print(f"The maximum number of teams in {selected_map} is {teams}.")
