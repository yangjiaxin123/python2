import numpy as np
import matplotlib.pyplot as plt

# 定义 x 的取值范围
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

# 计算 y 的值
y = np.sin(x)

# 创建图像
plt.figure(figsize=(8, 6))

# 绘制正弦函数曲线
plt.plot(x, y, label='y = sin(x)')

# 添加标题和标签
plt.title('Sine Function')
plt.xlabel('x')
plt.ylabel('y')

# 添加网格
plt.grid(True)

# 添加图例
plt.legend()

# 显示图像
plt.show()