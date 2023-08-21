from typing import List

from transformers import AutoProcessor
from transformers import BarkModel
import torch
import scipy

from text_deal import get_paragraph
from common_code import play_audio, get_paragraph

class TextToVoice(object):
    def __init__(self) -> None:
        self.init_param()

    def init_param(self):
        self.model = BarkModel.from_pretrained("suno/bark-small")
        self.processor = AutoProcessor.from_pretrained("suno/bark-small")
        
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)
        self.data = get_paragraph()

    def text_to_voice(self):
        for i,item in enumerate(self.data):
            for j,element in enumerate(item):
                inputs = self.processor(
                    text=[element],
                    return_tensors="pt",
                )
                # generate speech
                speech_output = self.model.generate(**inputs.to(self.device))
                sampling_rate = self.model.generation_config.sample_rate
                audio_file_path = f"data/audio/out{i}.{j}.wav"
                self.save_voice_file(audio_file_path, speech_output, sampling_rate)
                play_audio(audio_file_path)

    @staticmethod
    def save_voice_file(audio_file_path, speech_output, sampling_rate):
        scipy.io.wavfile.write(audio_file_path, rate=sampling_rate, data=speech_output[0].cpu().numpy())

 

if __name__ == '__main__':
    text = TextToVoice()
    text.text_to_voice()



