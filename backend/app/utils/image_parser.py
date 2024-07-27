from PIL import Image

class ImageParser:
    def parse_image(self, image_bytes):
        image = Image.open(image_bytes)
        return image
