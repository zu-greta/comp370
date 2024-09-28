Task 2:
How big is the dataset?
- 4.6M size. 36860 lines.
What’s the structure of the data? (i.e., what are the field and what are values in them)
- fields: title, writer, pony, dialog
How many episodes does it cover?
- 198 (>>> csvtool -c 1 clean_dialog.csv | uniq | wc -l)
During the exploration phase, find at least one aspect of the dataset that is unexpected – meaning that it seems like it could create issues for later analysis.
- some dialog lines contain things like "<U+0097>" and also gestures included in [].
- different versions of a character (eg. mean twilight sparkle)
- some rows have two characters speaking at once or everyone except a certain pony

Task 3:
Use the grep tool to determine how often each MAIN (Twilight Sparkle, Rarity, Pinkie Pie, Rainbow Dash, and Fluttershy) pony speaks.
*(not counting different version of the ponies)*
>>> csvtool -c 3 clean_dialog.csv| grep "^<pny name>$" | wc -l
- Twilight Sparkle: 4745 lines total 
- Rarity: 2660 lines
- Pinkie Pie: 2833 lines
- Rainbow Dash: 3072 lines
- Fluttershy: 2109 lines
Now calculate the percent of lines that each pony has over the entire dataset (including all characters).
- Twilight Sparkle: 12.87%
- Rarity: 7.22%
- Pinkie Pie: 7.69%
- Rainbow Dash: 8.33%
- Fluttershy: 5.72%