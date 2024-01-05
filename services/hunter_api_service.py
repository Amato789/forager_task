import requests
import json
from config import HUNTER_API_KEY


class HunterApiService:
    api_key = HUNTER_API_KEY
    email_url = 'https://api.hunter.io/v2/email-verifier'
    domain_url = 'https://api.hunter.io/v2/domain-search'


    def email_verify(self, email: str):
        return json.loads(requests.get(self.email_url, params={'email': email, 'api_key': self.api_key}).text)['data']

    def domain_search(self, domain: str):
        return json.loads(requests.get(self.domain_url, params={'domain': domain, 'api_key': self.api_key}).text)['data']
