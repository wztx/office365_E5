# 屏幕创建和初始化参数 
self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
self.rect = self.screen.get_rect()
pygame.display.set_caption(TITLE)
# 加载关卡图片
self.background = load_image('level.png')
self.back_rect = self.background.get_rect()
    # 这里载入图片需要乘上特定的系数来适配屏幕的尺寸
self.background = pygame.transform.scale(self.background,
                                     (int(self.back_rect.width * BACKGROUND_SIZE),
                                      int(self.back_rect.height * BACKGROUND_SIZE))).convert()
# 导入Mario
self.sheet = load_image('mario.png')
    # 这里由于Mario会有奔跑和跳跃的速度，所以需要导入一整张图片再裁剪使用。
self.load_from_sheet()
    # 初始化角色的一些基本常量
self.rect = self.image.get_rect()
self.pos = vec(WIDTH * 0.5, GROUND_HEIGHT - 70)
self.vel = vec(0, 0)
self.acc = vec(0, 0)
self.acc = vec(0, GRAVITY)
if GROUND_HEIGHT < self.mario.pos.y:
    # 如果Mario低于我们定义的地面，就之间将他的所有速度加速度都置零，之间放在我们的地面上
    # 如果速度和加速度不值零，可能会出现Mario卡在地面上抖动的情况，由于y值的不断变化
    self.mario.acc.y = 0
    self.mario.vel.y = 0
    self.mario.pos.y = self.ground_collide.rect.top
 self.mario.landing = True
 keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # 向右
        self.pos.x += 5 # ------------------------简单的改变位置
    elif keys[pygame.K_LEFT]:
        # 向左
       if self.vel.x < 0:
            # 这里很细节的加入了一个转向的速度控制
            self.acc.x = -TURNAROUND
            if self.vel.x >= 0:  # ------------------------改变加速度来改变运动
                self.acc.x = -ACC
        # 这里加入了一个最大速度限制
    if abs(self.vel.x) < MAX_SPEED:
        self.vel.x += self.acc.x
    elif keys[pygame.K_LEFT]:
        self.vel.x = -MAX_SPEED
    elif keys[pygame.K_RIGHT]:
        self.vel.x = MAX_SPEED
    # 这里对加速度和速度进行计算得出位移并在下一帧时改变Mario的位置
    self.acc.x += self.vel.x * FRICTION
    # 同时还要引用一个 摩擦力 的概念，随着速度的增大而增大
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
    self.rect.midbottom = self.pos
    if keys[pygame.K_SPACE]:
    if self.landing:
        # 这里跳跃的参数，只是给Mario一个向上的速度，类似于物理中的上抛运动
        self.vel.y = -JUMP
        def load_image(filename):
    src = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(src, 'resources', 'graphics', filename)
    return pygame.image.load(path)
    # 裁切方法
def get_image(self, x, y, width, height):
    image = pg.Surface([width, height])
    rect = image.get_rect()
    image.blit(self.sheet, (0, 0), (x, y, width, height))
    image.set_colorkey(BLACK)
    image = pg.transform.scale(image,
                               (int(rect.width * MARIO_SIZE),
                                int(rect.height * MARIO_SIZE)))
    return image
​
# 裁切并加入容器
def load_from_sheet(self):
    self.right_frames = []
    self.left_frames = []
​
    self.right_frames.append(
        self.get_image(178, 32, 12, 16)) # 站立
    self.right_frames.append(
        self.get_image(80, 32, 15, 16))  # 跑 1
    self.right_frames.append(
        self.get_image(96, 32, 16, 16))  # 跑 2
    self.right_frames.append(
        self.get_image(112, 32, 16, 16))  # 跑 3
    self.right_frames.append(
        self.get_image(144, 32, 16, 16))  # 跳 
​
    # 将向右的图片水平翻转就是向左的图片了
    for frame in self.right_frames:
        new_image = pg.transform.flip(frame, True, False)
        self.left_frames.append(new_image)
​
    # 最后全部加入容器方便我们之间通过下标
    self.frames = self.right_frames + self.left_frames
    # 定义一个方法来通过运动方向更换图片
def walk(self, facing):
    if facing == 'right':
        if self.image_index > 3:
            self.image_index = 0
     if facing == 'left':
        if self.image_index > 8:
            self.image_index = 5
        if self.image_index < 5:
            self.image_index = 5
      self.image_index += 1
          # 改进后的代码
    def walk(self, facing):
        if self.image_index == 0:
            self.image_index += 1
            # 加入一个时间戳
            self.walking_timer = pg.time.get_ticks()
        else:
            # 比较时间变化和当前的Mario的速度
            if (pg.time.get_ticks() - self.walking_timer >
                    self.calculate_animation_speed()):
                self.image_index += 1
                self.walking_timer = pg.time.get_ticks()
        if facing == 'right':
            if self.image_index > 3:
                self.image_index = 0
        if facing == 'left':
            if self.image_index > 8:
                self.image_index = 5
            if self.image_index < 5:
                self.image_index = 5
    
    # 计算速度的方法
    def calculate_animation_speed(self):
        if self.vel.x == 0:
            animation_speed = 130
        elif self.vel.x > 0:
            animation_speed = 130 - (self.vel.x * 12)
        else:
            animation_speed = 130 - (self.vel.x * 12 * -1)
            # 先定义好 镜头的位置移动规则 即self.viewpoint
if self.level.mario.pos.x < self.viewpoint.x + 15:
    self.level.mario.pos.x -= self.level.mario.vel.x
if self.level.mario.vel.x > 0:
    if self.level.mario.pos.x > WIDTH * 0.55 + self.viewpoint.x:
        # 1.1 这个系数是为了屏幕的顺滑后期加上去的
        self.viewpoint.x += int(self.level.mario.vel.x * 1.1)
# self.viewpoint是一个根据Mario的移动而改变参数的矩形
self.screen.blit(self.background, (0, 0), self.viewpoint)
self.all_group.draw(self.screen)
 def draw(self):
        pg.display.flip()
        # 每次都将背景拷贝一份，并且每一次都绘制在新的背景上，那么之前的就会被覆盖
        self.background_clean = self.background.copy()
        self.all_group.draw(self.background_clean)
        self.screen.blit(self.background, (0, 0), self.viewpoint)
        self.all_group.draw(self.screen)
        class Collider(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
            def set_ground(self):
        ground_rect1 = Collider(0, GROUND_HEIGHT, 2953, 60)
			# 其余的省略
        self.ground_group = pg.sprite.Group(ground_rect1,
                                            ground_rect2,
                                            ground_rect3,
                                            ground_rect4)

    def set_pipes(self):
        pipe1 = Collider(1202, 452, 83, 80)
        # 其余的省略
        self.pipe_group = pg.sprite.Group(pipe1, pipe2,
                                          pipe3, pipe4,
                                          pipe5, pipe6)

    def set_steps(self):
        step1 = Collider(5745, 495, 40, 44)
        # 其余的省略
        self.step_group = pg.sprite.Group(step1, step2,
                                          step3, step4,
                                          step5, step6,
                                          step7, step8,
                                          step9, step10,
                                          step11, step12,
                                          step13, step14,
                                          step15, step16,
                                          step17, step18,
                                          step19, step20,
                                          step21, step22,
                                          step23, step24,
                                          step25, step26,
                                          step27)
        def check_collide(self):
        self.ground_collide = pg.sprite.spritecollideany(self.mario, self.ground_group)
        self.pipe_collide = pg.sprite.spritecollideany(self.mario, self.pipe_group)
        self.step_collide = pg.sprite.spritecollideany(self.mario, self.step_group)
