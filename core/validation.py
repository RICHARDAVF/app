import requests
import json
class Validation:
    def __init__(self,dni) -> None:
        self.dni  = dni

    def valid(self):
        data = {}
        response = requests.get(f'https://my.apidevs.pro/api/dni/{self.dni}',headers = {
                    "Authorization":'Bearer 7d41929a0671ebe6d17c4976dab50e2f11db3736e915ec2712ab8d865a56a3c8'
                })
        res=json.loads(response.text)
        if not (res['success']):
            data['error'] = res['message']
        else:
            data = res
        return data