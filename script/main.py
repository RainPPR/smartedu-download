import sys
import download

def Main():
    if len(sys.argv) != 2:
        raise ValueError("传入的参数格式不正确")
    download.download(sys.argv[1], '../pdf/')

if __name__ == "__main__":
    Main()
