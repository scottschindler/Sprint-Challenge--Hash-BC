#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)

def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # insert first weight into hashtable
    hash_table_insert(ht, weights[0], 0)

    for i in range(1, len(weights)):
        if weights[i] > limit:
            continue

        # check if weight difference exists in hash table
        diff = abs(limit - weights[i])

        match = hash_table_retrieve(ht, diff)
        
        if match is not None:
            if match < i:
                return (i, match)
            else:
                return (match, i)

        hash_table_insert(ht, weights[i], i)
        
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")