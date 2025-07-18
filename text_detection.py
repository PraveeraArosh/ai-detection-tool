import os
from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

class TextAnalysisResult(BaseModel):
    is_ai_generated: bool = Field(..., description="Indicates if the text is AI-generated")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Confidence score of the analysis")
    error: Optional[str] = Field(None, description="Error message if analysis fails")

class TextDetector:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in .env file")
        self.client = OpenAI(api_key=self.api_key)

    def detect_text(self, text: str) -> TextAnalysisResult:
        try:
            if not isinstance(text, str) or not text.strip():
                return TextAnalysisResult(is_ai_generated=False, confidence=0.0, error="Invalid or empty text input")
            
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "Analyze the input text and determine if it is AI-generated or human-written. Return a JSON-like response with 'is_ai_generated' (boolean) and 'confidence' (float between 0 and 1)."},
                    {"role": "user", "content": text}
                ],
                temperature=0.0
            )
            result = response.choices[0].message.content
            # Simulate parsing a JSON-like response
            is_ai = "true" in result.lower()
            confidence = 0.95 if is_ai else 0.05
            return TextAnalysisResult(is_ai_generated=is_ai, confidence=confidence)
        except Exception as e:
            return TextAnalysisResult(is_ai_generated=False, confidence=0.0, error=f"Error analyzing text: {str(e)}")