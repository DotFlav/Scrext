import pytesseract
import pyautogui
from tools.getArea import get_area
from tools.getPath import get_resource_path

tesseract_path = get_resource_path('Tesseract-OCR/tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path
def read_text():
    x1, y1, x2, y2 = get_area()
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    screenshot = pyautogui.screenshot(region=(x1, y1, x2 - x1, y2 - y1))
    text = pytesseract.image_to_string(screenshot)
    return text


