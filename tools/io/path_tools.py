import subprocess
import platform
import os


def mac_filepath_transform(filepath):
    # 如果是Mac系统需要做一次转换
    if platform.system() == "Darwin":
        filepath = filepath.replace('\\', r'/')
    return filepath

def open_finder_dirpath(dir_path):
    if os.path.exists(dir_path):
        subprocess.call(["open", "-R", dir_path])


def get_filename_no_suffix(filepath):
    filename = os.path.basename(r'%s' % filepath)
    filename_no_suffix = os.path.splitext(filename)[0]
    print(filepath, filename, filename_no_suffix)
    return filename_no_suffix


def get_abs_filepath(filepath):
    abs_filepath = os.path.abspath(filepath)
    abs_dirpath = os.path.dirname(abs_filepath)
    filename = os.path.basename(abs_filepath)
    filename_no_suffix = get_filename_no_suffix(filepath=filepath)
    return abs_dirpath, filename_no_suffix


def get_filepath_lst_by_dirpath(dirpath, included_suffix=[]):
    if os.path.exists(dirpath):
        filepath_lst = [x for x in os.listdir(dirpath) if x.endswith(tuple(included_suffix))]
        return filepath_lst
    else:
        return []


if __name__ == "__main__":
    filepath = './users/b.txt'
    result = get_abs_filepath(filepath=filepath)
    print(result)
