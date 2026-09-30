# Project Statement

## Project Title
**Mini Voting System**

## 1. Problem Statement
Traditional voting processes require proper registration of voters, authentication, vote recording, and result calculation. For a beginner-level programming project, there is a need for a simple system that can demonstrate these basic election operations in a structured and easy-to-understand way.

The Mini Voting System is developed as a console-based Python application that allows an administrator to set up an election, register candidates and voters, authenticate voters, record votes, and display the final election results.

## 2. Scope of the Project
The scope of this project is limited to a simple, local, console-based election simulation.

The system includes:
- Election setup by an administrator.
- Candidate registration.
- Voter ID registration.
- Voter authentication.
- One-vote-per-registered-Voter-ID control during the program run.
- Vote recording and counting.
- Final result calculation.
- Tie detection.

The project does not include online voting, a database, network-based voting, biometric authentication, encryption, or a graphical user interface. It is intended for educational purposes and demonstrates basic Python programming concepts rather than being a production voting system.

## 3. Target Users
The main target users of this project are:

- **Administrators:** To set up an election, register candidates, and register voter IDs.
- **Registered Voters:** To authenticate using their Voter ID and cast their vote.
- **Students / Learners:** To understand how basic Python concepts can be combined to create a practical menu-driven application.
- **Teachers / Evaluators:** To test and demonstrate the working of the project.

## 4. High-Level Features

### 1. Admin Section
The administrator can enter the election name, register candidates, and register voter IDs.

### 2. Voter Authentication
The system checks whether the entered Voter ID is registered before allowing the user to vote.

### 3. Duplicate Vote Prevention
A set is used to store Voter IDs of voters who have already voted, preventing the same registered Voter ID from voting again during the program run.

### 4. Candidate Selection
The system displays the available candidates and allows the voter to select a candidate using the candidate number.

### 5. Vote Counting
Each valid vote increases the selected candidate's vote count by one.

### 6. Input Validation
The program handles invalid numeric inputs and invalid candidate choices.

### 7. Result Calculation
After the voting process is completed, the system displays the vote count of each candidate.

### 8. Tie Detection
If multiple candidates receive the same highest number of votes, the system reports that the election is tied between those candidates.

### 9. Controlled Section Access
The system ensures that the election must be set up before voting and that voting must be completed before results are displayed.
