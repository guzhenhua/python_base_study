# 1.遍历字符串
for i in 'abcd':
    print(i)

# 2.遍历列表
name_list=['张三','李四','王五']
for name in name_list:
    print(name)


# 练习1. 1+2+3+...+100和
sum=0
for i in  range(101):
    sum+=i
print(sum)

# 练习2. 列表排序
list_sort=[1,3,2,5,6,12,11,66,44]
def array_sort(arr):
    max=len(arr)
    for i in range(max):
        for j in range(max-i-1):
            if list_sort[j]>list_sort[j+1]:
                list_sort[j],list_sort[j+1]=list_sort[j+1],list_sort[j]
array_sort(list_sort)
print(list_sort)
