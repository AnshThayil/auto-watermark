#Import Modules
from PIL import Image
import os

#Function to create watermarked pictures
def watermark(input_image_path, output_image_path, watermark_image_path, position):

    base_image = Image.open(input_image_path)
    watermark = Image.open(watermark_image_path)
    width, height = base_image.size

    output = Image.new('RGBA', (width, height), (0,0,0,0))
    output.paste(base_image, (0,0))
    output.paste(watermark, position, mask=watermark)
    out = output.convert('RGB')
    out.save(output_image_path)

#Main Function
if __name__ == '__main__':

    #Loop to iterate through images in folder
    count = 1
    directory = os.fsencode("input")
    for file in os.listdir(directory):

        #Calling function for each picture in folder
        filename = os.fsdecode(file)
        print(filename)
        f = "input/" + filename
        out = "output/" + filename
        watermark(f, out, "logos/[[YOUR LOGO FILE NAME HERE]]", (0,0))
        print(str(count) + ": " + filename +" watermarked!")
        count += 1
