PROJECT SPECIFICATION 

# **The House Always Wins** 

_A Monte Carlo Simulation of Gambling Outcomes Using PyTorch_ 

|**Document type**|Probation project specification|**Revision**|1.0|
|---|---|---|---|
|**Prepared by**|Morgan Blue|**Date**|5 November 2026|
|**Participants**|Mielle, Fafams, Ivan|**Duration**|6 hours, single session|



## **1. Purpose** 

This document specifies a six-hour team project to be completed as a condition of probation. The participants will build a Monte Carlo simulation in PyTorch that models a large population of gamblers and measures, with data, what happens to their money over time. 

The project also develops skills used throughout machine learning: random sampling, vectorized tensor operations, expected value, the law of large numbers, and data visualization. 

## **2. Assignments** 

Each participant owns one part and is assessed on that part individually. The three parts must integrate into a single working project. 

|**Part**|**Owner**|**Responsibility**|
|---|---|---|
|A|Mielle|Simulation engine|
|B|Fafams|Statistical analysis|
|C|Ivan|Visualization and written report|



## **3. Simulation Parameters** 

|**Parameter**|**Value**|
|---|---|
|Game|European roulette, even-money bet on red|
|Probability of winning|18/37 (approximately 48.65%)|
|Starting bankroll|₱1,000 per player|
|Stake|₱50 per round|
|Maximum rounds|1,000 per player; a player who reaches ₱0 stops|
|Population|10,000 players, simulated concurrently|



Page 1 of 4 

Prepared by Morgan Blue 

_The House Always Wins: Project Specification_ 

_Revision 1.0_ 

## **4. Requirements** 

### **4.1 Part A: Simulation Engine (Mielle)** 

|**ID**|**Requirement**|
|---|---|
|A-1|Implement`simulate(n_players, start, bet, p_win, max_rounds)`in PyTorch.|
|A-2|The implementation shall be vectorized across players. A loop over rounds is permitted; a loop over<br>players is not.|
|A-3|A player whose bankroll reaches ₱0 shall stop betting. No bankroll may fall below 0.|
|A-4|The function shall return a bankroll history tensor of shape`[n_players, max_rounds + 1]`.|
|A-5|A fixed random seed shall be used so that results are reproducible.|



_Acceptance:_ a run of 10,000 players over 1,000 rounds completes in under one minute, and a fair game (p = 0.5) keeps the mean bankroll near ₱1,000. 

### **4.2 Part B: Statistical Analysis (Fafams)** 

|**ID**|**Requirement**|
|---|---|
|B-1|Derive the theoretical expected value per bet and compare it with the mean result observed in the<br>simulation.|
|B-2|Report the percentage of players at ₱0 after 100, 500, and 1,000 rounds.|
|B-3|Report the percentage of players who finish above their starting bankroll.|
|B-4|Repeat the simulation with a fair game (p = 0.5) and compare the outcomes, demonstrating that the house<br>edge is the cause of the losses.|
|B-5|Simulate the Martingale strategy (doubling the stake after each loss) and determine whether it overcomes<br>the house edge.|



_Acceptance:_ every reported figure is produced by code; no figure is calculated by hand. 

### **4.3 Part C: Visualization and Report (Ivan)** 

|**ID**|**Requirement**|
|---|---|
|C-1|Line chart of 50 sample players' bankrolls over time.|
|C-2|Line chart of the percentage of players at ₱0, by round.|
|C-3|Histogram of final bankrolls.|
|C-4|Line chart comparing mean bankroll over time for roulette and a fair game.|
|C-5|A written report of one to two pages covering the setup, the results, the interpretation of each chart, and an<br>explanation of why the house always wins.|



_Acceptance:_ a reader who has not seen the code can understand the result from the charts and report alone. 

Page 2 of 4 

Prepared by Morgan Blue 

_The House Always Wins: Project Specification_ 

_Revision 1.0_ 

### **4.4 Individual Reflection (All Participants)** 

Each participant shall write a reflection of approximately half a page, independently, addressing the following: 

|**No.**|**Question**|
|---|---|
|1|What surprised you in the results?|
|2|What did you learn about PyTorch or probability?|
|3|What does this change about how you think about gambling?|



## **5. Schedule** 

|**Time**|**Activity**|
|---|---|
|0:00 – 0:30|Kickoff. Review this specification and agree on the function interface.|
|0:30 – 2:30|Mielle builds the simulation engine. Fafams and Ivan develop against placeholder data of the same<br>tensor shape.|
|2:30 – 4:30|Integration. Run the full simulations, analysis, and charts.|
|4:30 – 5:30|Report, individual reflections, and presentation slides.|
|5:30 – 6:00|Final review and submission.|



## **6. Rules** 

|**No.**|**Rule**|
|---|---|
|1|Each participant writes their own part. Assisting one another with debugging is permitted.|
|2|AI tools may not be used to write code.|
|3|PyTorch shall be used for simulation and analysis; Matplotlib for charts.|
|4|Each participant must be able to explain every line of their own part.|
|5|Late or missing work counts against the responsible participant's probation.|



## **7. Deliverables** 

|**No.**|**Deliverable**|**Owner**|
|---|---|---|
|1|Simulation engine source code|Mielle|
|2|Analysis source code and results|Fafams|
|3|Four charts and written report|Ivan|
|4|Individual reflections|All|
|5|Ten-minute presentation to the engineers|All|



Page 3 of 4 

Prepared by Morgan Blue 

_The House Always Wins: Project Specification_ 

_Revision 1.0_ 

## **8. Evaluation** 

|**Criterion**|**Description**|**Weight**|
|---|---|---|
|Correctness|Simulation and reported figures are accurate|40%|
|Code quality|Vectorized, clean, and reproducible|20%|
|Clarity|Charts and report are easy to understand|20%|
|Presentation and reflection|Demonstrated understanding and honest reflection|20%|



## **9. Acknowledgement** 

By signing below, each participant confirms that they have read this specification and accept its terms as a condition of probation. 

|**Name**|**Signature**|**Date**|
|---|---|---|
|Mielle|||
|Fafams|||
|Ivan|||



Morgan Blue 

Page 4 of 4 

Prepared by Morgan Blue 

