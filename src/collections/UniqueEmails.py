
from typing import List

"""
Leet Code URL : https://leetcode.com/problems/unique-email-addresses/
"""

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:


        #Set to hold Unique Email Address

        uniqueEmails=set()

        for email in emails:

            #split email address pre and post @

            name,domain = email.split("@")

            #Get pre + and replace period with space
            name = name.split("+")[0].replace(".","")

            uniqueEmails.add(name+"@"+domain)


        # Print Results
        print(f"Unique Emails : {uniqueEmails}")

        return len(uniqueEmails)

def main():
    solution = Solution()
    emails =  ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    output = solution.numUniqueEmails(emails)
    expectedOutput=2

    print(f"Total Count is : {output} ")
    assert expectedOutput==output

    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    output = solution.numUniqueEmails(emails)
    expectedOutput=3

    print(f"Total Count is : {output} ")
    assert expectedOutput==output


if __name__ == "__main__":
    main()