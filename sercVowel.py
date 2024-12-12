import re

str = "Hello worzlda !"

regex = r'[aeuoi]'

str = str.lower()
vowels = 0
consonants = 0

for i in str:
    if i in regex:
        vowels = vowels + 1
    else:
        consonants = consonants + 1

print(f"Number of consonants present in the string is {consonants}")
print(f"Number of vowels present in the string is {vowels}")