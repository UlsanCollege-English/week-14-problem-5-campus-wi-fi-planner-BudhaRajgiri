from __future__ import annotations
from typing import Optional, Tuple, List


class TreeNode:
    """Simple binary tree node."""
    def __init__(self, value: int,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.value})"


def max_level_sum(root: Optional[TreeNode]) -> Tuple[Optional[int], int]:
    """
    Return a tuple (level_index, sum) where level_index is the index of the level
    with the maximum sum of node values. If multiple levels tie, return the smallest index.
    If the tree is empty, return (None, 0).
    """
    if root is None:
        return (None, 0)

    level = 0
    max_sum = float("-inf")
    best_level = None

    queue: List[TreeNode] = [root]

    while queue:
        level_sum = sum(node.value for node in queue)
        if level_sum > max_sum:
            max_sum = level_sum
            best_level = level
        elif level_sum == max_sum and best_level is None:
            # tie-breaking: choose smallest index
            best_level = level

        # prepare next level
        next_queue: List[TreeNode] = []
        for node in queue:
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
        level += 1

    return (best_level, max_sum)