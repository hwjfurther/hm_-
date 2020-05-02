def measure():

    print("测量开始")
    temp = 20
    witness = 50
    print("测量结束")
    #元组可以包含多个数据，因此使用元组使返回值返回duogezhi
    #如果函数返回的使元组，小括号可以省略
    return temp,witness

# result = measure()
# print(result)

#需要单独处理温度和湿度
#如果函数返回的类型是元组，同时希望单独处理元组中的数据
#可以使用多个变量，一次接收函数的返回结果
#使用多个变量接受函数结果是，变量的个数应该和函数返回的元组中元组的个数一致


gl_temp,gl_witness = measure()
print(gl_temp)
print(gl_witness)