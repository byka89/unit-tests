import requests

class YaUploader:

    host = "https://cloud-api.yandex.net/"
    token = "y0_AgAA..."

    def get_headers(self):
        return {
            'Content-Type': 'application/json', 'Authorization': f'OAuth {self.token}'
        }
    
    def create_a_folder(self,path):
        headers = self.get_headers()
        url = self.host + "v1/disk/resources"
        params = {"path": path}
        res = requests.put(url, params=params, headers=headers)
        return res.status_code