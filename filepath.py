def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

for line in read_large_file("data.txt"):
    print(line)