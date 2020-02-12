#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(length)
    ans = None
    for i,w in enumerate(weights):
        if hash_table_retrieve(ht, w) is not None:
            ans = [i, hash_table_retrieve(ht, w)]
            if ans[1] > ans[0]:
                ans[0], ans[1] = ans[1], ans[0]
            break
        else:
            hash_table_insert(ht, limit-w, i)
    return ans


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
