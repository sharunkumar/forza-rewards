import requests
import json
import sys

def send_message(webhook, msg):
    payload = {
        "content": msg
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(webhook, data=json.dumps(payload), headers=headers)

    print(response.status_code, response.text)


if __name__ == '__main__':
    arg = sys.argv[1:]
    send_message(arg[0], open("output.txt", 'r').read())