# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
concatenated_string1 = ' '.join(['Thirty', 'Days', 'Of', 'Python'])
print(concatenated_string1)  # Output: Thirty Days Of Python

# 2. Concatenate the string 'Coding', 'For', 'All' to a single string, 'Coding For All'.
concatenated_string2 = ' '.join(['Coding', 'For', 'All'])
print(concatenated_string2)  # Output: Coding For All

# 3. Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

# 4. Print the variable company using print().
print(company)  # Output: Coding For All

# 5. Print the length of the company string using len() method and print().
print(len(company))  # Output: Length of the string

# 6. Change all the characters to uppercase letters using upper() method.
print(company.upper())  # Output: CODING FOR ALL

# 7. Change all the characters to lowercase letters using lower() method.
print(company.lower())  # Output: coding for all

# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())  # Output: Coding for all
print(company.title())       # Output: Coding For All
print(company.swapcase())    # Output: cODING fOR aLL

# 9. Cut(slice) out the first word of Coding For All string.
print(company[7:])  # Output: For All

# 10. Check if Coding For All string contains a word Coding using index or find methods.
print(company.find('Coding'))  # Output: 0 (position of "Coding")
print('Coding' in company)    # Output: True

# 11. Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))  # Output: Python For All

# 12. Change 'Python for Everyone' to 'Python for All' using replace.
new_string = 'Python for Everyone'
print(new_string.replace('Everyone', 'All'))  # Output: Python for All

# 13. Split the string 'Coding For All' using space as the separator (split()).
print(company.split())  # Output: ['Coding', 'For', 'All']

# 14. Split the string "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', '))  # Output: List of companies

# 15. What is the character at index 0 in the string 'Coding For All'.
print(company[0])  # Output: C

# 16. What is the last index of the string 'Coding For All'.
print(len(company) - 1)  # Output: Last index (13)

# 17. What character is at index 10 in 'Coding For All' string.
print(company[10])  # Output: 'A'

# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase1 = 'Python For Everyone'
acronym1 = ''.join(word[0] for word in phrase1.split())
print(acronym1)  # Output: PFE

# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
phrase2 = 'Coding For All'
acronym2 = ''.join(word[0] for word in phrase2.split())
print(acronym2)  # Output: CFA

# 20. Use index to determine the position of the first occurrence of C in 'Coding For All'.
print(company.index('C'))  # Output: 0
