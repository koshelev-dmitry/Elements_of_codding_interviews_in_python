def smallest_substr_covering_values(words, keywords):
    positions = {}
    for i, word in enumerate(words):
        if word in positions:
            positions[word] += [i]
        else: 
            positions[word] = i
    
    start = 0
    stop = len(words)
    for key in keywords:
        if key in positions:
            start = min(start, min(positions[key]))
            stop = max(start, max(positions[key]))
        else: 
            return None 

    return (start, stop)

    

words = ['All', 'work', 
        'and', 'no', 
        'play','makes',
        'for', 'no',
        'work', 'no',
        'no', 'fun',
        'and', 'no',
        'result']
keywords = ['no', 'fun']