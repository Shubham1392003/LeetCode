class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,arriveBob: str, leaveBob: str) -> int:

        al_a = self.dayss(arriveAlice)
        al_l = self.dayss(leaveAlice)
        bob_a = self.dayss(arriveBob)
        bob_l = self.dayss(leaveBob)

        start = max(al_a, bob_a)
        end = min(al_l, bob_l)

        if start > end:
            return 0

        return end - start + 1

    def dayss(self, date: str) -> int:
        parts = date.split("-")
        month = int(parts[0])
        day = int(parts[1])

        days = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]

        ans = 0
        for i in range(month - 1):
            ans += days[i]

        return ans + day