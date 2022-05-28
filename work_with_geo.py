import json
import time

from geopy import distance
from functools import reduce

# Opening JSON file
t_all = time.perf_counter()
with open('russia.geo.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)

    t_st_sum_all = time.perf_counter()

    def method_sum_all(flatten):
        return tuple(reduce(lambda x, y: x + y, flatten(json_object
                                                        ['features']
                                                        [0]
                                                        ['geometry']
                                                        ['coordinates'])))


    all_time1 = time.perf_counter() - t_st_sum_all
    print("Время выполнения method_sum_all(flatten): " + str(all_time1) +
          "сек")

    t_m_pair_dots = time.perf_counter()

    def m_pair_dots():
        def flatten(t):
            sublist_ = (item for sublist in
                        (item for sublist in tuple(t) for item in sublist)
                        for item in sublist)
            return sublist_

        ll = []
        return m_ll(ll, method_sum_all(flatten))


    all_time2 = time.perf_counter() - t_m_pair_dots
    print("Время выполнения m_pair_dots: " + str(all_time2) + "сек")

    t_m_ll = time.perf_counter()

    def m_ll(ll, sum_all):
        for i in range(0, len(sum_all), 2):
            ll.append((sum_all[i + 1], sum_all[i]))
        return ll


    all_time3 = time.perf_counter() - t_m_ll
    print("Время выполнения m_ll: " + str(all_time3) + "сек")

    t_m_ll2 = time.perf_counter()

    def m_ll2():
        ll2 = []
        dots = m_pair_dots()
        for i in range(0, len(dots), 2):
            ll2.append((dots[i], dots[i + 1]))
        return ll2


    all_time4 = time.perf_counter() - t_m_ll2
    print("Время выполнения t_m_ll2: " + str(all_time4) + "сек")

kms = []

t_kms = time.perf_counter()
for i in m_ll2():
    dist = distance.distance(i[0], i[1]).km
    kms.append(dist)
all_time5 = time.perf_counter() - t_kms
print("Время выполнения t_kms: " + str(all_time5) + "сек")

print("Протяжённость: " + str(sum(kms)) + " км")

all_time6 = time.perf_counter() - t_all
print("Время выполнения t_all: " + str(all_time6) + "сек")
