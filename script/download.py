import common

def download(id, path):
    data = common.fetch_json(f'https://s-file-1.ykt.cbern.com.cn/zxx/ndrv2/resources/tch_material/details/{id}.json')
    path = path + data['global_title']['zh-CN'] + '.pdf'

    print(path, data['smart_link']['smart_link'])

    for item in data['ti_items']:
        if item['ti_format'] != 'pdf':
            continue
        common.download_file(item['ti_storages'][0].replace('-private', ''), path)
        return path

    raise ValueError("找不到对应的 pdf 文件")
