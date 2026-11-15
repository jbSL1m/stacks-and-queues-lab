def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.

    Approach (stack / LIFO):
      - Every opening bracket is pushed onto the stack.
      - Every closing bracket must match the most recently opened bracket,
        which is exactly the item on top of the stack. If the stack is empty
        or the top doesn't match, the string is unbalanced.
      - Once every character has been read, any brackets still on the stack
        were never closed, so the string is only valid if the stack is empty.

    Characters that aren't brackets (letters, digits, spaces, ...) are ignored,
    so "f(a[0])" validates the same as "([])".

    Runs in O(n) time and O(n) space for a string of length n.
    """
    # Map each closing bracket to the opening bracket it must close.
    pairs = {")": "(", "]": "[", "}": "{"}
    openers = set(pairs.values())

    stack = []
    for char in s:
        if char in openers:
            stack.append(char)
        elif char in pairs:
            # A closer with nothing open, or one that closes the wrong
            # bracket type (e.g. "([)]"), means the string is unbalanced.
            if not stack or stack.pop() != pairs[char]:
                return False

    # Leftover openers were never closed, e.g. "(()".
    return not stack


if __name__ == "__main__":
    examples = ["()", "{[()]}", "([]{})", "(", "([)]", "(()", ")(", "f(a[0])"]
    for example in examples:
        verdict = "balanced" if is_valid_parentheses(example) else "NOT balanced"
        print(f"{example!r:>10} -> {verdict}")
