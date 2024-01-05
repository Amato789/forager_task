import requests
import json
from config import HUNTER_API_KEY


class HunterApiService:
    api_key = HUNTER_API_KEY
    base_url = 'https://api.hunter.io/v2/email-verifier'

    def email_verify(self, email: str):
        return json.loads(requests.get(self.base_url, params={'email': email, 'api_key': self.api_key}).text)['data']

    def domain_search(self, domain: str):
        pass
