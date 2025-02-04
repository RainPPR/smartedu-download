import sys
import download
import threading

def Main():
    if len(sys.argv) == 1:
        raise ValueError("传入的参数格式不正确")

    threads = []
    for id in sys.argv[1:]:
        thread = threading.Thread(target=download.download, args=(id, '../pdf/'))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("所有下载完成！")

if __name__ == "__main__":
    Main()
