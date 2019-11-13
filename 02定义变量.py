# 1.第一次=表示定义变量
age=100
# 2.第二次=表示使用变量
age=age-90
# 3.变量的类型
#整数
high=100
#浮点
price=3.4
#字符串
sex="男"
#布尔值   1表示True,非1表示False
isenter=False
isenter=True
#空值  表示空值不等于0
None
#常量  没有限制不能修改常量只是用大写规范
PI=123123
PI=123333
print(PI)
#列表
list1 = ['physics', 'chemistry', 1997, 2000]
#字典
# 特点
# 1.可变容器模型，且可存储任意类型对象
# 2.键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
# 3.值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组
# 4.Python中字典和json不是一个东西 json的key是双引号,字典的key是单引号

dict = {'a': 1, 'b': 2, 'b': '3'}
#注意对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向
y=1
x=y
y=2
y=x
x=2
print(y)
# 整数未开辟新空间,所以id值是一样
x=1
print(id(x))
y=x
x=2
y=1
print(id(y))

# 字符串生成的id不一致 ,说明字符串是新开辟了内存空间
x='abc'
print(id(x))
y=x
x='ab'
y='adc'
print(id(y))



