import sys

def sample_lines(file_path, line_numbers):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file, start=1):
            if i in line_numbers:
                yield line

def main():
    # 第一个参数是文件路径，后续参数是行号
    file_path = sys.argv[1]
    line_numbers = set(map(int, sys.argv[2:]))

    for line in sample_lines(file_path, line_numbers):
        print(line, end='')

if __name__ == "__main__":
    main()
