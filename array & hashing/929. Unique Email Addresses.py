# Problem: 929. Unique Email Addresses
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/unique-email-addresses/




from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')# Split the email into local and domain parts using '@' as the delimiter    
            local = local.split('+')[0]            # Process the local part by removing everything after '+' character (if it exists)   
            local = local.replace('.', '')# Remove all '.' characters from the local part of the email address 
            unique_emails.add(local + '@' + domain)# Add  the processed email to the set of unique emails 
        return len(unique_emails) # Return the number of unique email addresses in the set 