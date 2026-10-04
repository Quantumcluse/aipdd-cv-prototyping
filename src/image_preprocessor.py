import cv2
import numpy as np
from typing import Tuple

class ImagePreprocessor:
    """Module responsible for resizing, normalization, and color space conversion."""
    def __init__(self, target_size: Tuple[int, int] = (640, 640), normalize: bool = True):
        self.target_size = target_size
        self.normalize = normalize

    def preprocess(self, raw_frame: np.ndarray) -> np.ndarray:
        """Resizes and normalizes raw image tensor for model input."""
        resized = cv2.resize(raw_frame, self.target_size)
        rgb_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
        if self.normalize:
            return rgb_frame.astype(np.float32) / 255.0
        return rgb_frame
