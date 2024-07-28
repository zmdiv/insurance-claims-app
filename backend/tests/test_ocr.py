import unittest
from mockito import when, verify, unstub
from app.services.ocr_service import OCRService

class TestOCRService(unittest.TestCase):
    def setUp(self):
        self.ocr_service = OCRService()
        self.image_content = b"dummy image content"

    def test_process_image(self):
        when(self.ocr_service).process_image(self.image_content).thenReturn("Extracted text")

        result = self.ocr_service.process_image(self.image_content)

        verify(self.ocr_service).process_image(self.image_content)
        self.assertEqual(result, "Extracted text")

    def tearDown(self):
        unstub()

if __name__ == "__main__":
    unittest.main()
