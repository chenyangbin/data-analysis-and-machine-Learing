#%% 导入文件
"""
np.genfromtxt(路径, 分隔符, 数据类型)
"""
import numpy as np
world_alcohol = np.genfromtxt("world_alcohol.txt", delimiter=",", dtype=str)
print(world_alcohol)
print(type(world_alcohol))  # 查看导入的数据类型
print(world_alcohol.dtype)
print(help(np.genfromtxt)) # 查看该函数的帮助

#%%  numpy数组
"""
np.array() #  构建数组数据结构  不限维度
"""
vector1 = np.array([1,2,3,4])  # 一维数组
vector2  = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 二维数组
vector3 = np.array([[[1,2,3],[4,5,6]]])   # 三维数组
print(vector1)
print(vector1.ndim)  # 查看维数
print(vector2)
print(vector2.ndim)
print(vector3)
print(vector3.ndim)

#%% 查看数组的结构,几行几列
"""
.shape
"""
vector4  = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(vector4.shape) # 查看数组的结构 方便理解数据的的结构

#%% np.array中的数据必须为同一类
# 如果允许不同类型则要定义新的np.array的数据结构 参数 dtype= project
print(world_alcohol)
print(world_alcohol[2,4]) # 按照索引查找指定的元素
print(world_alcohol[:,1])  # 取出每一行的第二个元素
print("每列的第一个元素",world_alcohol[1,:])  # 取出每一列的第一个元素 即第2条记录
print("每列的第一个元素",world_alcohol[:,0:2])  # 取出所有行的第一例和第二列元素

#%% numpy中的计算

# 逻辑判断 查找元素或者记录或者元素
# 判断数组中的某个值是否为某个具体值
world_alcohol2 = np.array([[1,2,3],[1,4,3]])
#print(world_alcohol2)
#print(world_alcohol2 == 3)  # 返回布尔判断

# 以布尔判断为索引取出相应的元素值
equl_to_two = world_alcohol2 == 2
equl_to_2 = (world_alcohol2[:,1] == 2) # 找出属性1(第2列)为2的布尔
print(equl_to_2)
print(world_alcohol2[equl_to_2,:])  # 找出所有记录中的属性1 即第2列为2的记录

#%%  修改数组的数据类型 dtype= "数据类型"  .astype(数据类型)修改数据类型
vector5 = np.array([1,2,3,4,], dtype="int")
print(vector4.dtype)
vector6 = np.array([1,2,3,4,5],dtype="float")
print(vector6.dtype)
vector7 = vector6.astype(str)
print(vector7.dtype)
print(vector7)

#%% 对数据求极值 .min
print(vector6.min())  # 求极值

#%% 求和 对某行某个记录或者某列求和, 指定维度 .sum(axis=1)行求和  .sum(axis=0)列求和
vector8 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("返回行和矩阵", vector8.sum(axis=1))
print("返回列和矩阵", vector8.sum(axis=0))

#%% 矩阵变换 .reshape(行数, 列数) 对矩阵进行参数化的reshape
vector9 = np.arange(10,20)  # 生成指定范围的行向量
print(vector9)
print(vector9.ndim)
print(vector9.reshape(2,5))
print(vector9.reshape(2,5).ndim)  # 矩阵的维度为2

#%% 查看矩阵信息
# vector.size 查看元素个数
# vector.dtype 查看矩阵的元素类型

#%% 生成特殊矩阵
# np.zeros([行,列], dtypr="元素类型") # 生成指定类型的行列的0矩阵
# np.ones([行,列], dtype="元素类型")  # 生成指定的全1的矩阵
# np.arange(起始值, 结束值, 步长)     # 生成指定步长比那花的一维数组

# 权重初始化的时候生成random矩阵
# np.random,rand(行, 列) # 生成-1 - +1 范围的指定行列的矩阵
vector10 = np.random.rand(2,3)  # random模块中的rand方法的使用生成随机值 默认-1至+1范围
print(vector10)

# np.linspace(起始值, 终点值, 值个数) # 生成指定个数的线性空间
print(np.linspace(1, 20, 100))

#%% 矩阵乘法
# 乘法 矩阵的元素对应相乘 得到矩阵 方阵相乘
# 内积 np.dot(vector1, vector2) 得到新的矩阵源矩阵的行,列

vector11 = np.arange(6).reshape(2,3)
vector12 = np.arange(6).reshape(3,2)
print(vector11)
print(vector12)
print("内积",np.dot(vector11,vector12))

#%% 矩阵相关操作
# 倍化随机矩阵 random的范围是-1 - +1 使用倍乘是元素增加
vector13 = 10* np.floor(10* np.random.rand(2 ,3)) # floor 向下取整
print(vector13)

# 矩阵转换为一维向量  .ravel()
print(vector13.ravel())  # 矩阵转换为一维向量(拉平)
# 矩阵reshape   (n, -1)  当第二个参数为-1 的时候, 自动根据第一个参数自动计算(大矩阵使用)
print(vector13.ravel().reshape(3,2)) # 拉平后在重新shape
print(vector13.ravel().reshape(3, -1)) # 拉平后在重新shape 自动计算

 #%%  矩阵的属性添加, 记录添加
# 对矩阵中的记录的属性的添加 即矩阵的横向扩展 np.hstack(v1, v2)
vector15 = np.array([[1,2,3],[4,5,6]])
vector16 = np.array([[7,8,9],[1,4,7]])

# 记录中的属性的叠加 横向叠加 np.hstack((v1, v2))
print(np.hstack((vector15, vector16)))

# 矩阵记录叠加增加样本 np.vstack((v1, v2))
print(np.vstack((vector15, vector16)))

#%% 矩阵属性的切分
# 矩阵属性值均匀切分 np.hsplit(v1, 切的份数) 例如 2x12 切成 2x4 的3份
vector17 = np.floor(10* np.random.rand(2, 12))
print("2行12矩阵\n", vector17)
print("属性切分\n", np.hsplit(vector17, 3))

# 矩阵的属性的指定位置的切分 np.hsplit(v, (列1后切, 列2后切...)
print("属性指定位置切分", np.hsplit(vector17, (3, 4, 5)))

#%% 矩阵记录的切分
# 按照行进行均匀切分 np.vsplit(v, 行均切份数)
vector18 = np.floor(10* np.random.rand(12, 2))
print(vector18)
print(np.vsplit(vector18, 3)) # 12行记录, 切成每个矩阵3个记录

# 按照行进行定制切分 np.vsplit(v, (行1, 行2...))
print("指定行切\n",np.vsplit(vector18, (2, 3, 6))) # 从1开始数

#%% 矩阵的复制
#   = 深复制, 引用复制, 复制以后绑定的在内存中同一个地址,
#  只是名字不一样, a变, b也变
vector19 = np.arange(12).reshape(3,4)
copy_vector19 = vector19
print(copy_vector19 is vector19)  # 使用 = 进行复制 二者同样只是名字不一样

# 浅复制 v.view()
copy_light_vector19 = vector19.view()
print(copy_light_vector19 is vector19) # 浅复制后的矩阵并不是原矩阵
copy_light_vector19.shape = 2,6  # 对浅复制进行reshape
print(copy_light_vector19.shape, vector19.shape)  # 可以看出shape改变互不影响
# 浅复制,虽然变量名所指的位置不一样,但是实际上,浅复制仍然共用矩阵中的值
# 即,改变a矩阵中的值, 浅复制的矩阵的值也会改变

#%% 复制两个内容一样但是互不影响的矩阵 v.copy() 用法同上

#%% 矩阵的索引排序

# 最大值的索引(位置)
