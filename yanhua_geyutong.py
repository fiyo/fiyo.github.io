##############################
#  名称：烟花汇演
#  作者：葛雨桐
#  班级：初一一班
#  学校：天山实验学校
##############################
import pygame
import random
import math

# 初始化 Pygame
pygame.init()

# 定义窗口大小
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# 设置窗口标题
pygame.display.set_caption("元宵节烟花汇演  初一一班葛雨桐")

# 定义颜色，烟花主体白色，窗口背景黑色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# 定义烟花类
class Firework:
    def __init__(self, x, y):
        # 烟花的x,y坐标
        self.x = x
        self.y = y
        # 烟花是否已爆炸
        self.exploded = False
        # 粒子数量
        self.particles = []
        # 随机选择颜色，每个烟花不同的颜色，定义红绿蓝三个颜色值每个烟花都在0到255之间随机变化
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def explode(self):
        # 烟花已爆炸
        self.exploded = True
        num_particles = 100  # 粒子数量
        for _ in range(num_particles):
            speed = random.uniform(2, 5)  # 粒子速度
            angle = random.uniform(math.pi / 4, 3 * math.pi / 4)  # 粒子角度范围
            # 粒子以随机速度和角度向外扩散
            self.particles.append([self.x, self.y, speed * math.cos(angle), -speed * math.sin(angle)])

    def update(self):
        if not self.exploded:
            # 烟花上升
            self.y -= 5
            if self.y <= 200:
                self.explode()  # 达到指定高度后爆炸
        else:
            for particle in self.particles:
                particle[0] += particle[2]  # 更新x坐标
                particle[1] += particle[3]  # 更新y坐标
                particle[3] += 0.1  # 添加重力，模拟抛物线运动

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, WHITE, (int(self.x), int(self.y)), 3)  # 绘制烟花主体
        else:
            for particle in self.particles:
                pygame.draw.circle(screen, self.color, (int(particle[0]), int(particle[1])), 2)  # 绘制烟花爆炸粒子

# 创建时钟对象 (可以控制游戏循环频率)
clock = pygame.time.Clock()

running = True
fireworks = []# 存储所有烟花实例的列表

while running:
    screen.fill(BLACK)  # 填充背景色，夜晚黑色的天空

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新和绘制所有烟花
    for firework in fireworks:
        firework.update()
        firework.draw()

    # 清除已经结束的烟花
    fireworks = [firework for firework in fireworks if not (firework.exploded and not firework.particles)]

    # 添加新的烟花
    if random.random() < 0.01:
        fireworks.append(Firework(random.randint(0, WIDTH), HEIGHT))

    pygame.display.flip()  # 刷新屏幕
    clock.tick(60)  # 通过时钟对象指定循环频率，每秒循环60次

pygame.quit()  # 退出
