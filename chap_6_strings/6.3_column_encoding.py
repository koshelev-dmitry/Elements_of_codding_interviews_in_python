def compute_column_encoding(column_code):
    result = 0
    for c in reversed(column_code):
        num = ord(c) - ord('A') + 1
        result = result*26 + num
    print(result)

compute_column_encoding('Z')
