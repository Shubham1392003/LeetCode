class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        arriveAliceD = self.days(arriveAlice)
        leaveAliceD = self.days(leaveAlice)
        arriveBobD = self.days(arriveBob)
        leaveBobD = self.days(leaveBob)

        start = max(arriveAliceD,arriveBobD)
        end = min(leaveAliceD,leaveBobD)

        if start > end :
            return 0
        
        return end-start + 1

    def days(self, date):
        parts = date.split('-')
        month = int(parts[0])
        day = int(parts[1])
        ans=0

        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        for i in range(month-1):
            ans+=months[i]

        return ans+day
        