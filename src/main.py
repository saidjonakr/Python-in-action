import random
from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
from task3 import decorator_1

@decorator_1
def func():
    print("Start 1")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)

@decorator_1
def funx(n=2, m=5):
    print("Start 2")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    kwargsAcceptFun(name="Alice", age=30, city="Wonderland")
    
    transformed = typeBasedTransformer(a=4, b=2.5, c="Hello", d=True, e=[1, 2, 3], f={"a": 1, "b": 2})
    print(transformed)
    
    func()
    funx()
    func()
    funx()
    func()
