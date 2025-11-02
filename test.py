import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties

# 创建示例数据集（替换为您的实际数据）
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.repeat(['A', 'B', 'C'], 30),
    'Subgroup': np.tile(['X', 'Y', 'Z'], 30),
    'Value': np.random.randn(90) * 10 + 50
})

# 创建分组箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(
    x='Category',
    y='Value',
    hue='Subgroup',  # 分组依据
    data=data,
    palette='Set3',  # 配色方案
    width=0.7,  # 箱体宽度
    fliersize=3  # 异常点尺寸
)

# 创建FontProperties对象，指定使用宋体
font = FontProperties(fname=r'C:\Windows\Fonts\simsun.ttc', size=12)

# 添加图表装饰
plt.title('分组箱线图示例', fontproperties=font)
plt.xlabel('主类别', fontproperties=font)
plt.ylabel('数值分布', fontproperties=font)
# 使用prop参数设置图例文本字体
plt.legend(title='子分组', loc='upper right', prop=font)
plt.grid(axis='y', linestyle='--', alpha=0.4)

# 显示图表
plt.tight_layout()
plt.savefig('grouped_boxplot.png', dpi=300)  # 保存图像
plt.show()