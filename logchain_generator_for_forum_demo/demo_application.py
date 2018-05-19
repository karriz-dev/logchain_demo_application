# gw의 순서대로 tx를 발생시킨다. gw3->gw4->gw10->gw8->gw6

# tx 발생시 3s 정도의 딜레이를 준다.

# 모든 tx를 전송한뒤에는 블록이 생성될것이다.(5개) 그리고 10s 딜레이를 준다.

# 이과정을 무한 반복한다.

import requests
from time import sleep

gw_list = {'192.168.0.5', '192.168.0.9', '192.168.0.6', '192.168.0.11', '192.168.0.8'}


def make_transaction(gw, data):
    print('(' + gw + ')' + ' send transaction : ' + data)
    requests.post(gw, data=data, headers={'Content-Type': 'application/json; charset=utf-8'})


if __name__ == "__main__":
    index = 0
    data = {'tx_title': 'test', 'tx_body': 'test_body'}
    while True:
        for index in range(0, 4):
            make_transaction(gw_list[index], data)
            sleep(3)
        sleep(10)
