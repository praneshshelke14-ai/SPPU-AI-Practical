# AI Practicals 1-9: Oral / Viva Questions and Answers

Questions are grouped by practical. Answers are short, examination-style responses. Refer to each practical README and the complete notes for the source code and procedure.

## Practical 01 Expert System

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

## Practical 02 BFS DFS Maze

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

## Practical 03 A Star Search

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

## Practical 04 Constraint Satisfaction

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

## Practical 05 Minimax

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

## Practical 06 Minimax Alpha Beta

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

## Practical 07 ChatGPT

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

## Practical 08 Sora

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

## Practical 09 AI Image Generator

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
