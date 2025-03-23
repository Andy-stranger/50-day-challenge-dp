from collections import defaultdict

def leastInterval(self, tasks, n: int) -> int:
    m = len(tasks)
    mapp = defaultdict(int)
    max_freq = 0
    for i in tasks:
        mapp[i] += 1
        if mapp[i] > max_freq:
            max_freq = mapp[i]
    tasks_with_max_freq = 0
    for v in mapp.values():
        if v == max_freq:
            tasks_with_max_freq += 1

    idle_parts = max_freq - 1
    units_per_idle_part = n - (tasks_with_max_freq-1)
    total_units_in_all_parts = idle_parts * units_per_idle_part
    remaining_tasks = m - (max_freq * tasks_with_max_freq)
    idles = max(0 , total_units_in_all_parts - remaining_tasks)

    return m + idles

#refer - https://medium.com/@satyem77/task-scheduler-leetcode-39d579f3440