# 格式1.
if(True):
    print('1')

# 格式2.
if(True):
    print('1')
elif False:
    print('2')

# 格式3.
if(True):
    print('1')
elif False:
    print('2')
else:
    print('3')

# 格式4.
if(True):
    print('1')
elif False:
    print('2')

# 格式5.
if(True):
    print('1')
    if False:
        print('1.1')
    else:
        print('1.2')
elif False:
    print('2')