

def superhiro(superhiro_url):
    result_dict = {}
    for i in superhiro_url:
        resp = requests.get(i)
    # pprint(res.json())
        result_dict[resp.json()['results'][0]['name']] = \
            [resp.json()['results'][0]['powerstats']['intelligence']]
    pprint(f"общие результаты {result_dict}")
    pprint(f'в конкурсе самый умный супергерой победил {max(result_dict.items())}')


superhiro(["https://superheroapi.com/api/2619421814940190/search/Captain America",
           "https://superheroapi.com/api/2619421814940190/search/Thanos",
           "https://superheroapi.com/api/2619421814940190/search/Hulk"])



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload_my_mac(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': file_path, 'overwrite': 'true'}
        respose = requests.get(url=upload_url, params=params, headers=headers)
        resp = requests.put(respose.json()['href'], data=open(path_to_file, 'rb'))
        pprint(respose.json())
#


if __name__ == '__main__':
    path_to_file = 'asdfrewq.txt'
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload_my_mac(path_to_file)




    def upload_for_net(self, file_pass: str):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': file, 'url': file_pass}
        r = requests.post(url=upload_url, params=params, headers=headers)
        res = r.json()
        pprint(res)




if __name__ == '__main__':
    dounload_path = "https://yt3.ggpht.com/a/AGF-l7_KPxu7Jqpz4w2F3gOAWuuQDmM-Tt76d2j3ww=s900-c-k-c0xffffffff-no-rj-mo"
    file = 'nft.jpg'

    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload_for_net(dounload_path)




def stackexchange():
    url = "https://api.stackexchange.com/2.3/questions?"
    params = {'sort': 'activity', 'tagged': ['python'], 'site': 'stackoverflow', 'order': 'desc',
              'fromdate': '2021-09-07', 'todate': '2021-09-09' }
    r = requests.get(url=url, params=params)
    pprint(r.json())


stackexchange()