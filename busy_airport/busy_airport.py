import sys
import numpy as np
from queue import PriorityQueue
sys.stdin = open('./busy_airport/input.txt', 'r')
sys.stdout = open('./busy_airport/output.txt', 'w')


def get_completion_time(arrival_time, pq, job_duration, number_of_workers):
    size = pq.qsize()
    if size >= number_of_workers:
        min_available_time = pq.get()
    else:
        min_available_time = 0

    if min_available_time <= arrival_time:
        pq.put(arrival_time + job_duration)
        return arrival_time + job_duration
    pq.put(min_available_time + job_duration)
    return min_available_time + job_duration


a, b, c, d = list(map(int, input().strip('').split(' ')))
n = int(input())
arr = np.array(list(map(int, input().strip('').split(' '))))
passport_queue = PriorityQueue()
baggage_queue = PriorityQueue()
passport_time = []
baggage_time = []
for x in arr:
    passport_time.append(get_completion_time(x, passport_queue, a, b))
    baggage_time.append(get_completion_time(
        passport_time[-1], baggage_queue, c, d))

print(np.max(baggage_time))
