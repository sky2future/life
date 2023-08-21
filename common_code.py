import time
from typing import List

import pygame

from var_type import PATH_LIKE
from text_deal import get_paragraph

def play_audio(audio_file_path:PATH_LIKE):
    # audio_file_path = os.path.abspath(audio_file_path)
    # 播放音频
    # playsound(audio_file_path)
    import pygame

    # 初始化 pygame
    pygame.init()

    # 加载音频文件
    audio_file = audio_file_path # 替换为实际的音频文件路径
    pygame.mixer.music.load(audio_file)

    # 播放音频
    pygame.mixer.music.play()

    # 等待音频播放完成
    while pygame.mixer.music.get_busy():
        time.sleep(0.5)

    # 退出 pygame
    pygame.quit()

def load_data(language:int=2)->List[List[str]]:
    data_path ='data/text/charactor.txt'
    paragraph = get_paragraph(data_path)
    paragraph = [[paragraph[index], paragraph[index+1]] for index in range(0, len(paragraph)-len(paragraph)%language, language)]
    return paragraph