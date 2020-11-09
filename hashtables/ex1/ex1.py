
def get_indices_of_item_weights(weights, length, limit):
 
    HashTable = {}

    for i in range(length):
        target = limit - weights[i]

        if target in HashTable.values():
            x = i
            y = [k for k,v in HashTable.items() if v == target][0]
            return (x, y) if x > y else (y, x)

        HashTable[i] = weights[i]
    
    return None
