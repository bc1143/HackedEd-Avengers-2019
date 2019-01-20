try:
	from PIL import Image
except ImportError:
	import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'/usr/local/Cellar/tesseract/4.0.0/bin/tesseract'

print(pytesseract.image_to_string(Image.open('test.png')))