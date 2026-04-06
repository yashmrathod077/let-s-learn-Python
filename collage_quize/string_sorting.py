import time

line = ("""Hamne Wahi lagaya dill jaha dill lagana mana tha \n
           aakhir wahi kiya sajde jaha sir zukana mana tha """)
words = line.split()

for word in words:
    print(word, end=' ', flush=True)
    time.sleep(0.4)   # delay between words

print()