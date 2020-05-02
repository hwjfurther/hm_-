def test(num):
    print("在函数内部%d对应的地址为%d"%(num,id(num)))
    #定义一个字符串变量
    result = "hello"

    print("函数要返回数据的内存地址%d"%id(result))
    #将字符串变量返回，返回的是数据的引用，而不是数据本身

    return result

    #pass
#定义一个数字变量
a = 10
#数据的地址本质上就是一个数字
print("a变量保存数据的内存地址是%d"%id(a))
#调用test函数，本质上传递的实参是传递数据的引用，而不是数据本身
r = test(a)
#test(a)

print("%s的内存地址是%d"%(r,id(r)))