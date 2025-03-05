mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = len(mission_names)
successful_missions = 0
missions_before_2000 = []

for i in range(total_missions):
    if mission_success[i]:
        successful_missions += 1
    if mission_years[i] < 2000:
        missions_before_2000.append(mission_names[i])

success_rate = (successful_missions / total_missions) * 100

print("The total number of missions is:", total_missions)
print("The total number of successful missions is:", successful_missions)
print(f"Success rate: {success_rate:.2f}%")
print("Missions launched before 2000:", missions_before_2000)
    