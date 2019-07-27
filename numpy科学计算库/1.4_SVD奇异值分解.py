import numpy as np
import os
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib as mpl
from pprint import pprint

def restore(sigma, u, v, K):  # 奇异值、左特征向量、右特征向量 第k个奇异值
    m = u.shape[0]
    n = v.shape[0]
    a = np.zeros((m, n))

    for k in range(K):
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
        # np.dot，向量是点乘，矩阵是矩阵乘法，下面是矩阵乘法
        # K越大，叠加的分解结果越多
        a += sigma[k] * np.dot(uk, vk)

    # clip这个函数将将数组中的元素限制在a_min, a_max之间，
    # 大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min
    a = a.clip(0, 255)
    # np.rint(a)计算数组各元素的四舍五入值
    return np.rint(a).astype('uint8')


if __name__ == "__main__":
    print(os.getcwd())

    A = Image.open("./lena.jpg", 'r')  # 打开图片
    print(A)

    output_path = './lena_output'    # 图片路径
    if not os.path.exists(output_path): # 路径不存在的时候
        os.mkdir(output_path)   # 创建路径

    a = np.array(A)  # 加载图片为数组
    # (512,512,3)
    print(a.shape)   # 输出数组

    # (512, 512) (512,) (512, 512)
    # 注意下面分解出的v，直接对应公式中v的转置矩阵
    u_r, sigma_r, v_r = np.linalg.svd(a[:, :, 0])   # 开始分解，使用np中的线性代数包的svd方法分解 有红绿蓝通道
    u_g, sigma_g, v_g = np.linalg.svd(a[:, :, 1])  # 不同的格式的图像的svd分解参数不一样，颜色通道不同
    u_b, sigma_b, v_b = np.linalg.svd(a[:, :, 2])
    print(u_r.shape, sigma_r.shape, v_r.shape)  #  分别对应U左奇异向量 D奇异值 V又奇异向量

    # facecolor 设置背景色，w表示白色，其他颜色值表示可以网上查到
    # figsize 以dpi为单位的设置显示图像大小，一般8左右比较合适，可以根据需要设置变小 dpi1英寸包含的像素个数
    plt.figure(figsize=(8, 8), facecolor='w')

    # matploblib 解决中文显示的问题  画图显示
    mpl.rcParams['font.sans-serif'] = ['simHei']
    mpl.rcParams['axes.unicode_minus'] = False

    # 分别获取1到num个奇异值恢复图像
    num = 20
    for k in range(1, num+1):
        print(k)
        R = restore(sigma_r, u_r, v_r, k)
        G = restore(sigma_g, u_g, v_g, k)
        B = restore(sigma_b, u_b, v_b, k)
        
        # (512, 512)
        print(R.shape)
        # 增加了一个维度，这个维度上的索引0，1，2分别存放R，G，B
        # axis从0开始索引，2表示第三个维度
        I = np.stack((R, G, B), axis=2) # 将图像的数据重新叠加
        # (512,512,3)
        print(I.shape)

        # 将array保存为三通道彩色图像
        Image.fromarray(I).save('%s/svd_%d.png' % (output_path, k))

        # 按照三行四列显示前12图像
        if k <= 12:
            plt.subplot(3, 4, k)
            plt.imshow(I)
            plt.axis('off')
            plt.title('奇异值个数：%d' % k)

    plt.suptitle('SVD与图像分解', fontsize=20)
    plt.tight_layout(0.3, rect=(0, 0, 1, 0.92))
    plt.show()
