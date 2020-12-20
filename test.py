from PIL import Image

image = Image.open("advent_of_code.png")
image.thumbnail((100,100))

output_image = Image.new('RGB', (1000,1000))

index = 0
for i in range(0,1000,100):
    for j in range(0,1000,100):
        # im = Image.open(files[index])
        # im.thumbnail((300,300))
        output_image.paste(image, (i,j))
        index += 1

output_image.save("yolo.png")