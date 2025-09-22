# You’re given a list of meeting intervals, where each interval is defined by a start 
# time and an end time (intervals[i] = [startᵢ, endᵢ]). 
# Determine whether it’s possible for one person to attend every meeting without any 
# overlaps.
# Time complexity O(n^2)
intervals1 = [[0,30], [10,20], [15,40]];
intervals2 = [[0,10], [15,20], [25,40]];
def canAttendMeetings(intervals):
    def overlap(interval1, interval2):
        return (interval1[0] >= interval2[0] and interval1[0] < interval2[1] or 
                interval2[0] >= interval1[0] and interval2[0] < interval1[1])
    n = len(intervals);
    for i in range(n):
        for j in range(i+1, n):
            if overlap(intervals[i], intervals[j]):
                return False;
    return True;

print(canAttendMeetings(intervals1));
print(canAttendMeetings(intervals2));

# Time complexity O(n log n)
def can_attend_meetings(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True;

print(can_attend_meetings(intervals1));
print(can_attend_meetings(intervals2));