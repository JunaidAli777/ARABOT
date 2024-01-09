# ARABOT Readme

## English-Arabic dictionary telegram bot
The bot would take an english word from the user as text and return reply back its meaning in arabic
and vice versa. It would also reply back a few similar words along with the meaning, if the word isn't found, the reply would only consist of the similar words.

## Resource at hand
- Excel file which had both Eng-Ar and Ar-Eng word translations

## Programming Langauge
- Python

## Modules and packages used
- pandas
- typing
- telegram
- telegram.ext
- fuzzywuzzy
- re

## Issues faced
- Since the data was raw, many english words randomly has upper case letters in them. Needed to process the data a bit by dividing the file into two different files and converting all of the english words into lowercase and made sure that the user_text is converted into lowercase as well.

- To add a similar word word section, tried out a few different packages but many were unsatisfactory, at last fuzzywuzzy to be quite apt because of its brevity and efficiency.

- The random diacritical marks in the Ar-Eng file created another issue in the words getting detected as result of which, decided to process the data a bit again, and stripped off all the diacritical marks and made the same for the user-texts as well if in Arabic, for the words to match properly in a systematic manner.