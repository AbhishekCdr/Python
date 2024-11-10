# Python is primarilay a single threaded language but it does support multithreading and multi processing 

"""
-> Single Threaded Nature

Python has a global interpreter lock (GIL) which ecsure tat only one thread executes python bytecode at a time

-> Multi Threaded Nature

Python has the threadeing moudule using which we can create and manage the threads

because of GIL multi-threading does't provide significant performance improvements for CPU bond task


-> Multi Processing in Python
in order to take full advantage  Pytonn offers multiprocessing module which avoids the GIL by spawning seperate processes each with its own python interpreter

"""