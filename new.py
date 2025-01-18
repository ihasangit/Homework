# Concatenate the strings 'Thirty', 'Days', 'Of', 'Python' to a single string
string1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print(string1)

# Concatenate the strings 'Coding', 'For', 'All' to a single string
string2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print(string2)

# Declare a variable named company and assign it to an initial value
company = "Coding For All"

# Print the variable company
print(company)

# Print the length of the company string
print(len(company))

# Change all characters to uppercase letters
print(company.upper())

# Change all characters to lowercase letters
print(company.lower())

# Use capitalize(), title(), swapcase() methods
print(company.capitalize())  # First letter capitalized
print(company.title())  # First letter of each word capitalized
print(company.swapcase())  # Swap uppercase and lowercase

# Cut (slice) out the first word of the string
first_word = company.split()[0]
print(first_word)

# Check if the string contains the word 'Coding'
contains_coding = "Coding" in company
print(contains_coding)

# Replace the word 'Coding' with 'Python'
replaced_string = company.replace('Coding', 'Python')
print(replaced_string)

# Change 'Python for Everyone' to 'Python for All' using replace()
string_to_replace = "Python for Everyone"
replaced_string2 = string_to_replace.replace('Everyone', 'All')
print(replaced_string2)

# Split the string 'Coding For All' using space as the separator
split_string = company.split()
print(split_string)

# Split the string 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' at the comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(', ')
print(split_companies)

# Character at index 0 in the string 'Coding For All'
first_char = company[0]
print(first_char)

# Last index of the string 'Coding For All'
last_index = len(company) - 1
print(last_index)

# Character at index 10 in the string 'Coding For All'
char_at_index_10 = company[10]
print(char_at_index_10)

# Create an acronym for 'Python For Everyone'
acronym1 = ''.join(word[0] for word in "Python For Everyone".split())
print(acronym1)

# Create an acronym for 'Coding For All'
acronym2 = ''.join(word[0] for word in "Coding For All".split())
print(acronym2)

# Use index to determine the position of the first occurrence of 'C' in 'Coding For All'
index_of_c = company.index('C')
print(index_of_c)