# sstf.py

import dataset

def sstf_scheduler(initial_head, requests):
    head = initial_head
    pending = requests.copy()
    order = []
    total_movement = 0

    while pending:
        # Find request with minimum distance from head
        distances = [abs(r - head) for r in pending]
        idx = distances.index(min(distances))
        next_req = pending.pop(idx)
        movement = abs(next_req - head)
        total_movement += movement
        order.append({'request': next_req, 'movement': movement})
        head = next_req

    return order, total_movement


def print_sstf_example():
    order, total = sstf_scheduler(dataset.initial_head, dataset.base_requests)
    print('SSTF servicing order (request, movement):')
    for o in order:
        print(o)
    print(f'Total head movement: {total} cylinders')


if __name__ == '__main__':
    print_sstf_example()
