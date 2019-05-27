# Write a function called longestRun, which takes as a parameter a list of integers
# named L (assume L is not empty).
# This function returns the length of the longest run of monotonically increasing numbers occurring in L.
# A run of monotonically increasing numbers means that a number at position k+1
# in the sequence is either greater than or equal to the number at position k in the sequence.

# For example, if L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2] then your function should return the value 5
# because the longest run of monotonically increasing integers in L is [3, 4, 5, 7, 7].

# Do not leave any debugging print statements when you paste your code in the box.


def longestRun(L):
    answer = 1
    tmp_ans = 1
    for i in range(1, len(L)):
        if L[i] >= L[i-1]:
            tmp_ans += 1
        else:
            if answer < tmp_ans:
                answer, tmp_ans = tmp_ans, 1
            else:
                tmp_ans = 1
    return answer if answer > tmp_ans else tmp_ans

print(longestRun([10, 1]))
