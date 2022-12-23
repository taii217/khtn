import os

def read_file(namefile):
    with open (namefile,'r') as readfile:
        d = readfile.read().splitlines()
    return d


def write_file(namefile, data):
    file1 = open(namefile, "w")
    for i, line in enumerate(data):
        if i == len(data) - 1:
            file1.write(f'{line}')
            return
        file1.write(f'{line}\n')


def write_file_split(path1, path2, data, is_hidden=False):
    try:
        file1 = open(os.path.expanduser(path1), "w")
        file2 = open(os.path.expanduser(path2), "w")
    except Exception as e:
        # os.remove("demofile.txt")
        # os.remove("demofile.txt")
        # try:
        #     file1 = open(os.path.expanduser(path1), "w")
        #     file2 = open(os.path.expanduser(path2), "w")
        # except Exception as e:
        return False, 'File đã ẩn và tồn tại, không thể ghi'

    if is_hidden:
        os.system(f"attrib +h {path1}")
        os.system(f"attrib +h {path2}")

    n = len(data) / 2
    for i, line in enumerate(data):
        if i < n:
            file1.write(f'{line}\n')
        else:
            file2.write(f'{line}\n')
    return True, ''


def merge_file(path1, path2) -> list:
    data = []

    with open(path1, 'r') as readfile:
        d1 = readfile.read().splitlines()

    with open(path2, 'r') as readfile:
        d2 = readfile.read().splitlines()

    return d1 + d2












