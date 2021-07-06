# return a new sorted merged list from K sorted lists, each with size N.

import heapq

def merge(lists):
    merged_list = []

    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    print("heap",heap)
    print()
    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)
        merged_list.append(val)
        print("merged_list",merged_list)
        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],list_ind,element_ind + 1)
            print("next_tuple",next_tuple)
            heapq.heappush(heap, next_tuple)
            print("heap",heap)
        print()
    return merged_list

if __name__ == '__main__':
    lists = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    print(lists)
    print(merge(lists))
