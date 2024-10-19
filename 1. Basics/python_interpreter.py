"""

PVM -> Python Virtual Machine

https://www.youtube.com/watch?v=BkHdmAhapws

https://medium.com/illumination/how-does-python-actually-work-9d00bf6dd02b#:~:text=When%20you%20run,%20python%20source.py.%20Here%20python%20is%20the%20interpretor,

-> Get the compiled pyhton code

python3 -m py_compile file.py

-> the compiled code is saved in __pycache__ folder

--> Python internally compiles the source code into and intermediate code called bytecode

--------------

Bytecode -> it is lower level representational of the python code

we can look into __pycache__ folder and find the same with and extension of .pyc

bytecode make the execution faster by skipping parsing and syntax analysis in subsequent runs

---------------

Once the bytecode is generated it is sent to PVM -> python virtual machine

FLOW: Source Code -> ByteCode -> PVM



"""