# 单例模式，让一个类创建出唯一的实例
from functools import wraps
import dis
def singleton(cls):
    # 单例类装饰器
    instances = {}
    @wraps(cls)
    def wrapper(*args,**kwargs):
        if cls not in instances:
            instances[cls]=cls(*args,**kwargs)
        return instances[cls]
    return wrapper

@singleton
class President:
    pass

# 不使用中间变量，交换两个变量的值
def changetwo(a,b):
    a = 1
    b = 2
    a,b = b,a
    print(a,b)
    a = 1
    b = 2
    c = 3
    a,b,c = c,b,a #元组解包
    print(a,b,c)
    t = ("a","b","c")
    a,b,c = t
    print(a,b,c)

# 删除列表中重复元素的函数，要求去重后元素相对位置保持不变
def removesame(items):
    no_dup_items = []
    seen = set()
    for item in items:
        if item not in seen:
            no_dup_items.append(item)
            seen.add(item)
    return no_dup_items

print(removesame([1,2,1,1,3,4,6,6,7,2]))
# CPython解释器
a,b,c,d = 1,1,1000,1000
print(a is b,c is d)
def foo():
    e = 1000
    f = 1000
    print(e is f, e is d)
    g = 1
    print(g is a)

foo()

# lambda函数
# 用一行代码来实现求最大公约数的函数
gcd = lambda x,y:y%x and gcd(y%x,x) or x
levelmul = lambda x: levelmul(x-1)*x if x>=2 else 1
print(levelmul(4))

# filter 筛选出奇数
# map 生成平方
items = [12,5,7,10,8,19]
items = list(map(lambda x:x**2,filter(lambda x:x%2,items)))
print(items)
items = [12,5,7,10,8,19]
# 列表的生成式
items = [e**2 for e in items if e%2]
print(items)

# copy vs deepcopy
import pickle
my_deep_copy = lambda obj:pickle.loads(pickle.dumps(obj))
import copy
# 基于原型对象创建对象
class PrototypeMeta(type):
    def __init__(cls,*args,**kwargs):
        super().__init__(*args,**kwargs)
        cls.clone = lambda self,is_deep=True:copy.deepcopy(self)if is_deep else copy.copy(self)
class Person(metaclass=PrototypeMeta):
    pass

p1 = Person()
p2 = p1.clone()
p3 = p1.clone(is_deep=False)

s = "/../ab/"
L = []
L.pop()








