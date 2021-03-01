#!/bin/python3

import os
import sys


#
# Complete the contacts function below.
#
def contacts(queries):
    potential_matches_count = []
    suggestion_dict = {}

    while queries:
        command = queries.pop(0)
        if command[0] == 'add':
            contact_name = command[1]
            for i in range(1, len(contact_name)+1):
                if contact_name[:i] not in suggestion_dict:
                    suggestion_dict[contact_name[:i]] = [contact_name]
                else:
                    suggestion_dict[contact_name[:i]].append(contact_name)
        if command[0] == 'find':
            search_query = command[1]
            print('full dict')
            print(suggestion_dict)
            if search_query in suggestion_dict.keys():
                potential_matches_count.append(len(suggestion_dict[search_query]))
            else:
                potential_matches_count.append(0)
    print(potential_matches_count)
    return potential_matches_count


if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

#    fptr.write('\n'.join(map(str, result)))
#    fptr.write('\n')

#    fptr.close()
