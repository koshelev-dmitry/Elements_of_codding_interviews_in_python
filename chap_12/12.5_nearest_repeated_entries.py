def find_nearest(words):
    word_stat = {}
    neares_repetition = float('inf')
    for i, word in enumerate(words):
        if word in word_stat:
            latest_index = word_stat[word]
            neares_repetition = min(i - latest_index, 
                                    neares_repetition)
            word_stat[word] = i
        else:
            word_stat[word] = i
    return neares_repetition if neares_repetition!= float('inf') else -1
    
    # for element in word_stat:
    #     if len(word_stat[element]) == 1:
    #         word_stat.pop(element)
    #     else:
    #         indx_list = word_stat[element]
    #         # find shortest length
    #         shortest
            

words = ['All', 
        'work', 
        'and', 
        'no', 
        'play',
        'makes',
        'for',
        'no',
        'work',
        'no',
        'no',
        'fun',
        'and',
        'no',
        'result']

print(find_nearest(words))