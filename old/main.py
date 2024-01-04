import json
import requests

API_KEY = 'b7a19832219fb4b4f1c1532b821b340945672961'

domain_name = 'stripe.com'
# email_name = 'maximsidorchuk@gmail.com'
# email_name = 'miannahabibi@gmail.com'
email_name = 'patrick@stripe.com'

url_domain_search = f'https://api.hunter.io/v2/domain-search?domain={domain_name}&api_key={API_KEY}'
url_email_verification = f'https://api.hunter.io/v2/email-verifier?email={email_name}&api_key={API_KEY}'


def get_info() -> dict:
    res = requests.get(url_email_verification)
    response = json.loads(res.text)["data"]
    return response


def save_data(data):
    new_data = {"email": data["email"], "data": data}

    try:
        with open(f"../data/email_validation.json", encoding="utf8") as file:
            data = json.load(file)
            data.append(new_data)
            with open(f"../data/email_validation.json", "w", encoding="utf8") as outfile:
                json.dump(data, outfile, indent=4, ensure_ascii=False)
    except:
        with open(f"../data/email_validation.json", "w", encoding="utf8") as outfile:
            json.dump([new_data], outfile, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    save_data(get_info())
