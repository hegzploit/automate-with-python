#!/usr/bin/python3

from tqdm import trange
import time
from signal import signal, SIGINT


def handler(signum, time):
    print('\n HAHA not stoppig :)')


signal(SIGINT, handler)

for _ in trange(1000000):
    time.sleep(0.1)
