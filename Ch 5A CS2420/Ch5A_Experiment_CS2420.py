import time
import random
import statistics
import Algo_and_Struts_05_a_sequential_search
import Algo_and_Struts_05_c_binary_search

#these are the objects, not the times
items_test = [1000, 10000, 100000, 10000000]

def sequential_search(a_list, item):
    pos = 0

    #spot 0-0, etc.
    #sorted spot
    #fill dictionary with something
    #ie spot zero has zero

    while pos < len(a_list):
        if a_list[pos] == item:
            return True
        pos = pos + 1

    return False

#binary search
def binary_search(a_list, item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
            return True
        elif item < a_list[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False

items_test = [1000, 10000, 100000, 10000000]
search_methods = {"Sequential_search": sequential_search, 
                  "Binary_search": binary_search}

results = {method: {"Average": [], "Median": []} for method in search_methods}
results["Dictionary Search"] = {"Average": [], "Median": []}


for size in items_test:
    sorted_list = list(range(size))
    data_dict = {key: True for key in sorted_list}

    search_items = random.sample(sorted_list, 100)

#run experiment
    for method_name, search_method in search_methods.items():
        times = []
        for item in search_items:
            start_time = time.time()
            search_method(sorted_list, item)
            end_time = time.time()
            times.append(end_time - start_time)

        results[method_name]["Average"].append(statistics.mean(times))
        results[method_name]["Median"].append(statistics.median(times))

    #dictionary search
    dict_times = []
    for item in search_items:
        start_time = time.time()
        _= data_dict.get(item)
        end_time = time.time()
        dict_times.append(end_time - start_time)

    results["Dictionary Search"]["Average"].append(statistics.mean(dict_times))
    results["Dictionary Search"]["Median"].append(statistics.median(dict_times))

    print(results)