import pygame
import sys
import random


# 初始化pygame
pygame.init()

# 设置游戏窗口大小
window_width = 800
window_height = 600
cell_size = 20 #单元格大小

# 创建游戏窗口
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇游戏')

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

#设置字体和大小
font_style = pygame.font.SysFont(None, 30) 

clock = pygame.time.Clock()

'''
# 定义贪吃蛇和食物
snake = [(200, 200)]
snake_direction = 'RIGHT'
food = (random.randint(0, window_width//cell_size-1)*cell_size, 
        random.randint(0, window_height//cell_size-1)*cell_size)

# 创建得分变量
score = 0
'''

# 显示分数
def display_score(score):
    value = font_style.render(f"score: {score}", True, white)
    window.blit(value, [700, 10])

# 显示游戏结束信息
def display_message(msg, color):
    mesg = font_style.render(msg, True, color)
    window.blit(mesg, [window_width/3, window_height/3])
    #重新开始
    reset_mesg = font_style.render("Press R to Restart or Q to Quit", True, color)
    window.blit(reset_mesg, [window_width/3, window_height/2])

# 游戏重新开始函数
def reset():
    global snake, snake_direction, food, score
    snake = [(200, 200)]
    snake_direction = 'RIGHT'
    food = (random.randint(0, window_width//cell_size-1)*cell_size, 
            random.randint(0, window_height//cell_size-1)*cell_size)
    score = 0

reset()

# 游戏主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != 'DOWN':
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN and snake_direction != 'UP':
                snake_direction = 'DOWN'
            elif event.key == pygame.K_LEFT and snake_direction != 'RIGHT':
                snake_direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and snake_direction != 'LEFT':
                snake_direction = 'RIGHT'
            elif event.key == pygame.K_r:  # 按R重新开始
                reset()
            elif event.key == pygame.K_q:  # 按Q退出
                pygame.quit()
                sys.exit()

    # 移动贪吃蛇
    head = snake[0]
    x, y = head
    if snake_direction == 'UP':
        new_head = (x, y - cell_size)
    elif snake_direction == 'DOWN':
        new_head = (x, y + cell_size)
    elif snake_direction == 'LEFT':
        new_head = (x - cell_size, y)
    elif snake_direction == 'RIGHT':
        new_head = (x + cell_size, y)


    snake.insert(0, new_head)  # 将新的头部添加到贪吃蛇；append是末尾添加

    # 检查是否吃到食物
    if new_head == food:
        food = (random.randint(0, window_width//cell_size-1)*cell_size, 
                random.randint(0, window_height//cell_size-1)*cell_size) #更新食物位置
        score += 10  # 增加得分
    else:
        snake.pop() #如果没有吃到，删除蛇最后一个位置，保持长度
        #pass

    # 检测是否撞墙
    if new_head[0] < 0 or new_head[0] >= 800 or new_head[1] < 0 or new_head[1] >= 600:
        window.fill(black)
        display_message("GAME OVER", white)
        pygame.display.update()
        pygame.time.delay(2000)
        continue

    # 渲染背景
    window.fill(black)

    display_score(score)

    # 绘制贪吃蛇
    for segment in snake:
        pygame.draw.rect(window, green, (segment[0], segment[1], cell_size, cell_size))
    
    # 绘制食物；surface,color,矩形位置与尺寸,线条宽度width = 0
    pygame.draw.rect(window, red, (food[0], food[1], cell_size, cell_size))

    # 更新窗口
    pygame.display.update()

    clock.tick(10)  # 控制帧率
