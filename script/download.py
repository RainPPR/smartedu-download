import sys
import common
import random
import threading

def download_id(ids, path='../pdf/'):
    semaphore = threading.Semaphore(4)

    def m_download(id, path):
        with semaphore:
            data = common.fetch_json(f'https://s-file-{random.randint(1, 3)}.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{id}.json')
            path = path + data['global_title']['zh-CN'] + '.pdf'
            print(f'开始下载：{data['global_title']['zh-CN']}.pdf')
            for item in data['ti_items']:
                if item['ti_format'] != 'pdf':
                    continue
                common.download_file(item['ti_storages'][0].replace('-private', ''), path)
                return path
            raise ValueError("找不到对应的 pdf 文件")

    threads = []
    for id in ids:
        thread = threading.Thread(target=m_download, args=(id, path))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    print("下载完成！")

def Main():
    if len(sys.argv) == 1:
        raise ValueError("传入的参数格式不正确")
    download_id(sys.argv[1:])

if __name__ == "__main__":
    Main()
