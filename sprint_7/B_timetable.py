from __future__ import annotations

from line_profiler_pycharm import profile

@profile
def main():
    cnt = int(input())
    lessons = []
    for _ in range(cnt):
        item = [float(x) for x in input().split()]
        lessons.append((item[1], item))

    lessons_sorted_by_endtime = sorted(lessons)

    res = []
    cur_start = -1
    for k in lessons_sorted_by_endtime:
        if cur_start <= k[1][0]:
            cur_start = k[0]
            res.append(k[1])

    print(len(res))
    for item in res:
        print(f'{item[0]:g} {item[1]:g}')


if __name__ == "__main__":
    main()
