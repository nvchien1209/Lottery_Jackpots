import requests
from bs4 import BeautifulSoup
import sys


def get_jackpots():
    jackpots = dict()
    link = 'http://ketqua.net'
    data = requests.get(link)
    soup = BeautifulSoup(data.text, 'html.parser')

    for ketqua in soup.find_all('td')[1:38]:
        if ketqua.string is not None:
            if not ketqua.string.isdigit():
                current_id = ketqua.string
                jackpots[ketqua.string] = []
            else:
                jackpots[current_id].append(ketqua.string)
    return jackpots


def main():
    jackpots = get_jackpots()
    jackpots_2 = []
    for jackpot in jackpots.values():
        jackpots_2.extend(jackpot)
    jackpots_2 = [i[-2:] for i in jackpots_2]
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            if not i.isdigit():
                print(i + ': invalid')
            else:
                result = i in jackpots_2
                print(i, ':', result)
    else:
        for i in jackpots.items():
            print(i)


if __name__ == '__main__':
    main()