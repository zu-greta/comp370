#!/bin/bash

ponies=("Twilight Sparkle" "Rarity" "Pinkie Pie" "Rainbow Dash" "Fluttershy")

input_file="clean_dialog.csv"
output_file="Line_percentages.csv"

total_lines=$(csvtool -c 3 "$input_file"| wc -l)

echo "pony_name,total_line_count,percent_all_lines" > "$output_file"

for pony in "${ponies[@]}"; do
	count=$(csvtool -c 3 "$input_file" | grep "^${pony}$" | wc -l)
	percent=$(echo "scale=2; ($count / $total_lines) * 100" | bc)
	echo "${pony},${count},${percent}" >> "$output_file"
done

