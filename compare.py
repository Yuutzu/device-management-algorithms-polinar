# compare.py
import fcfs
import sstf
import fifo_paging
import dataset

def run_comparison():
    # FCFS
    order, avg_wait = fcfs.fcfs_scheduler(dataset.base_requests,
                                          dataset.arrival_times,
                                          dataset.service_times)
    print("=== FCFS Scheduling ===")
    for o in order:
        print(o)
    print(f"Average waiting time: {avg_wait:.2f}\n")

    # SSTF
    order, total_movement = sstf.sstf_scheduler(dataset.initial_head,
                                                dataset.base_requests)
    print("=== SSTF Disk Scheduling ===")
    for o in order:
        print(o)
    print(f"Total head movement: {total_movement}\n")

    # FIFO Paging
    steps, faults = fifo_paging.fifo_page_replacement(dataset.frames,
                                                      dataset.page_sequence)
    print("=== FIFO Page Replacement ===")
    for s in steps:
        print(s)
    print(f"Total page faults: {faults}\n")


# 👇 This makes sure the function runs when you execute: python compare.py
if __name__ == "__main__":
    run_comparison()
