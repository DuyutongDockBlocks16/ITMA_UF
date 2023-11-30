#!/bin/bash

# 定义输入目录和每个文件的样本大小
input_directory="/work/courses/unix/T/ELEC/E7130/general/trace/flow-continue"
sample_per_file=7126

# 定义IPv4和IPv6输出文件
output_ipv4_file="./output_sampled_ipv4.txt"
output_ipv6_file="./output_sampled_ipv6.txt"

# IPv4和IPv6的正则表达式
ipv4_regex="^([0-9]{1,3}\.){3}[0-9]{1,3}$"
ipv6_regex="^(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:))"

# 删除已存在的输出文件
rm -f "$output_ipv4_file" "$output_ipv6_file"

# 获取文件总数
total_files=$(find "$input_directory" -type f | wc -l)
current_file=0

# 处理每个文件
for file in "$input_directory"/*; do
    if [ -f "$file" ]; then
        let current_file++
        echo "正在处理 ($current_file / $total_files): $file"

        # 直接使用指定路径的文件
        temp_ipv4="./temp_ipv4"
        temp_ipv6="./temp_ipv6"

        # 清空或初始化这些文件
        > "$temp_ipv4"
        > "$temp_ipv6"

        # 将文件分割为IPv4和IPv6两部分
        tail -n +29 "$file" | awk -v ipv4_regex="$ipv4_regex" '$1 ~ ipv4_regex' > "$temp_ipv4"
        tail -n +29 "$file" | awk -v ipv6_regex="$ipv6_regex" '$1 ~ ipv6_regex' > "$temp_ipv6"

        # 对IPv4临时文件抽样
        total_lines_ipv4=$(wc -l < "$temp_ipv4")
        if [ $total_lines_ipv4 -ge $sample_per_file ]; then
            selected_lines_ipv4=($(shuf -i 1-$total_lines_ipv4 -n $sample_per_file))
            python3 sample_script.py "$temp_ipv4" "${selected_lines_ipv4[@]}" >> "$output_ipv4_file"
        else
            cat "$temp_ipv4" >> "$output_ipv4_file"
        fi

        # 对IPv6临时文件抽样
        total_lines_ipv6=$(wc -l < "$temp_ipv6")
        if [ $total_lines_ipv6 -ge $sample_per_file ]; then
            selected_lines_ipv6=($(shuf -i 1-$total_lines_ipv6 -n $sample_per_file))
            python3 sample_script.py "$temp_ipv6" "${selected_lines_ipv6[@]}" >> "$output_ipv6_file"
        else
            cat "$temp_ipv6" >> "$output_ipv6_file"
        fi

        # 不再需要删除这些文件
        # rm -f "$temp_ipv4" "$temp_ipv6"
    fi
done

echo "抽样完成，IPv4结果保存在 $output_ipv4_file，IPv6结果保存在 $output_ipv6_file"

