
from time import sleep
import requests
from instabot import Bot
from PIL import Image
from io import BytesIO

class InstaBot:
    def post(self, image):
        bot = Bot()
        bot.login(username="nash.exe_beta", password="Yarayara-1290",use_cookie=False)
        print("this ran")
        sleep(2)

        bot.upload_photo(image, caption="test2")
        print("wroked")
        bot.mainloop()
    
    def resize_and_crop_image(self, image):
        # Check if the image is a URL
        if isinstance(image, str) and image.startswith("http"):
            response = requests.get(image)
            image = Image.open(BytesIO(response.content))
        else:
            image = Image.open(image)

        # Calculate the current aspect ratio
        current_ratio = image.width / image.height

        # Calculate the target width and height for 4:5 aspect ratio
        target_ratio = 4 / 5
        if current_ratio > target_ratio:
            # Image is wider, calculate height
            target_width = image.height * target_ratio
            target_height = image.height
        else:
            # Image is taller, calculate width
            target_width = image.width
            target_height = image.width / target_ratio

        # Resize the image while maintaining the aspect ratio
        resized_image = image.resize((int(target_width), int(target_height)), Image.ANTIALIAS)

        # Calculate the cropping box to achieve the 4:5 aspect ratio
        left = (resized_image.width - target_width) / 2
        top = (resized_image.height - target_height) / 2
        right = (resized_image.width + target_width) / 2
        bottom = (resized_image.height + target_height) / 2

        # Crop the image
        cropped_image = resized_image.crop((left, top, right, bottom))
        return cropped_image
        
