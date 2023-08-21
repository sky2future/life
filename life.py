import pygame

from common_code import play_audio, get_paragraph


class Life(object):
    def __init__(self) -> None:
        self.show_win()

    def get_win_size(self):
        # 获取屏幕信息
        screen_info = pygame.display.Info()
        # 获取屏幕大小
        screen_width = screen_info.current_w//3
        screen_height = screen_info.current_h//3
        return screen_width, screen_height
    
    @property
    def mergin(self):
        return 3

    @property
    def title(self):
        return 'life'
    
    @property
    def background(self):
        return (255, 255, 255)
    
    @property
    def font_text_color(self):
        return (0, 0, 0)
    
    @property
    def win_size(self):
        w, h = self.screen.get_size()
        return w,h
    
    @property
    def win_size_rm_mergin(self):
        return self.win_size[0]-self.mergin, \
                self.win_size[1]-self.mergin
    
    @property
    def text_size(self):
        return 20

    def show_win(self):
        # 初始化 pygame
        pygame.init()

        # 设置窗口大小
        window_size = self.get_win_size()
        self.screen = pygame.display.set_mode(window_size)

        # 设置窗口标题
        pygame.display.set_caption(self.title)

        self.welcom_str()

        # 游戏循环
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            self.screen_fill()
            
            # 更新显示
            pygame.display.flip()

        # 退出 pygame
        pygame.quit()

    def screen_fill(self):
         # 填充窗口背景颜色
        self.screen.fill(self.background)

        self.draw_welcom_str()

    def draw_welcom_str(self):
        # 在窗口上绘制文本
        # self.screen.blit(self.text_surface, self.text_rect)
        y = None
        text_surface_list = []
        if len(self.start_str_text_surface) == 2:
            return

        if len(self.start_str_text_surface) == 1:
            for index,line in enumerate(self.start_str):
                text_surface = self.font.render(line, True, self.font_text_color )
                text_rect = text_surface.get_rect()

                if not None:
                    y = len(self.start_str)*text_rect.height
                    y = (self.win_size[1] - y )//2 - text_rect.height//2

                text_rect.center = (self.win_size[0] // 2, y+index*(text_rect.height))
                text_surface_list.append(text_rect)
                self.screen.blit(text_surface, text_rect)
                y += self.font.get_linesize()
            self.start_str_text_surface.append(text_surface_list)

    def welcom_str(self):
        self.font = pygame.font.Font('data/font/SIMKAI.TTF', self.text_size)
        all_paragraph = get_paragraph()
        self.start_str = all_paragraph[0]
        self.start_str = self.split_text(self.start_str, self.font, self.win_size_rm_mergin[0])
        self.start_str_text_surface = [self.start_str]

    # 将字符串分割为多行
    @staticmethod
    def split_text(text, font, max_width)->list:
        words = text.split()
        lines = []
        current_line = words[0]
        
        for word in words[1:]:
            test_line = current_line + " " + word
            width, _ = font.size(test_line)
            if width <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        
        lines.append(current_line)
        return lines
            

    def welcom(self):
        welcom_voice_path = 'data/audio/out0.1.wav'
        play_audio(welcom_voice_path)

    def current_status(self):
        pass

if __name__ == '__main__':
    Life()