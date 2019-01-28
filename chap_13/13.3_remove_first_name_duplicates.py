def remove_repeated_first_names(names):
    # sort names
    names.sort(key=lambda x: x[0])
    x = 0
    # while x < len(names):
    #     if names[x][0] == names[x-1][0]:
    #         del names[x]
    #     else: 
    #         x += 1 
    write_indx = 1
    for cand in names[1:]:
        if cand[0] != names[write_indx-1][0]:
            names[write_indx] = cand
            write_indx += 1
    del names[write_indx:]


names = [('Ian', 'Curties'), 
         ('Bill', 'Big'),
         ('Bill', 'Small'),
         ('Ian', 'Yours'), 
         ('Ian', 'Small')] 
remove_repeated_first_names(names)
print(names)