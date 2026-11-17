# SPPU SE AI & DS - Artificial Intelligence Practicals 1-9: Complete Typed Notes

> Text-only study document for GitHub. Practical-wise explanations are also available in each practical folder. Python programs are separate `.py` files so they can be run directly.

## How to use this collection
1. Read the practical-wise README for aim, problem statement, objectives, theory, algorithm, complexity, expected output and viva answers.
2. For Practicals 1-6, open and run the linked Python source file.
3. For Practicals 7-9, follow the typed activity worksheet and complete the observation table using the tool currently available to you.
4. Read `SOURCE-MATERIAL-NOTES.md` for the distinction between information taken from supplied materials and prepared example code.


---

# Practical 01 Expert System
## Expert System Using Rule-Based System (RBS) in AI

## Aim
Build a simple expert system using rules to provide simple decision-making advice.

## Problem statement
Develop an expert system using a Rule-Based System. The notebook frames this as a simple decision-making expert system; the included demonstration domain is computer troubleshooting.

## Objectives
- Understand the concept of an expert system and rule-based system.
- Represent knowledge as facts and IF-THEN rules.
- Apply rules to known facts to infer a recommendation.

## Theory
1. An expert system is an AI program that uses stored domain knowledge to provide advice or decisions in a limited subject area.
2. A rule-based system represents knowledge using IF-THEN rules. The IF part is the condition and the THEN part is the conclusion or action.
3. A fact is information supplied by the user or already known to the system. An inference engine checks rules against facts and fires matching rules.
4. A knowledge base stores rules and facts; an inference engine applies them. Forward chaining starts from facts and derives conclusions. Backward chaining starts from a goal and checks whether supporting facts are true.

## Algorithm / Procedure
1. Start the program.
2. Ask the user a small set of yes/no questions and store the answers as facts.
3. Compare the known facts with conditions in the rule base.
4. When all conditions of a rule match, display its conclusion.
5. If no rule matches, request more information or display a fallback message.
6. Stop.

## Complexity / Practical nature
For R rules with up to C conditions per rule, the simple sequential rule check is O(R x C) time. Space is O(F + R), where F is the number of stored facts.

## Expected output / record
Example: answer n to “Does the computer power on?” The system reports that the computer does not power on and recommends checking the socket, cable, adapter and battery.

## Python program
Source file: [`practical_01_rule_based_expert_system.py`](practical_01_rule_based_expert_system.py)

### Run
```bash
python practical_01_rule_based_expert_system.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is an expert system?**
Answer: An AI program that uses stored expert knowledge and rules to solve problems in a specific domain.

**Q2. What is a rule-based system?**
Answer: A system that represents knowledge as IF-THEN rules.

**Q3. What is a knowledge base?**
Answer: The collection of facts and rules used by the expert system.

**Q4. What is an inference engine?**
Answer: The component that matches facts with rules and derives conclusions.

**Q5. What is a fact?**
Answer: A known piece of information, usually supplied by the user or stored in the system.

**Q6. What is forward chaining?**
Answer: A data-driven method that starts with facts and applies rules to derive new facts or conclusions.

**Q7. What is backward chaining?**
Answer: A goal-driven method that starts with a possible conclusion and checks whether its conditions can be proved.

**Q8. Why is this example not a general AI system?**
Answer: It uses a limited set of manually written rules for one narrow troubleshooting domain.

**Q9. What happens if no rule matches?**
Answer: The system returns a fallback message saying that there is not enough information.

**Q10. Give one advantage and one limitation of an RBS.**
Answer: It is easy to explain and audit; however, it only handles cases covered by its rules.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.


---

# Practical 02 BFS DFS Maze
## Implementation of Search Algorithms (BFS and DFS) for Maze Solving

## Aim
Implement BFS and DFS maze solvers using graph search.

## Problem statement
Implement AI search algorithms BFS and DFS to solve a maze, as written in the Practical 2 notebook.

## Objectives
- Understand graph traversal and search.
- Implement Breadth-First Search and Depth-First Search.
- Compare the routes found by BFS and DFS in a maze.

## Theory
1. A maze can be represented as a graph: each open cell is a vertex and each legal move is an edge.
2. BFS explores nodes level by level using a queue. In an unweighted maze, BFS finds a path with the minimum number of moves.
3. DFS explores one branch deeply before backtracking, typically using a stack or recursion. DFS can find a route but does not guarantee a shortest route.
4. A visited set prevents repeated exploration and infinite loops. A parent map is used to reconstruct the path.

## Algorithm / Procedure
1. Find the start cell S and goal cell E.
2. Treat every non-wall cell as a graph vertex and connect up, down, left and right neighbours.
3. For BFS, place S in a queue. For DFS, place S on a stack.
4. Remove the next cell from the frontier. If it is E, reconstruct the path using parent links.
5. Add every valid unvisited neighbour to the frontier and record its parent.
6. Repeat until E is reached or the frontier becomes empty.

## Complexity / Practical nature
For V open cells and E legal neighbour connections, both BFS and DFS take O(V + E) time and O(V) auxiliary space. In a grid maze, V is at most rows x columns.

## Expected output / record
The program prints a route and move count for both BFS and DFS and shows the route cells marked with *.

## Python program
Source file: [`practical_02_bfs_dfs_maze_solver.py`](practical_02_bfs_dfs_maze_solver.py)

### Run
```bash
python practical_02_bfs_dfs_maze_solver.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is a graph?**
Answer: A set of vertices connected by edges.

**Q2. What is BFS?**
Answer: Breadth-First Search explores all neighbours at the current depth before moving deeper.

**Q3. Which data structure is used by BFS?**
Answer: A queue (FIFO).

**Q4. What is DFS?**
Answer: Depth-First Search explores one branch as far as possible before backtracking.

**Q5. Which data structure is used by iterative DFS?**
Answer: A stack (LIFO).

**Q6. Which algorithm finds the shortest path in an unweighted graph?**
Answer: BFS.

**Q7. Does DFS always find the shortest path?**
Answer: No. It finds a path if one exists, but the path may not be shortest.

**Q8. Why is a visited set required?**
Answer: To avoid processing the same cell repeatedly and prevent cycles.

**Q9. What is the purpose of the parent dictionary?**
Answer: It stores the predecessor of each discovered cell so that the path can be reconstructed.

**Q10. What is the time complexity of BFS and DFS?**
Answer: O(V + E) using adjacency-list-style traversal.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.


---

# Practical 03 A Star Search
## Implementation of A* Search Algorithm

## Aim
Implement the A* algorithm to solve an AI search problem using graph search.

## Problem statement
Implement an A* search algorithm to solve an AI search problem using graph search, following the Practical 3 notebook.

## Objectives
- Understand informed or heuristic search.
- Represent a weighted problem as a graph.
- Use path cost and heuristic estimates to select promising states.

## Theory
1. A* is an informed search algorithm that selects the node with the lowest estimated total cost.
2. It uses f(n) = g(n) + h(n), where g(n) is the cost from the start node to n and h(n) estimates the remaining cost from n to the goal.
3. The frontier is maintained as a priority queue. The algorithm updates a node if a less expensive route to it is found.
4. An admissible heuristic never overestimates the true remaining cost. With suitable conditions (including an admissible heuristic and correct graph-search handling), A* can find an optimal path.

## Algorithm / Procedure
1. Initialize the priority queue with the start node and f(start) = h(start).
2. Set g(start) = 0 and record no parent for the start.
3. Remove the frontier node with the smallest f score.
4. If it is the goal, reconstruct the path from the parent links.
5. For each neighbour, calculate tentative_g = g(current) + edge_cost.
6. If tentative_g is better than the recorded cost, update its cost and parent and push it with f = g + h.
7. If the frontier becomes empty, report that no path exists.

## Complexity / Practical nature
A* worst-case time and space are exponential in search depth in general; performance depends strongly on branching factor and heuristic quality. A priority-queue implementation adds logarithmic heap operations per insertion/removal.

## Expected output / record
The supplied graph example returns the path S -> A -> C -> G with total path cost 7.

## Python program
Source file: [`practical_03_a_star_search.py`](practical_03_a_star_search.py)

### Run
```bash
python practical_03_a_star_search.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is informed search?**
Answer: Search that uses additional problem knowledge, usually a heuristic, to guide exploration.

**Q2. What is A*?**
Answer: A best-first search algorithm that orders nodes using f(n) = g(n) + h(n).

**Q3. What is g(n)?**
Answer: The actual path cost from the start node to node n.

**Q4. What is h(n)?**
Answer: An estimate of the remaining cost from node n to the goal.

**Q5. What is f(n)?**
Answer: The estimated total solution cost through n: g(n) + h(n).

**Q6. What is an admissible heuristic?**
Answer: A heuristic that never overestimates the true minimum remaining cost.

**Q7. Which data structure is commonly used for the open list?**
Answer: A priority queue or min-heap.

**Q8. What happens if h(n) = 0 for every node?**
Answer: A* behaves like uniform-cost search.

**Q9. Why store parent links?**
Answer: To reconstruct the final path after reaching the goal.

**Q10. Can A* performance depend on the heuristic?**
Answer: Yes. A more informative admissible heuristic can reduce the number of explored nodes.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.


---

# Practical 04 Constraint Satisfaction
## Implementation of Constraint Satisfaction Problem (CSP) in AI

## Aim
Implement a CSP solution for a real-world style problem such as map colouring, Sudoku or timetable scheduling, using backtracking and constraints.

## Problem statement
Implement a Constraint Satisfaction Problem in AI. The notebook mentions map colouring, Sudoku and timetable scheduling and calls out backtracking and constraint programming.

## Objectives
- Understand CSP variables, domains and constraints.
- Study recursion, backtracking, forward checking and consistency.
- Understand MRV and LCV heuristics.
- Apply CSP ideas to map colouring, Sudoku and timetable scheduling.

## Theory
1. A CSP consists of variables, domains and constraints. A solution assigns a value to every variable while satisfying all constraints.
2. In map colouring, each region is a variable, available colours form its domain, and neighbouring regions must have different colours.
3. Backtracking assigns one variable at a time. If an assignment causes a conflict, the algorithm undoes it and tries another value.
4. Forward checking removes values that are no longer possible for neighbouring unassigned variables and detects failure early.
5. MRV (Minimum Remaining Values) selects the unassigned variable with the fewest legal values. LCV (Least Constraining Value) tries the value that restricts neighbours least.

## Algorithm / Procedure
1. Define map regions as variables, colours as domains and neighbouring relationships as constraints.
2. Select an unassigned region using MRV.
3. Order its legal colours using LCV.
4. Assign one colour and run forward checking.
5. If all unassigned regions still have at least one legal colour, recursively assign the next region.
6. If a conflict is found, remove the assignment and try the next colour.
7. Stop when all regions are assigned or no solution is possible.

## Complexity / Practical nature
Backtracking CSP search is exponential in the number of variables in the worst case. MRV, LCV and forward checking are heuristics/propagation methods that reduce the search in many practical cases but do not remove the worst-case exponential bound.

## Expected output / record
The program prints a valid colour for each region in the Australia map-colouring example and verifies that every pair of neighbouring regions has different colours.

## Python program
Source file: [`practical_04_csp_map_coloring.py`](practical_04_csp_map_coloring.py)

### Run
```bash
python practical_04_csp_map_coloring.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is a CSP?**
Answer: A problem defined by variables, domains and constraints.

**Q2. What are variables in map colouring?**
Answer: The map regions.

**Q3. What is a domain?**
Answer: The set of allowed values for a variable, such as Red, Green and Blue.

**Q4. What is a constraint?**
Answer: A condition that restricts which combinations of values are allowed.

**Q5. What is backtracking?**
Answer: A search technique that assigns values and undoes an assignment when it leads to failure.

**Q6. What is forward checking?**
Answer: After an assignment, it removes inconsistent values from neighbouring unassigned variables and detects empty domains.

**Q7. What is MRV?**
Answer: Minimum Remaining Values: choose the variable with the fewest legal values remaining.

**Q8. What is LCV?**
Answer: Least Constraining Value: choose the value that rules out the fewest choices for neighbouring variables.

**Q9. Why can CSP search become expensive?**
Answer: The number of possible assignments can grow exponentially with the number of variables.

**Q10. Give examples of CSP applications.**
Answer: Map colouring, Sudoku, exam timetabling, staff scheduling and resource allocation.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.


---

# Practical 05 Minimax
## Implementation of Minimax Algorithm for Two-Player Deterministic Games

## Aim
Implement the Minimax algorithm for two-player deterministic games.

## Problem statement
Understand and implement the basic Minimax algorithm for a two-player deterministic game. The notebook discusses adversarial search and examples such as Chess and Tic-Tac-Toe.

## Objectives
- Understand adversarial search in competitive environments.
- Represent possible moves using a game tree.
- Evaluate terminal states and select a move assuming the opponent also plays optimally.

## Theory
1. Adversarial search is used when players have conflicting goals. In a zero-sum game, one player’s gain is the other player’s loss.
2. Minimax assumes both players play optimally. MAX chooses the largest child value; MIN chooses the smallest child value.
3. Terminal game states are assigned utility values. In the included Tic-Tac-Toe example, X win = +1, O win = -1 and draw = 0.
4. The algorithm recursively explores possible moves, evaluates terminal states and propagates values back up the game tree.

## Algorithm / Procedure
1. Check whether the current board is a terminal state. If X wins, return +1; if O wins, return -1; if draw, return 0.
2. If it is MAX’s turn, try every empty cell as X and return the maximum recursive score.
3. If it is MIN’s turn, try every empty cell as O and return the minimum recursive score.
4. Undo each trial move before checking the next possibility.
5. For each legal move available to X, calculate its Minimax value and select the move with the highest score.

## Complexity / Practical nature
With branching factor b and search depth d, basic Minimax takes O(b^d) time. Recursive space is O(d), excluding the board representation and move-generation overhead.

## Expected output / record
For the included board, X has an immediate winning move at cell 7 (1-based indexing), so the program prints best move = 7 and score = +1.

## Python program
Source file: [`practical_05_minimax_tictactoe.py`](practical_05_minimax_tictactoe.py)

### Run
```bash
python practical_05_minimax_tictactoe.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is Minimax?**
Answer: A decision algorithm for two-player games that maximizes the minimum guaranteed payoff.

**Q2. What is adversarial search?**
Answer: Search where an agent chooses actions while considering an opponent with conflicting goals.

**Q3. What is a game tree?**
Answer: A tree whose nodes are game states and whose edges represent legal moves.

**Q4. Who is MAX?**
Answer: The player who tries to maximize the utility value.

**Q5. Who is MIN?**
Answer: The opponent who tries to minimize the utility value.

**Q6. What is a utility function?**
Answer: A function that assigns a numerical value to a terminal or evaluated game state.

**Q7. What does zero-sum mean?**
Answer: One player’s gain is balanced by the other player’s loss.

**Q8. Why is recursion used?**
Answer: Each possible move creates a new game state, so the same evaluation procedure can be applied to the child state.

**Q9. What is the main limitation of Minimax?**
Answer: It can explore a very large game tree and become slow for games with high branching factors.

**Q10. What are the utility values used here?**
Answer: X win = +1, O win = -1 and draw = 0.

## Source alignment note
Your notebook photograph shows the practical title/aim/objectives but does not include the full program pages. The Python program in this folder is a prepared, runnable implementation of the topic (not a verbatim transcription of unseen handwritten code). Check it against any class-specific code your instructor supplied.


---

# Practical 06 Minimax Alpha Beta
## Implementation of Minimax Algorithm with Alpha-Beta Pruning in AI

## Aim
Implement Minimax with Alpha-Beta Pruning to reduce computation time.

## Problem statement
Enhance Minimax using Alpha-Beta pruning to reduce computation time, as stated in Practical 6.

## Objectives
- Use recursion and backtracking in decision-making for games.
- Understand MAX and MIN nodes, game trees and utility values.
- Use alpha and beta bounds to remove branches that cannot affect the final decision.
- Understand that pruning improves efficiency without changing the Minimax result.

## Theory
1. Alpha-Beta pruning is an optimization of Minimax. It skips branches that cannot change the final decision.
2. Alpha (α) is the best value MAX can guarantee so far. It starts at negative infinity and can only increase.
3. Beta (β) is the best value MIN can guarantee so far. It starts at positive infinity and can only decrease.
4. When α >= β, the remaining children of the current node can be pruned.
5. The pruning result is the same as Minimax. The amount of work saved depends on move ordering.

## Algorithm / Procedure
1. Start with α = -infinity and β = +infinity.
2. At a MAX node, evaluate children, update the best value and α = max(α, best).
3. At a MIN node, evaluate children, update the best value and β = min(β, best).
4. Whenever α >= β, stop exploring the remaining children of that node.
5. Return the node’s Minimax value and select the move with the highest value for X.

## Complexity / Practical nature
Worst-case time remains O(b^d), similar to Minimax. With ideal move ordering, the effective search can approach O(b^(d/2)). Recursive space is O(d).

## Expected output / record
The program recommends cell 7 for X on the included example board, with score +1, and also reports the number of recursive nodes evaluated.

## Python program
Source file: [`practical_06_minimax_alpha_beta.py`](practical_06_minimax_alpha_beta.py)

### Run
```bash
python practical_06_minimax_alpha_beta.py
```

The program uses only Python's standard library; no external package installation is needed.

## Oral / viva questions with answers
**Q1. What is Alpha-Beta pruning?**
Answer: An optimization that skips Minimax branches that cannot affect the final decision.

**Q2. What is alpha?**
Answer: The best lower-bound value MAX can guarantee so far.

**Q3. What is beta?**
Answer: The best upper-bound value MIN can guarantee so far.

**Q4. What is the pruning condition?**
Answer: Prune when alpha is greater than or equal to beta.

**Q5. Does pruning change the optimal move?**
Answer: No. It produces the same Minimax decision while evaluating fewer nodes.

**Q6. What are the initial alpha and beta values?**
Answer: Alpha = negative infinity and beta = positive infinity.

**Q7. Which node updates alpha?**
Answer: MAX nodes.

**Q8. Which node updates beta?**
Answer: MIN nodes.

**Q9. What is the worst-case time complexity?**
Answer: O(b^d), the same asymptotic bound as Minimax.

**Q10. When is pruning most effective?**
Answer: When the best moves are examined early, giving good move ordering.

## Source alignment note
This runnable Tic-Tac-Toe demonstration implements the Minimax + Alpha-Beta topic described in the supplied Practical 6 PDF. It is a complete teaching implementation and may be longer/different from the short illustrative code fragment in the manual.


---

# Practical 07 ChatGPT
## Exploration and Practice of ChatGPT and Its Applications

## Aim
Implement and practice the use of ChatGPT as a tool within Artificial Intelligence.

## Problem statement
Assignment and practice of ChatGPT and its usage.

## Objectives
- Understand AI and NLP concepts used by ChatGPT.
- Explore the role of Transformer-based Large Language Models.
- Develop effective prompting strategies.
- Apply ChatGPT to summarization, translation, programming assistance and problem-solving.
- Evaluate limitations, bias and responsible use.

## Theory
1. ChatGPT is a conversational AI system based on GPT (Generative Pre-trained Transformer) language-model technology.
2. A prompt is the instruction or context supplied by the user. Clear prompts include the task, context, constraints and desired format.
3. A Large Language Model is trained on large text collections to learn language patterns and generate text. Transformer architecture uses attention mechanisms to process relationships among tokens.
4. Typical tasks include content generation, summarization, translation, coding assistance, explanation and brainstorming.
5. Outputs can contain incorrect statements or bias. Users should verify important facts and avoid sharing private or confidential data.

## Algorithm / Procedure
1. Open the authorised ChatGPT application or website and sign in if required.
2. Enter a clear prompt for a selected task, such as summarization, translation or code explanation.
3. Review the generated answer for relevance, completeness and correctness.
4. Improve the prompt by adding context, constraints or output-format requirements.
5. Compare the first and improved response.
6. Record the task, prompts, observations and limitations.

## Complexity / Practical nature
This is a tool-exploration practical rather than a local algorithm implementation. Model inference cost depends on model architecture, input/output tokens and serving infrastructure; no fixed classroom time complexity applies.

## Expected output / record
Record at least three prompt experiments (for example summarization, translation and code explanation), compare outputs and note any corrections or verification performed.

## Practical activity worksheet
See [`practical_07_tool_activity.md`](practical_07_tool_activity.md) for a guided demonstration, prompt examples and record sheet.

## Oral / viva questions with answers
**Q1. What is ChatGPT?**
Answer: A conversational AI assistant based on large language-model technology.

**Q2. What does GPT stand for?**
Answer: Generative Pre-trained Transformer.

**Q3. What is NLP?**
Answer: Natural Language Processing, a field of AI concerned with processing and generating human language.

**Q4. What is an LLM?**
Answer: A Large Language Model trained on large amounts of text to understand and generate language.

**Q5. What is a prompt?**
Answer: The instruction or context given to an AI model.

**Q6. What is prompt engineering?**
Answer: Designing and refining prompts to obtain more useful and relevant outputs.

**Q7. Name two uses of ChatGPT.**
Answer: Summarization and programming assistance; it can also translate, explain and brainstorm.

**Q8. What is a hallucination?**
Answer: An output that sounds plausible but contains false or unsupported information.

**Q9. Why should AI answers be checked?**
Answer: The model can make errors, omit context or reflect bias.

**Q10. What is responsible use?**
Answer: Verify important claims, protect private data, respect policies and disclose AI assistance when required.

## Source alignment note
The supplied practical is a tool-exploration activity rather than a Python-programming assignment. The folder therefore contains a demonstration worksheet and oral preparation, not an unrelated fabricated Python script.


---

# Practical 7 - ChatGPT exploration worksheet

## Aim
Practice the use of ChatGPT as an AI tool.

## Setup
Use the official ChatGPT application or website with an account permitted by your institution. Do not enter passwords, private student data, confidential documents or sensitive personal information.

## Demonstration 1: Prompt quality
**Prompt A (vague):** `Explain AI.`

**Prompt B (specific):** `Explain Artificial Intelligence to a second-year engineering student in 120 words. Give one definition, three applications and one limitation. Use simple English.`

Record which response is more focused and why.

## Demonstration 2: Summarization
Prompt: `Summarize the following paragraph in five bullet points. Preserve all important facts and do not add new information: [paste a short, non-sensitive paragraph].`

Check whether the summary preserves the meaning.

## Demonstration 3: Translation
Prompt: `Translate the following paragraph from English to Marathi. Keep technical terms in English where appropriate: [paste sample paragraph].`

Check terminology and meaning; do not assume every translation is perfect.

## Demonstration 4: Programming assistance
Prompt: `Explain this short Python program line by line. Then identify one possible input error and suggest a correction: [paste a small practice program].`

Run and independently verify any code before trusting it.

## Demonstration 5: Critical evaluation
Ask ChatGPT a factual question whose answer can be checked from a textbook or official source. Compare the response with the source and record any errors, omissions or uncertainty.

## Suggested record table
| Task | Prompt used | What the tool returned | How you checked it |
|---|---|---|---|
| Explanation | | | |
| Summarization | | | |
| Translation | | | |
| Code explanation | | | |

## Key observations
- Clear instructions and context generally improve relevance.
- Outputs can contain errors, bias or fabricated details.
- Human verification remains important, especially for academic, technical or high-impact use.
- Respect academic integrity and your institution's AI-use policy.

## Conclusion
ChatGPT was explored for explanation, summarization, translation and programming assistance. Its output was evaluated critically for relevance and accuracy.


---

# Practical 08 Sora
## Exploration and Practice of Sora

## Aim
Implement and practice the use of Sora as an AI tool within Artificial Intelligence.

## Problem statement
Assignment and practice of Sora.

## Objectives
- Understand AI-driven video generation.
- Explore the workflow of text-to-video generation.
- Study prompt design and video controls.
- Observe capabilities, limitations and ethical concerns.

## Theory
1. Sora is a generative AI video model that creates video content from user instructions and supported visual inputs.
2. Prompt engineering is the process of describing the subject, action, environment, camera viewpoint, visual style, lighting and desired motion clearly.
3. A generated video should be reviewed for temporal consistency, object motion, scene continuity, prompt relevance and visual quality.
4. The supplied manual describes text prompts, image prompts and video prompts and mentions editing operations such as re-cut, remix, blend and loop. Exact controls and availability can change over time.
5. Responsible use includes avoiding deceptive impersonation, clearly labelling synthetic media when appropriate and respecting people’s rights.

## Algorithm / Procedure
1. Access Sora only through an official account and currently supported interface.
2. Enter a descriptive text prompt or provide a supported image/video input.
3. Choose the available aspect ratio, duration, resolution and other settings shown in the current interface.
4. Generate the video and wait for processing to finish.
5. Review motion, consistency, visual quality and alignment with the prompt.
6. Try a revised prompt or an available editing control such as remix or loop.
7. Save the prompt, settings and observations for the practical record.

## Complexity / Practical nature
This is a hosted generative-media tool activity, not a local Python algorithm practical. Generation time and resource usage depend on the service and selected settings.

## Expected output / record
Record the prompt, selected generation settings, description of the generated clip, observations and any improvements made after revising the prompt.

## Practical activity worksheet
See [`practical_08_tool_activity.md`](practical_08_tool_activity.md) for a guided demonstration, prompt examples and record sheet.

## Oral / viva questions with answers
**Q1. What is Sora?**
Answer: A generative AI system for creating video from prompts and supported visual inputs.

**Q2. What is text-to-video generation?**
Answer: Generating a video clip from a natural-language description.

**Q3. What is prompt engineering in video generation?**
Answer: Writing clear instructions about subject, actions, setting, camera, style and motion.

**Q4. What is an image prompt?**
Answer: An image supplied as a visual reference or starting point for generating video.

**Q5. What is a video prompt?**
Answer: A video input or instruction used to guide generation or transformation, where supported.

**Q6. What should you check in the output?**
Answer: Whether the clip follows the prompt, motion is coherent, objects remain consistent and visual quality is acceptable.

**Q7. Name two video-editing controls discussed in the manual.**
Answer: Examples include re-cut, remix, blend and loop.

**Q8. Why can generated motion look unrealistic?**
Answer: The model may not perfectly maintain physical relationships or temporal consistency.

**Q9. What is a deepfake risk?**
Answer: Synthetic media can misrepresent a person or event and be used to deceive.

**Q10. Why should old interface instructions be treated carefully?**
Answer: Product availability, menus and generation settings can change by account, region and time.

## Source alignment note
The supplied practical is a tool-exploration activity rather than a Python-programming assignment. The folder therefore contains a demonstration worksheet and oral preparation, not an unrelated fabricated Python script.


---

# Practical 8 - Sora exploration worksheet

## Aim
Explore the use of Sora as an AI video-generation tool.

## Important access note
The supplied lab manual contains interface and availability details that may have changed. Use only the current official product interface and an account/location where access is officially available. Do not rely on dated menu screenshots or instructions to bypass regional restrictions.

## Prompt structure
A useful video prompt describes:
1. Subject or main character.
2. Action or movement.
3. Environment and background.
4. Camera position or movement.
5. Lighting, colour palette and visual style.
6. Desired duration/aspect ratio where those settings are available.

## Prompt experiment A - simple scene
`A red bicycle rolls slowly along a quiet tree-lined road at sunrise. Gentle camera tracking from the side, warm natural light, realistic cinematic style, smooth motion.`

## Prompt experiment B - detailed scene
`Wide cinematic shot of a small wooden boat moving across a calm lake at dawn. Light mist above the water, distant green hills, subtle ripples behind the boat, slow forward camera movement, soft golden light, natural realistic colours.`

## Procedure
1. Open the official Sora interface if available to your account.
2. Enter Prompt A and review the generation settings currently offered.
3. Generate the clip and wait for completion.
4. Review subject consistency, motion, camera behaviour, background stability and prompt relevance.
5. Revise the prompt with more precise motion or camera instructions and generate another version if permitted.
6. Compare the two results and record the differences.
7. Explore editing controls that are currently visible in the interface. The supplied manual mentions re-cut, remix, blend and loop; names and availability can change.

## Evaluation checklist
- Does the clip show the requested subject?
- Is the action understandable and physically plausible?
- Do objects remain consistent across frames?
- Does camera movement match the prompt?
- Is lighting and style consistent?
- Are there artefacts, distortions or abrupt changes?

## Record sheet
| Item | Observation |
|---|---|
| Prompt used | |
| Settings shown in interface | |
| Description of generated clip | |
| Strongest feature | |
| Limitation / artefact noticed | |
| Prompt improvement made | |

## Responsible use
Do not create deceptive videos of real people or events. Respect consent, privacy, copyright and applicable platform rules. Clearly identify synthetic media where context requires it.

## Conclusion
Sora was explored as a text-to-video generative AI tool. The generated clip was assessed for prompt alignment, motion quality, consistency and responsible use.


---

# Practical 09 AI Image Generator
## Exploration and Practice of AI Image Generator

## Aim
Implement and practice the use of an AI Image Generator as a tool within Artificial Intelligence.

## Problem statement
Assignment and practice of AI Image Generator.

## Objectives
- Understand AI-driven image generation.
- Explore how text prompts are converted into visual outputs.
- Study generative models such as GANs and diffusion models and neural style transfer.
- Evaluate quality, limitations, originality and ethical concerns.

## Theory
1. An AI image generator uses a trained model to create an image that matches a text prompt or supported visual input.
2. NLP models can encode prompts into numerical embeddings that represent semantic meaning and guide image generation.
3. A GAN contains a generator that creates samples and a discriminator that attempts to distinguish generated samples from real examples.
4. Diffusion models learn to reverse a gradual noising process. During generation, they start from noise and iteratively denoise it under prompt guidance.
5. Neural Style Transfer combines the content of one image with the style of another, balancing content loss and style loss.
6. The manual discusses applications in design, advertising, education, entertainment and prototyping, as well as risks such as bias, copyright disputes, low-quality details and deepfakes.

## Algorithm / Procedure
1. Open a permitted AI image-generation tool.
2. Write a prompt describing the subject, setting, composition, style, lighting, colours and image format.
3. Generate one or more images using available settings.
4. Evaluate the results for prompt relevance, coherence, artefacts, detail and visual quality.
5. Refine the prompt or use available editing/variation options.
6. Record the final prompt, settings, selected result and ethical considerations.

## Complexity / Practical nature
This is a hosted generative-media activity, not a local Python algorithm practical. Generation time and resource use depend on the model, resolution, number of variations and service.

## Expected output / record
Record at least two prompt trials, compare the generated images and state which result best matches the prompt and why.

## Practical activity worksheet
See [`practical_09_tool_activity.md`](practical_09_tool_activity.md) for a guided demonstration, prompt examples and record sheet.

## Oral / viva questions with answers
**Q1. What is an AI image generator?**
Answer: A generative AI tool that creates images from text prompts or supported visual inputs.

**Q2. What is Generative AI?**
Answer: AI that creates new content such as text, images, audio or video.

**Q3. What is a GAN?**
Answer: A Generative Adversarial Network made of a generator and a discriminator.

**Q4. What does the generator do in a GAN?**
Answer: It creates synthetic samples intended to resemble real training examples.

**Q5. What does the discriminator do?**
Answer: It classifies samples as real or generated.

**Q6. What is a diffusion model?**
Answer: A generative model trained to reverse a process that gradually adds noise to data.

**Q7. What is forward diffusion?**
Answer: The gradual addition of noise to the training data.

**Q8. What is reverse diffusion?**
Answer: The learned denoising process used to generate a sample from noise.

**Q9. What is Neural Style Transfer?**
Answer: A technique that combines the content of one image with the visual style of another.

**Q10. Name two ethical issues.**
Answer: Copyright/ownership concerns and the possibility of creating misleading synthetic images.

## Source alignment note
The supplied practical is a tool-exploration activity rather than a Python-programming assignment. The folder therefore contains a demonstration worksheet and oral preparation, not an unrelated fabricated Python script.


---

# Practical 9 - AI image generator exploration worksheet

## Aim
Explore and practice an AI image generator as a tool in Artificial Intelligence.

## Prompt structure
Describe the subject, action/pose, environment, composition, art style, lighting, colour palette and aspect ratio or image format if supported.

## Prompt experiment A - realistic
`A red apple hanging from a leafy green tree branch after light rain, close-up composition, soft natural morning light, realistic photography, crisp details, shallow depth of field.`

## Prompt experiment B - creative
`A tiny futuristic library inside a glass dome on the surface of Mars, warm glowing bookshelves, astronauts exploring, cinematic science-fiction concept art, detailed environment, dramatic rim lighting.`

## Procedure
1. Open a permitted AI image-generation tool such as one supported by your institution.
2. Enter Prompt A and generate an image.
3. Review the result for subject accuracy, composition, details and artefacts.
4. Change one prompt element (for example camera angle, lighting or art style) and generate Prompt A again.
5. Generate Prompt B and compare the realistic and imaginative outputs.
6. Save the prompt and any settings shown by the tool. Do not publish outputs without checking applicable usage rights.

## Concepts to explain
- **Text embeddings:** numerical representations of prompt meaning used to guide a model.
- **GAN:** generator creates synthetic samples; discriminator tries to distinguish real from generated samples.
- **Diffusion:** a model learns to reverse noise addition and generates an image by iterative denoising.
- **Neural Style Transfer:** combines the content of one image with the visual style of another.
- **Content loss / style loss:** measures used to preserve image content and match artistic style in Neural Style Transfer.

## Evaluation checklist
- Prompt relevance and completeness.
- Image coherence and object structure.
- Text/hand/finger artefacts if present.
- Lighting, colour and composition.
- Bias, misleading realism, ownership and copyright considerations.

## Record sheet
| Item | Observation |
|---|---|
| Tool used | |
| Prompt 1 and output | |
| Prompt 2 and output | |
| Which output matched better? Why? | |
| Artefacts or limitations | |
| Ethical considerations | |

## Responsible use
Avoid deceptive images, impersonation, privacy violations and misleading depictions of real events. Check the tool's terms and applicable copyright rules before reuse or publication.

## Conclusion
An AI image generator was explored using multiple prompts. The outputs were compared for quality, relevance, limitations and ethical concerns.
