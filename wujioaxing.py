import turtle

# 设置画布和画笔
screen = turtle.Screen()
pen = turtle.Turtle()

# 设置画笔速度
pen.speed(2)

# 绘制五角星
for _ in range(5):
    pen.forward(100)  # 向前移动100个单位
    pen.right(144)   # 右转144度

# 关闭画布
screen.mainloop()