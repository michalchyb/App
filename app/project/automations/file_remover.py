import os

dir = "C:/Users/macy/Downloads/"
ext = (".ica")

def remove_files() -> None:
    for files in os.listdir(dir):
        if files.endswith(ext):
            print(files)
            os.remove(dir + files)
            print("The file has been removed")
