def find_subset_with_sum(A, m):
    def helper_DFS(i, sum_left, curr_sequence=[]):
        # print(f"i={i}, sum_left={sum_left}, curr_seq={curr_sequence}")

        current_sum = sum(curr_sequence) 
        # print(current_sum)

        if current_sum == m: # we have result
            result.append(curr_sequence)
            return 

        if i == len(A): # last element
            return

        if current_sum + sum_left < m: # we are not able to get to the result
            return

        
        helper_DFS(i+1, sum_left - A[i], curr_sequence + [A[i]])
        helper_DFS(i+1, sum_left - A[i], curr_sequence)
    
    result = []
    sum_left = sum(A)
    helper_DFS(0, sum_left)
    return result


A = [5, 10, 15, 2, 28, 19, 11, 10, 10]
m = 30
for res in find_subset_with_sum(A, m):
    print(res)