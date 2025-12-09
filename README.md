[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/VjQjuzxF)
# HW05 — Campus Wi-Fi Planner (Max Level Load in a Tree)

## Story

A university is planning its campus Wi-Fi network. Each access point (router) is represented as a node in a **binary tree**:

- The root is the main building.
- Children are routers deeper in the network.

Each node stores an integer **capacity** value (how many students it can support).

The IT team wants to know:

> "At which depth of the tree (level) is our **total Wi-Fi capacity** the highest?"

You must compute which **level index** has the maximum total capacity, and what that total capacity is.

---

## Technical Description

In `main.py`, implement:

```python
class TreeNode
max_level_sum(root) -> tuple
```

### TreeNode Structure

Constructor (same pattern as HW04, but used for a different task):

```python
TreeNode(value, left=None, right=None)
```

- `value`: integer capacity at that router
- `left`, `right`: child routers or `None`

### Behavior

- The **root** is at level `0`.
- Its children are at level `1`, their children at level `2`, and so on.
- For each level, compute the **sum of `value`** for all nodes at that level.
- Find the level with the **maximum sum**.

### Output

- Return a tuple: `(best_level_index, best_sum)`
  - `best_level_index`: an integer level index (0-based)
  - `best_sum`: the capacity sum at that level (int)
- If the tree is empty (`root is None`), return `(None, 0)`

### Constraints

- Use **BFS (level-order traversal)** or another correct method
- Time complexity: **O(N)** where N is the number of nodes
- Extra space: **O(W)** where W is the maximum width of the tree (e.g., BFS queue)

---

## 8 Steps of Coding (minimal prompts)

You own the full process now:

- Clarify the problem and restate it
- Identify inputs/outputs and any helper data structures (queue, counters)
- Plan your approach (probably BFS using a queue)
- Write pseudocode, then implement
- Test and debug on small trees (1–3 levels) and an empty tree
- Verify you only traverse the tree once

---

## Hints

1. `collections.deque` is useful for BFS queues (`append`, `popleft`)
2. Process the tree **level by level**: before each level, note the number of nodes in that level
3. Track both the current level index and the best sum seen so far

---

## How to Run Tests Locally

From the project root:

```bash
python -m pytest -q
```

Pytest will discover `hw05/tests/test_hw05.py`.

---
## FAQ

**Q1: How do I know which nodes are on the same level?**

One pattern:

- Use a queue
- At each step, record `level_size = len(queue)` and process exactly that many nodes as the current level

**Q2: What if multiple levels have the same max sum?**

Return the smallest level index (i.e., the earliest, shallowest level).

**Q3: What if `root` is `None`?**

Return `(None, 0)`.

**Q4: Do I have to reuse HW04's TreeNode?**

No, this is a new file. But use the same constructor style: `TreeNode(value, left=None, right=None)`.

**Q5: Why BFS and not DFS?**

BFS naturally groups nodes by level. DFS can also work, but you must manually track depths.

**Q6: What Big-O is expected?**

Time O(N), space O(W) where W is the maximum number of nodes on any level.

**Q7: Can I use any non-standard libraries?**

No. Only the Python standard library is allowed.
