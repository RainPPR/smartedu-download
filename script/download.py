import sys
import common
import random
import threading
import urllib

def download_id(ids, path='../pdf/'):
    semaphore = threading.Semaphore(4)

    def m_download(id, path):
        with semaphore:
            data = common.fetch_json(f'https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{id}.json')
            path = path + data['title'] + '.pdf'
            print(f'开始下载：{data['title']}.pdf')
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

def download_url(url, path='../pdf/'):
    tags = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)['defaultTag'][0].split('/')
    list_url = common.fetch_json('https://s-file-1.ykt.cbern.com.cn/zxx/ndrs/resources/tch_material/version/data_version.json')['urls'].split(',')
    
    list_id = []
    def m_add(item):
        if len(item['tag_paths']) > 0:
            list_tags = item['tag_paths'][0].split("/")[2:]
            if all(item in list_tags for item in tags):
                list_id.append(item['id'])

    for url in list_url:
        for item in common.fetch_json(url):
            m_add(item)

    download_id(list_id, path)

def Main():
    if len(sys.argv) == 1:
        raise ValueError("传入的参数格式不正确")
    download_id(sys.argv[1:])

if __name__ == "__main__":
    Main()
