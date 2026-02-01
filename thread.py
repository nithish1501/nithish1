from threading import Thread
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

threads = []
for i in range(3):
    t = Thread(target=task, args=(f"Task-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()