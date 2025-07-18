from text_detection import TextDetector, TextAnalysisResult
from pydantic import BaseModel, Field
from typing import Optional

class FileInput(BaseModel):
    content: str = Field(..., description="Text content of the uploaded file")

class Backend:
    def __init__(self):
        self.detector = TextDetector()

    def process_text(self, text: str) -> TextAnalysisResult:
        return self.detector.detect_text(text)

    def process_file(self, file) -> TextAnalysisResult:
        try:
            text = file.read().decode("utf-8")
            file_input = FileInput(content=text)
            return self.process_text(file_input.content)
        except Exception as e:
            return TextAnalysisResult(is_ai_generated=False, confidence=0.0, error=f"Error reading file: {str(e)}")