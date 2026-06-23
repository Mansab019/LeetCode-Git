def finalValueAfterOperations(operations):
    # your code here
    x = 0
    for op in operations:
        if op in ("++X", "X++"):
            x += 1
        else:
            x -= 1
    return x
    
operations = ["--X", "X++", "X++"]
print(finalValueAfterOperations(operations))  # Expected: 1