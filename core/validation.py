import requests
import json
import dotenv
import os
dotenv.load_dotenv()

class Validation:
    def __init__(self,dni) -> None:
        self.dni  = dni

    def valid(self):
        data = {}
        response = requests.get(f'https://my.apidevs.pro/api/dni/{self.dni}',headers = {
                    "Authorization":f'Bearer {os.getenv("TOKEN_DNI")}'
                })
        res=json.loads(response.text)
        if not (res['success']):
            data['error'] = res['message']
        else:
            data = res
        return data