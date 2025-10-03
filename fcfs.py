# fcfs.py
"""
First-Come-First-Served (FCFS) device scheduling simulation.
Input: requests, arrival times, service times.
Output: servicing order and average waiting time.
"""

import dataset

def fcfs_scheduler(requests, arrivals, services):
    # Combine into records
    recs = [
        {'id': i + 1, 'request': r, 'arrival': a, 'service': s}
        for i, (r, a, s) in enumerate(zip(requests, arrivals, services))
    ]
    # Sort by arrival time
    recs.sort(key=lambda x: x['arrival'])

    current_time = 0
    order = []
    waiting_times = []

    for r in recs:
        start = max(current_time, r['arrival'])
        wait = start - r['arrival']
        finish = start + r['service']
        order.append({
            'id': r['id'], 'request': r['request'],
            'arrival': r['arrival'], 'start': start,
            'wait': wait, 'finish': finish
        })
        waiting_times.append(wait)
        current_time = finish

    avg_wait = sum(waiting_times) / len(waiting_times) if waiting_times else 0.0
    return order, avg_wait


def print_fcfs_example():
    order, avg = fcfs_scheduler(dataset.base_requests, dataset.arrival_times, dataset.service_times)
    print('FCFS servicing order (id, request, arrival, start, wait, finish):')
    for o in order:
        print(o)
    print(f'Average waiting time: {avg:.3f} time units')


if __name__ == '__main__':
    print_fcfs_example()
