def check_first_n_numbers_collatz(n):
    def check_collatz(num):
        if num % 2 == 0: # even case
            return num/2
        else:
            return num*3 + 1

    checked = {1}
    for num in range(1, n + 1):
        temp = num
        while temp not in checked:
            temp = check_collatz(temp)
        checked.add(num)
        if num % 1000 == 0:
            print(f"Number {num} is verified")


check_first_n_numbers_collatz(1000000)