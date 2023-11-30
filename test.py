import glob

# 定义数据文件的目录
directory_path = 'files/my_files/'

# 使用 glob 来获取目录下的所有文件路径
file_paths = glob.glob(directory_path + '*.t2')

# 统计文件数量
file_count = len(file_paths)

# 统计所有文件的总行数
total_lines = sum(1 for file in file_paths for _ in open(file))

print(f"files number：{file_count}")
print(f"lines number：{total_lines}")
