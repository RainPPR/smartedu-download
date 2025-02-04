import sys
import download

def Main():
    if len(sys.argv) == 1:
        raise ValueError("传入的参数格式不正确")
    for id in sys.argv[1:]:
        download.download(id, '../pdf/')

if __name__ == "__main__":
    Main()
