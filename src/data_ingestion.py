import cv2
import numpy as np
from typing import Generator, Optional, Tuple

class DataIngestion:
    """Module responsible for video stream ingestion from RTSP or local files."""
    def __init__(self, source_url: str, frame_width: int = 1920, frame_height: int = 1080):
        self.source_url = source_url
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.cap: Optional[cv2.VideoCapture] = None

    def connect_stream(self) -> bool:
        """Establishes stream connection."""
        self.cap = cv2.VideoCapture(self.source_url)
        return self.cap.isOpened()

    def read_frame(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Reads a single frame from the video stream."""
        if not self.cap or not self.cap.isOpened():
            return False, None
        return self.cap.read()

    def release(self) -> None:
        """Releases video capture handle."""
        if self.cap:
            self.cap.release()
