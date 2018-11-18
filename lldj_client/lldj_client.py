#!/usr/bin/env python

# lldj client

import requests

#hardcoded lldj server address

LLDJ_SERVER_URL = 'http://katsumoto.pythonanywhere.com'
            
def test_http_request(url, lldj_address):
    payload = {'getip': 'true', 'address': lldj_address}
    r = requests.get(url, payload)
    print(str(r.text))


def make_get_request(payload):
    return requests.get(LLDJ_SERVER_URL, payload)


def get_my_ip():
    """Fetches the ip of the sender."""
    payload = {'getip': ''}
    r = make_get_request(payload)
    ip_clean = str.strip(r.text.split(":")[1])
    return ip_clean

def get_ip_for(address):
    """Gets the ip address associated with the given lldj_address."""
    payload = {'getip': str(address)}
    r = make_get_request(payload)
    ip_clean = str.strip(r.text.split(":")[1])
    return ip_clean

def set_ip_for(address):
    """Sets a new lldj_address with the ip of the sender."""
    payload = {'setip': str(address)}
    r = make_get_request(payload)
    print(str(r.text))


def update_ip_for(address):
    """Updates the current ip with the ip of the sender for the given lldj_address."""
    payload = {'update': str(address)}
    r = make_get_request(payload)
    print(str(r.text))


def get_all_addresses():
    payload = {'list': ''}
    r = make_get_request(payload)
    print(str(r.text))


def clear_all_addresses():
    payload = {'clear': ''}
    r = make_get_request(payload)
    print(str(r.text))


if __name__ == "__main__":
    print("lldj_client tests")
    #test_http_request("http://localhost:58922/", "gitlabaddress")
    ip = get_my_ip()
    print(ip)
    print(get_ip_for("dark"))
    set_ip_for("dark")
    update_ip_for("dark")



