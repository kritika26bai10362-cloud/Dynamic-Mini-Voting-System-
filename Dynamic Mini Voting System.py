import os
                                                                                                                         
# Global data structure to store election state
Candidates = {}
Num_of_candidates = 0
Num_of_voters = 0
Valid_VIDs = []
voted_voters = set()
is_setup_done = False
is_voting_done = False

def clear_screen():
    """Clears the terminal screen for voter privacy."""
    os.system("cls" if os.name == "nt" else "clear")

def admin():
    """Module 1: Election setup and voter registration."""
    global Candidates, Num_of_candidates, Num_of_voters, Valid_VIDs, is_setup_done
    print("\n-----ADMIN'S SECTION-----\n")
    Election_title = input("Enter election name: ")

    # Input validation for candidate count
    while True:
        try:
            Num_of_candidates = int(input("Enter the number of candidates: "))
            if Num_of_candidates > 0:
                break
            print("Number of candidates must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            
    Candidates = {}
    for i in range(0,Num_of_candidates):
        Cname = input(f"Enter the name of candidate {i+1}: ")
        Candidates[i+1] = {"Names":Cname , "Votes":0}

    # Input validation for voter count 
    while True:
        try:
            Num_of_voters = int(input("Enter the number of voters: "))
            if Num_of_voters > 0:
                break
            print("Number of voters must be greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            
    Valid_VIDs = []
    for i in range(0,Num_of_voters):
        VID = input(f"Enter the Voter ID of voter {i+1}: ")
        Valid_VIDs.append(VID)
    print("Election setup completed successfully.")
    is_setup_done = True

def voter():
    """Module 2: Voter authentication and vote casting."""
    global voted_voters, is_voting_done
    print("\n-----VOTER'S SECTION-----\n")
    V_count = 1
    while V_count <= Num_of_voters:
        ID = input("Enter your Voter ID: ")

        # Authentication and duplicate vote prevention
        if ID in voted_voters:
            print("You have already voted.")
        elif ID not in Valid_VIDs:
            print("You are not a registered voter.")
        else:
            for i in range(0,Num_of_candidates):
                print(i+1, Candidates[i+1]["Names"])
            try:
                Choice = int(input("Enter the number of candidate you want to vote for: "))
            except ValueError:
                print("Invalid input! Please enter the number corresponding to candidate.")
                continue
            
            if Choice in range(1,Num_of_candidates+1):
                Candidates[Choice]["Votes"] += 1
                V_count += 1
                voted_voters.add(ID)
                print("Your vote has been successfully recorded.")
                print("Thanks for Voting!!")
                input("\n Press Enter for the next voter...")
                clear_screen()
            else:
                print("Invalid Choice. Please vote again.")
    is_voting_done = True

def result():
    """Module 3: Result calculation and tie-breaking logic."""
    print("\n-----RESULT SECTION-----\n")
    print("*****Election Results*****")

    # Finding highest vote
    Max_votes = -1
    for i in Candidates:
        if Candidates[i]["Votes"] > Max_votes:
            Max_votes = Candidates[i]["Votes"]

    # Handling single winner or ties
    Winners = []
    for i in Candidates:
        if Candidates[i]["Votes"] == Max_votes:
            Winners.append(Candidates[i]["Names"])
            
    print("Final Vote Count:")
    for i in Candidates:
        print(Candidates[i]["Names"],":",Candidates[i]["Votes"])
        
    if len(Winners) == 1:
        print("WINNER:", Winners[0], "has won the election with", Max_votes)
    else:
        print("It's a tie between: ",end = "")
        print(" & ".join(Winners),end = " ")
        print("with",Max_votes,"votes.")
    print("Congratulations for winning the elections.")
        
print("\nMINI VOTING SYSTEM\n")
print("Welcome to Mini Voting System.")

# Main navigaton loop
while True:
    print("\n-----Voting System Menu-----")                 
    print("1. Admin's Section")
    print("2. Voter's Section")
    print("3. Result Section")

    try:
        choice = int(input("Enter the number of section you want to choose: "))
    except ValueError:
        print("Invalid input! Please enter a valid number(1,2, or 3).")
        continue
    if choice == 1:
        admin()
    elif choice == 2:
        if not is_setup_done:
            print("Access Denied! You need to go to Admin Section first to setup the election.")
        else:
            voter()
    elif choice == 3:
        if not is_setup_done:
            print("Access Denied! No election has been setup yet. Go to Admin Section first.")
        elif not is_voting_done:
            print("Access Denied! Voting process is not completed yet. Please complete the Voter's Section first.")
        else:
            result()
            break  
    else:
        print("Invalid Choice! Please enter a number between 1 to 3.")

print("Thank You for using the voting system!!")
    



