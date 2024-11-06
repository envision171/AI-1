def alpha_beta(node, depth, alpha, beta, maximizing_player):
    if depth == 0 or is_terminal(node):
        return evaluate(node)

    if maximizing_player:
        max_eval = float('-inf')
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for child in get_children(node):
            eval = alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def is_terminal(node):

    return len(get_children(node)) == 0

def evaluate(node):

    return node.value
def get_children(node):

    return node.children


class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []


root = Node(0, [
    Node(0, [
        Node(3), Node(5)
    ]),
    Node(0, [
        Node(6), Node(9)
    ])
])

best_value = alpha_beta(root, depth=3, alpha=float('-inf'), beta=float('inf'), maximizing_player=True)
print("Best value:", best_value)