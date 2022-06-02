
from typing import List

class Solution:
    def printAndCount(self, vals: List[str]) -> int:
        for val in vals:
            print(f"input val : {val}")
        return  len(vals)

def main():
    solution = Solution()
    vals =  [1, 2, 3]
    count = solution.printAndCount(vals)
    print(f"Total Count is : {count} ")


if __name__ == "__main__":
    main()