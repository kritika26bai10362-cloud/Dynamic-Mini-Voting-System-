# Mini Voting System

## Project Title
**Mini Voting System**

## Overview of the Project
The Mini Voting System is a menu-driven Python project that simulates a simple election process. It is divided into three main sections: **Admin's Section, Voter's Section, and Result Section**.

The Admin sets up the election by entering the election name, registering candidates, and registering voter IDs. Registered voters can then authenticate themselves using their Voter ID and cast their vote for one of the available candidates. After all registered voters have voted, the system displays the final vote count and declares the winner or reports a tie.

The project is designed as a simple console-based application for understanding basic Python programming concepts.

## Features
- Menu-driven voting system.
- Admin section for election setup.
- Registration of candidates and voter IDs.
- Voter ID authentication.
- Prevention of duplicate voting using a set.
- Display of registered candidates during voting.
- Vote counting for each candidate.
- Validation of candidate and numeric inputs.
- Voting continues until all registered voters have voted.
- Final result and vote count display.
- Tie detection when two or more candidates receive the highest number of votes.
- Screen clearing between voters to provide basic voting privacy.
- Access control for the Admin, Voter, and Result sections.
- Thank-you message after the election process is completed.

## Technologies / Tools Used
- **Programming Language:** Python
- **Development Environment:** Python IDLE / Python-compatible terminal
- **Python Concepts Used:**
  - Variables
  - Dictionaries
  - Lists
  - Sets
  - Functions
  - `while` loops
  - `for` loops
  - `if-elif-else` statements
  - `try-except` for input validation
  - Global variables
- **Python Module Used:** `os` for clearing the terminal screen.

## Steps to Install & Run the Project

### Step 1: Install Python
Install Python on the computer if it is not already installed.

### Step 2: Save the Program
Save the Python program with a `.py` extension, for example:

```text
voting_system.py
```

### Step 3: Open the Program
Open the file using Python IDLE or another Python-compatible editor.

### Step 4: Run the Program
Run the Python file.

The program will display:

```text
MINI VOTING SYSTEM
Welcome to Mini Voting System.
```

### Step 5: Follow the Menu
Choose the required section:

```text
1. Admin's Section
2. Voter's Section
3. Result Section
```

Complete the Admin section first, followed by the Voter section, and finally open the Result section.

## Instructions for Testing

### Test 1: Election Setup
1. Select **1. Admin's Section**.
2. Enter an election name.
3. Enter the number of candidates.
4. Enter candidate names.
5. Enter the number of voters.
6. Enter the Voter IDs.
7. Check that the message **"Election setup completed successfully."** is displayed.

### Test 2: Valid Voting
1. Select **2. Voter's Section**.
2. Enter a registered Voter ID.
3. Select a valid candidate number.
4. Check that the vote is recorded successfully.
5. Repeat for the remaining registered voters.

### Test 3: Invalid Voter ID
Enter a Voter ID that was not registered by the Admin.

Expected result:

```text
You are not a registered voter.
```

### Test 4: Duplicate Voting
After a voter has successfully voted, enter the same Voter ID again.

Expected result:

```text
You have already voted.
```

### Test 5: Invalid Candidate Choice
Enter a candidate number that is not present in the candidate list.

Expected result:

```text
Invalid Choice. Please vote again.
```

### Test 6: Result Section
After all registered voters have voted, select **3. Result Section**.

The program should display:
- Final vote count of every candidate.
- The winner when there is one candidate with the highest number of votes.
- A tie message when two or more candidates have the same highest number of votes.

## Screenshots
Screenshots of the following stages can be added to this README:
1. Main Menu
2. Admin Section
3. Voter Section
4. Vote Recorded Message
5. Final Election Results
6. Tie Result (if tested)

## Project Flow

**Admin Section → Voter Section → Result Section → Thank You Message**

The Result Section can be accessed only after the election has been set up and the voting process has been completed.
