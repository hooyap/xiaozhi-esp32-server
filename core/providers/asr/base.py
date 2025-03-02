import time
import wave
import os
from abc import ABC, abstractmethod
import logging
from typing import Optional, Tuple, List
import uuid

import opuslib

logger = logging.getLogger(__name__)


class ASRProviderBase(ABC):
    @abstractmethod
    def save_audio_to_file(self, opus_data: List[bytes], session_id: str) -> str:
        """解码Opus数据并保存为WAV文件"""
        pass

    @abstractmethod
    async def speech_to_text(self, opus_data: List[bytes], session_id: str) -> Tuple[Optional[str], Optional[str]]:
        """将语音数据转换为文本"""
        pass
