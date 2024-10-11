import pandas as pd
import random

# Load the CSV file
data = pd.read_csv("Participants.csv")

# Filter the data where 'Would you like to be a part of a random team?' is 'Yes'
filtered_data = data[data['Would you like to be a part of a random team?'] == 'Yes']

# Convert the 'Your Name' column to a list
Names = filtered_data['Your Name'].tolist()

# Shuffle the list of names to randomize the order
random.shuffle(Names)

# Initialize a list to store all the teams
teams = []

# Generate teams while there are still people left in the list
team_number = 1
while len(Names) > 1:
    # Generate a random number between 2 and 4 for the team size
    num_members = random.randint(2, 4)

    # Make sure not to form a team larger than the remaining people
    if len(Names) < num_members:
        num_members = len(Names)

    # Create the team
    team = Names[:num_members]
    teams.append(team)

    # Remove the team members from the Names list
    Names = Names[num_members:]

    # Save the team as team_n
    print(f"Team {team_number}: {team}")
    team_number += 1

# If only 1 person remains, add them to a team with 2 or 3 members
if len(Names) == 1:
    remaining_person = Names[0]

    # Try to find a team with 2 members
    for team in teams:
        if len(team) == 2:
            team.append(remaining_person)
            print(f"{remaining_person} added to a team with 2 members: {team}")
            break
    else:
        # If no team with 2 members exists, add to a team with 3 members
        for team in teams:
            if len(team) == 3:
                team.append(remaining_person)
                print(f"{remaining_person} added to a team with 3 members: {team}")
                break