import pytesseract
from PIL import Image
from io import BytesIO

class OCRService:
    def process_image(self, image_bytes):
        image = Image.open(BytesIO(image_bytes))
        text = pytesseract.image_to_string(image)
        return text
