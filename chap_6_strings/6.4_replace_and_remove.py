# replace each 'a' by 'dd'
# delete all 'b'
def replace_and_remove(s):
    s = list(s)
    count_of_a = 0
    write_indx = 0
    for c in s:
        if c != 'b':
            s[write_indx] = (c)
            write_indx += 1
        if c == 'a':
            count_of_a += 1
    
    cur_indx = write_indx - 1
    write_indx += count_of_a - 1
    while cur_indx >= 0:
        if s[cur_indx] == 'a':
            s[write_indx] = 'd'
            s[write_indx - 1] = 'd'
            write_indx -= 2
        else:
            s[write_indx] = s[cur_indx]
            write_indx -= 1
        cur_indx -= 1
    return ''.join(s)

print(replace_and_remove('acdbbca'))