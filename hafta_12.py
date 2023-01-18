#thread
import threading
def thread_function():
    for i in range(1, 100000):
        print(i, " - Thread çalıştı")
def thread_function2():
    for i in range(1, 100000):
        print(i, " 1111111111111111")
thread = threading.Thread(target=thread_function)
thread2 = threading.Thread(target=thread_function2)
thread.start()
thread2.start()

#thread_pool
import concurrent
from concurrent.futures import ThreadPoolExecutor
def square(x):
    return x * x
with ThreadPoolExecutor() as executor:
    results = []
    for i in range(10):
        results.append(executor.submit(square, i))
for f in concurrent.futures.as_completed(results):
    print(f.result())
