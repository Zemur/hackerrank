from bisect import insort

if __name__ == '__main__':
    n = int(input().strip())
    running_list = []

    for i in range(n):
        item_to_insert = int(input().strip())
        insort(running_list, item_to_insert)
        pos = len(running_list) // 2
        result = float(running_list[pos])
        if len(running_list) % 2 == 0:
            result += running_list[pos - 1]
            result /= 2
        print(result)
