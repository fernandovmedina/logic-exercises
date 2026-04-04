intervals = [[1,3],[2,6],[8,10],[15,18]]

def merge_intervals(intervals):
  new_intervals = []
  for i in range(len(intervals) - 1):
    if intervals[i][1] >= intervals[i + 1][0]:
      new_intervals.append([intervals[i][0], max(intervals[i][1], intervals[i + 1][1])])
    else:
      new_intervals.append(intervals[i])
  new_intervals.append(intervals[len(intervals) - 1])
  return new_intervals

print(merge_intervals(intervals))