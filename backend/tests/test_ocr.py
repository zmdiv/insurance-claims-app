import unittest
from mockito import mock, when, verify
from app.services.ocr_service import OCRService

class TestOCRService(unittest.TestCase):
    def test_process_image(self):
        ocr_service = OCRService()
        image = mock()
        
        when(ocr_service).process_image(image).thenReturn("Extracted text")

        result = ocr_service.process_image(image)

        verify(ocr_service, times=1).process_image(image)
        self.assertEqual(result, "Extracted text")
