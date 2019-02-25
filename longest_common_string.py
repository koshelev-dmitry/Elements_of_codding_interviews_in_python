"""
function bla bla
"""
def longest_common_string(string_1, string_2):
    """bla bla"""
    def helper_lcs(i, j):
        """bla bla"""
        if (i, j) in memo:
            return memo[(i, j)]
        if i >= len(string_1) or j >= len(string_2):
            memo[(i, j)] = ''
        elif string_1[i] == string_2[j]:
            memo[(i, j)] = string_1[i] + helper_lcs(i+1, j+1)
        else:
            memo[(i, j)] = max(helper_lcs(i, j+1), helper_lcs(i+1, j), key=len)
        return memo[(i, j)]
    memo = {}
    return helper_lcs(0, 0)

STR_1 = 'abd'
STR_2 = 'aabeced'
print(longest_common_string(STR_1, STR_2))
