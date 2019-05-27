# Write a Python function called satisfiesF that has the specification below.
# Then make the function call run_satisfiesF(L, satisfiesF).
# Paste your entire function satisfiesF, including the definition, in the box below.
# After you define your function, make a function call to run_satisfiesF(L, satisfiesF).
# Do not define f or run_satisfiesF. Do not leave any debugging print statements.

# For this question, you will not be able to see the test cases we run.
# This problem will test your ability to come up with your own test cases.


# Paste your function here
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    # Your function implementation here
    for s in range((len(L) - 1), -1, -1):
        if f(L[s]):
            continue
        else:
            L.remove(L[s])
    return len(L)

run_satisfiesF(L, satisfiesF)
