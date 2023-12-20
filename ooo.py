#!/usr/bin/env python
"""
A raffle random-person chooser thing. To make this work,
    pip install progress
Then edit the `PEOPLE` list, then run it:
    python raffle.py
or
    ./raffle.py
"""
import random
from progress.bar import Bar


PEOPLE = [
  'Person 1',
  'Person 2'
]


print("\n\n")
bar = Bar('And the winner is...', max=10)
for i in range(10):
    [x for x in range(999999)]  # short pause...
    bar.next()
bar.finish()
print("\n\n\t{}!\n\n".format(random.choice(PEOPLE)))
print("-" * 60 + "\n")