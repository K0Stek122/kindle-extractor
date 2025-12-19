# Python 3 Object-Oriented Programming, Third Edition
- Author: Dusty Phillips
---
> Usually, we don't need to be overly concerned with data types at the design stage,
- Page 32
- Date Added: 2024-02-10 10:22:57
---
> Python has a utility called the global interpreter lock, or GIL. It's impossible to turn off, and it means that threads are useless in Python for one thing that they excel at in other languages: parallel processing.
- Page 542
- Date Added: 2024-02-20 08:22:08
---
> GIL is released as soon as the thread starts to wait for something.
- Page 542
- Date Added: 2024-02-20 08:22:22
---
> Pay special attention to the if __name__ == '__main__': guard around the module level code that prevents it running if the module is being imported, rather than run as a program. This is good practice in general, but when using multiprocessing on some operating systems, it is essential.
- Page 544
- Date Added: 2024-02-20 08:25:04
---
> If we need more control over communication between processes, we can use a Queue. Queue
- Page 549
- Date Added: 2024-02-20 08:28:52
---
> This use of queues is actually a local version of what could become a distributed system.
- Page 552
- Date Added: 2024-02-20 08:30:49
---
> the primary drawback is that sharing data between processes is costly.
- Page 552
- Date Added: 2024-02-20 08:31:33
---
> Excessive pickling quickly dominates processing time.
- Page 552
- Date Added: 2024-02-20 08:31:49
---
> They don't completely solve the problem of accidentally altering shared state,
- Page 553
- Date Added: 2024-02-20 08:32:36
---
> the external environment is passed into the function or returned from it. This is not a technical requirement, but it is the best way to keep your brain inside your skull when programming with futures.
- Page 554
- Date Added: 2024-02-20 08:34:05
---
> Once the executor has been constructed, we submit a job to it using the root directory. The submit() method immediately returns a Future object, which promises to give us a result eventually. The future is placed in the queue. The loop then repeatedly removes the first future from the queue and inspects it.
- Page 556
- Date Added: 2024-02-20 08:35:25
---
> AsyncIO is the current state of the art in Python concurrent programming. It combines the concept of futures and an event loop with the coroutines we discussed in Chapter 9, The Iterator Pattern.
- Page 556
- Date Added: 2024-02-20 08:35:46
---
> the need to manually advance to the first send location. The result is concurrent code that we can reason about as if it were sequential.
- Page 557
- Date Added: 2024-02-20 08:36:53
---
> An AsyncIO coroutine executes each line in order until it encounters an await statement, at which point, it returns control to the event loop.
- Page 561
- Date Added: 2024-02-20 08:37:08
---
> AsyncIO was specifically designed for use with network sockets,
- Page 562
- Date Added: 2024-02-20 08:38:01
---
> Because it is capable of handling many thousands of simultaneous connections, AsyncIO is very common for implementing servers.
- Page 569
- Date Added: 2024-02-20 08:41:53
---
