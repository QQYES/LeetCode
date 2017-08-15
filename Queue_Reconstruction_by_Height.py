class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if isinstance(people, list):
            stop = 0
            while not stop:
                for i, person in enumerate(people):
                    inner_stop = 0
                    if isinstance(person, list):
                        for j, person_com in enumerate(people):
                            count = 0
                            if count == person[1]:
                                break
                            if person_com[0] >= person[0]:
                                people[j], people[i] = people[i], people[j]
                                count += 1
                                inner_stop = 1
                    if i == len(people) - 1 and inner_stop == 0:
                        stop = 1
                    break

            return people


solution = Solution()
print(solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
