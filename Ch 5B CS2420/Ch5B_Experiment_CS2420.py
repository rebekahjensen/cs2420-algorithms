import time
import random
import Algo_and_Struts_05_f_sorting
import Algo_and_Struts_05_g_quick_sort

items_test = [1000, 10000, 100000, 10000000]

#sorting
def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])

def bubble_sort_short(a_list):
    for i in range(len(a_list)):
        exchanges = False
        for j in range(len(a_list)-i-1):
            if a_list[j] > a_list[j + 1]:
                exchanges = True
                (a_list[j], a_list[j + 1]) = (a_list[j + 1], a_list[j])
        if not exchanges:
            break

def selection_sort(a_list):
    for i, item in enumerate(a_list):
        min_idx = len(a_list) - 1
        for j in range(i, len(a_list)):
            if a_list[j] < a_list[min_idx]:
                min_idx = j
        if min_idx != i:
            a_list[min_idx], a_list[i] = a_list[i], a_list[min_idx]


def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        cur_val = a_list[i]
        cur_pos = i

        while cur_pos > 0 and a_list[cur_pos - 1] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - 1]
            cur_pos = cur_pos - 1
        a_list[cur_pos] = cur_val

def shell_sort(a_list):
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            gap_insertion_sort(a_list, pos_start, sublist_count)
        #print("After increments of size", sublist_count, "the list is", a_list)
        sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        cur_val = a_list[i]
        cur_pos = i
        while cur_pos >= gap and a_list[cur_pos - gap] > cur_val:
            a_list[cur_pos] = a_list[cur_pos - gap]
            cur_pos = cur_pos - gap
        a_list[cur_pos] = cur_val

def merge_sort(a_list):
    #print("Splitting", a_list)
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i = i + 1
            else:
                a_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j = j + 1
            k = k + 1
   # print("Merging", a_list)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# bubble_sort(a_list)
# bubble_sort_short(a_list)
# selection_sort(a_list)
# insertion_sort(a_list)
# shell_sort(a_list)
# merge_sort(a_list)
print(a_list)

#quick sort
def quick_sort(a_list):
    quick_sort_helper(a_list, 0, len(a_list) - 1)


def quick_sort_helper(a_list, first, last):
    if first < last:
        split = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split - 1)
        quick_sort_helper(a_list, split + 1, last)


def partition(a_list, first, last):
    pivot_val = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_val:
            left_mark = left_mark + 1
        while left_mark <= right_mark and a_list[right_mark] >= pivot_val:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            a_list[left_mark], a_list[right_mark] = (
                a_list[right_mark],
                a_list[left_mark],
            )
    a_list[first], a_list[right_mark] = a_list[right_mark], a_list[first]

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(a_list)
print(a_list)

items_test = [1000, 10000, 100000, 10000000]
sorting_alg = {"Bubble_Sort": bubble_sort,
                  "Selection_Sort": selection_sort,
                  "Insertion_Sort": insertion_sort,
                  "Shell_Sort": shell_sort,
                  "Merge_Sort": merge_sort,
                  "Quick_Sort": quick_sort}

#let's try one at a time
#uncomment/comment as neccessary
# selected_method = "Bubble_Sort"
# selected_method = "Selection_Sort"
# selected_method = "Insertion_Sort"
# selected_method = "Shell_Sort"
# selected_method = "Merge_Sort"
selected_method = "Quick_Sort"

results = {selected_method: {"Times": []}}

for size in items_test:
    print(f"\nTesting {selected_method} with list size: {size}")
    random_list = [random.randint(0, 10000000) for _ in range(size)]

    sort_function = sorting_alg[selected_method]

    #time the sorting method
    start_time = time.time()
    sort_function(random_list)
    end_time = time.time()

    #find elapsed time
    elapsed_time = end_time - start_time
    results[selected_method]["Times"].append(elapsed_time)

    print(f"{selected_method} took {elapsed_time:.6f} seconds for list size {size}.")

print("\Results:")
for method, data in results.items():
    print(f"{method}: {data['Times']}")