#!/usr/bin/env python3
from datetime import datetime
import os
import sys
import time
import json

from lib.constants import BACKOFF, MAX_ATTEMPTS, MAX_STATUS_LEN, TIMEOUT_BACKOFF

# from lib import images
# from lib import mastodon
# from lib import twitter
from lib import words


def main():
    print(f"[{datetime.now()}] Start")
    words.init_pronouncing()

    with open("oracle-cards.json", "rt") as f:
        database = json.load(f)

    # database = [
    #     {"name": "Nicol Bolas, the Arisen"},
    #     {"name": "Isamaru, Hound of Konda"},
    #     {"name": "Kiki-Jiki, Mirror Breaker"},
    # ]

    banned = ["Rivals of Ixalan Checklist"]

    card_set = set()

    for card in database:
        if "name" in card:
            for card_name in card["name"].split(" // "):
                if card_name not in banned and words.isTMNT(card_name, debug=False):
                    card_set.add(card_name)

    print(f"Number of TMNT cards: {len(card_set)}")
    for card in sorted(card_set):
        print(f"TMNT: {card}")

    print(f"[{datetime.now()}] Complete! \n=====")


if __name__ == "__main__":
    main()
