import random

print("Birthday Paradox Simulation")
print("---------------------------")

people = int(input("How many people are in the group? "))
simulations = int(input("How many times do you want to run the simulation? "))

matches = 0

for simulation in range(simulations):

    birthdays = []

    for person in range(people):
        birthday = random.randint(1, 365)

        if birthday in birthdays:
            matches += 1
            break

        birthdays.append(birthday)

probability = (matches / simulations) * 100

print("\nSimulation complete!")
print("Groups tested:", simulations)
print("Groups with matching birthdays:", matches)
print("Probability of a shared birthday:", probability, "%")