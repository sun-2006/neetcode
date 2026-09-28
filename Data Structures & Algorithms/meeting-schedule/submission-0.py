class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # Sort intervals by their start time
        intervals.sort(key=lambda x: x.start)
        
        # Check if the start of the current meeting overlaps with the end of the previous one
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
                
        return True