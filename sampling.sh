#!/bin/bash

# Define the input directory and the sample size per file
input_directory="/work/courses/unix/T/ELEC/E7130/general/trace/flow-continue"
sample_per_file=7126

# Define the output files for IPv4 and IPv6
output_ipv4_file="./output_sampled_ipv4.txt"
output_ipv6_file="./output_sampled_ipv6.txt"

# Regular expressions for IPv4 and IPv6
ipv4_regex="^([0-9]{1,3}\.){3}[0-9]{1,3}$"
ipv6_regex="^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))"

# Remove existing output files
rm -f "$output_ipv4_file" "$output_ipv6_file"

# Get the total number of files
total_files=$(find "$input_directory" -type f | wc -l)
current_file=0

# Process each file
for file in "$input_directory"/*; do
    if [ -f "$file" ]; then
        let current_file++
        echo "Processing file ($current_file / $total_files): $file"

        # Directly use specified file paths
        temp_ipv4="./temp_ipv4"
        temp_ipv6="./temp_ipv6"

        # Clear or initialize these files
        > "$temp_ipv4"
        > "$temp_ipv6"

        # Split the file into IPv4 and IPv6 parts
        tail -n +29 "$file" | awk -v ipv4_regex="$ipv4_regex" '$1 ~ ipv4_regex' > "$temp_ipv4"
        tail -n +29 "$file" | awk -v ipv6_regex="$ipv6_regex" '$1 ~ ipv6_regex' > "$temp_ipv6"

        # Sample the IPv4 temporary file
        total_lines_ipv4=$(wc -l < "$temp_ipv4")
        if [ $total_lines_ipv4 -ge $sample_per_file ]; then
            selected_lines_ipv4=($(shuf -i 1-$total_lines_ipv4 -n $sample_per_file))
            python3 sample_script.py "$temp_ipv4" "${selected_lines_ipv4[@]}" >> "$output_ipv4_file"
        else
            cat "$temp_ipv4" >> "$output_ipv4_file"
        fi

        # Sample the IPv6 temporary file
        total_lines_ipv6=$(wc -l < "$temp_ipv6")
        if [ $total_lines_ipv6 -ge $sample_per_file ]; then
            selected_lines_ipv6=($(shuf -i 1-$total_lines_ipv6 -n $sample_per_file))
            python3 sample_script.py "$temp_ipv6" "${selected_lines_ipv6[@]}" >> "$output_ipv6_file"
        else
            cat "$temp_ipv6" >> "$output_ipv6_file"
        fi

        # No longer need to delete these files
        # rm -f "$temp_ipv4" "$temp_ipv6"
    fi
done

echo "Sampling completed, IPv4 results saved in $output_ipv4_file, IPv6 results saved in $output_ipv6_file"
