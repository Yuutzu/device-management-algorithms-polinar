# fifo_paging.py
import dataset

def fifo_page_replacement(frames_count, page_sequence):
    frames = []
    queue = []
    page_faults = 0
    steps = []

    for step_idx, page in enumerate(page_sequence, start=1):
        if page in frames:
            status = 'Hit'
        else:
            status = 'Fault'
            page_faults += 1
            if len(frames) < frames_count:
                frames.append(page)
                queue.append(page)
            else:
                victim = queue.pop(0)
                victim_idx = frames.index(victim)
                frames[victim_idx] = page
                queue.append(page)

        steps.append({'step': step_idx, 'page': page, 'frames': frames.copy(), 'status': status})

    return steps, page_faults

def print_fifo_example():
    steps, faults = fifo_page_replacement(dataset.frames, dataset.page_sequence)
    print('FIFO paging steps:')
    for s in steps:
        print(s)
    print(f'Total page faults: {faults}')

if __name__ == '__main__':
    print_fifo_example()
