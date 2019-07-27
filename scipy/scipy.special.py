"""
scipy的不同的模块,用于不同的功能.
scipy.cluster 矢量 K-均值
scipy.constants 物理和数学常数
scipy.fffpack 傅里叶变换
scipy.intergrate 积分程序
scipy.interpolate 插值
scipy,io 数据 输入输出
scipy.linalg 线性代数程序
scipy.ndimage n维图像包
scipy.odr 正交距离回归
scipy.optimize 优化
scipy.signal 信号处理
scipy.sparse 稀疏矩阵
scipy.spatial 空间数据结构
scipy.special 任何特殊数学函数
scipy.stats 统计

"""
#%% 读取外部文件 以及pandas的 dataframe 数据结构
# 查看数据类型
import pandas
food_info = pandas.read_csv("food_info.csv")
print("查看对象类型",type(food_info))
print("查看加载的数据类型中包含的数据类型",food_info.dtypes)
print(help(pandas.read_csv))  # 查看read_csv的帮助

#%%
# 查看数据的前n条 data.frame(n)
print(food_info.head(10))














