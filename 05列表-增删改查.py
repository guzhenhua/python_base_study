# 1.列表定义:一系列按照特定顺序排列的元素
# 特点区别其他语法:可以装不同的数据类型

# 1.1如何访问列表元素 (索引从0开始而不是1开始)
name_list=['张三','李四','王五','赵六']
print(name_list[0])
print(name_list[-1])

# 1.2修改列表元素
name_list1=['张三','李四','王五','赵六']
name_list1[0]='guzhenhua'
print(name_list1[0])
print(name_list1)

# 1.3在列表中添加元素
name_list2=['张三','李四','王五','赵六']
name_list2.append('樱木花道')
name_list2.append('流川枫')
print(name_list2)

# 1.4在地址索引位置插入元素
name_list3=['张三','李四','王五','赵六']
name_list3.insert(0,'第一个人')
print(name_list3)

# 1.5删除制定索引的元素
name_list4=['张三','李四','王五','赵六']
del name_list4[2]
print(name_list4)

#1.6移除最后的元素
name_list5=['张三','李四','王五','赵六']
name_list5.pop()
print(name_list5)

# 1.7移除制定的值的元素
name_list6=['张三','李四','王五','赵六']
name_list6.remove('张三')
print(name_list6)

# 1.8列表的遍历
name_list7=['张三','李四','王五','赵六']
for values in name_list7:
    print(values)

# 1.9遍历中结合if条件可以做对应处理