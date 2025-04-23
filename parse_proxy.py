#!/usr/bin/env python
import yaml
import random


def get_random_proxy():
    _proxy_list = []
    _proxy_strings = []
    with open("proxy.yml") as stream:
        try:
            _proxy_list = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    for proxy in _proxy_list:
        if "sec" in proxy['Last Checked'] and "Germany" in proxy['Country']:
            print(proxy)
            _proxy_strings.append(proxy['IP Address'] + ':' + proxy['Port'])
        else:
            continue
    return random.choice(_proxy_strings)

print(get_random_proxy())
