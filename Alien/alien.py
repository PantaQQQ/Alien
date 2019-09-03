import pyganme
from pygame.sprite import Sprite

class Alien(sprite):
    """表示单个外星人的类"""
    def _init_(self,ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self)._init_()
        self.screen = screen
        self.ai_settings = ai_settings

        #加载外星人图像，并设置其rect属性
        self.image = pygame.image.load('images/aline.bmp')
        self.rect = self.image.get_rect()

        #每个外星人最初都在屏幕左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储外星人准确位置
        self.x = float(self.rect.x)

    def blitme(self):
        """指定外星人在什么位置"""
        self.screen.blit(self.image, self.rect)



