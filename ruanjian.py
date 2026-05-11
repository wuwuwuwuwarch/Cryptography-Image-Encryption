import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib.table import Table

# 1. 设置中文字体（需根据系统路径调整）
font_path = "C:/Windows/Fonts/simhei.ttf"  # Windows系统黑体路径
font_prop = fm.FontProperties(fname=font_path, size=12)

# 2. 定义甘特图数据
tasks = [
    "需求分析", "系统设计", "前端开发", "后端开发",
    "数据分析", "测试与优化", "交付与总结"
]
time_columns = ["第1-3周", "第4-6周", "第7-9周", "第10-12周", "第13-15周", "第16周"]

# 每个任务的时间段填充状态（True表示填充）
gantt_data = [
    [True,  False, False, False, False, False],  # 需求分析
    [True,  False, False, False, False, False],  # 系统设计
    [False, True,  True,  False, False, False],  # 前端开发
    [False, True,  True,  True,  False, False],  # 后端开发
    [False, False, False, True,  True,  False],  # 数据分析
    [False, False, False, False, True,  True ],  # 测试与优化
    [False, False, False, False, False, True ]   # 交付与总结
]

# 3. 绘制表格
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis("off")
table = ax.table(
    cellText=[["" for _ in time_columns] for _ in tasks],
    rowLabels=tasks,
    colLabels=time_columns,
    cellLoc="center",
    loc="center",
    colWidths=[0.15]*len(time_columns),
    cellColours=[
        ["#4CAF50" if cell else "white" for cell in row]
        for row in gantt_data
    ]
)

# 4. 设置字体和样式
table.auto_set_font_size(False)
table.set_fontsize(12)
for key, cell in table.get_celld().items():
    cell.set_text_props(fontproperties=font_prop)
    cell.set_linewidth(0.5)
    cell.set_edgecolor("#333333")
    if key[0] == 0:  # 表头加粗
        cell.set_text_props(weight="bold")

# 5. 保存为图片
plt.savefig("gantt_chart.png", dpi=300, bbox_inches="tight")
plt.show()