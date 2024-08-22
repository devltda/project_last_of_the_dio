import pytesseract
from PIL import Image
import os

input_dir = 'inputs/'
output_dir = 'output/'

for filename in os.listdir(input_dir):
    if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(input_dir, filename)
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        output_file = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(output_dir, output_file)
        with open(output_path, 'w') as f:
            f.write(text)

print("Reconhecimento de texto concluído. Os resultados estão na pasta 'output'.")
