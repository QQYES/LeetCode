class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if isinstance(people, list):
            flag = 1
            while flag:

                for i, person in enumerate(people):
                    if isinstance(person, list):
                        for j, person_com in enumerate(people):
                            count = 0
                            if count == person[1]:
                                flag = 1
                                break
                            if person_com[0] >= person[0]:
                                people[j], people[i] = people[i], people[j]
                                count += 1
                                flag = 0
                        break

            return people


solution = Solution()
print(solution.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
