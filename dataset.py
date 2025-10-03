# dataset.py

# Example dataset for FCFS & SSTF
base_requests = [95, 180, 34, 119, 11, 123, 62, 64]
arrival_times = [0, 2, 4, 6, 8, 10, 12, 14]
service_times = [3, 4, 2, 6, 5, 3, 4, 2]

# Initial head position for SSTF
initial_head = 53

# Paging simulation parameters
frames = 3

# Derive a page sequence from the base requests by taking modulo 10
# and add some extra pages to simulate re-use
page_sequence = [r % 10 for r in (base_requests + [67, 14, 124, 65, 37, 98])]

# Helper to pretty-print dataset when run directly
if __name__ == '__main__':
    print('=== Dataset ===')
    print('Base requests:', base_requests)
    print('Arrival times:', arrival_times)
    print('Service times:', service_times)
    print('Initial head:', initial_head)
    print('Frames:', frames)
    print('Page sequence:', page_sequence)
