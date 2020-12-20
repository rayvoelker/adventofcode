# print dem trees!
from PIL import Image, ImageDraw

# this is our "place holder" image
image = Image.open("advent_of_code.png")
image.thumbnail((100,100))

# with open("2020-12-19_test_input.txt") as input:
with open("2020-12-19_input.txt") as input:
    # get the first line ... the tile id of the first tile
    # tile_id = input.readline()
    tiles = {}
    line = input.readline()
    while line:
        line = line.strip("\n")
        if line.strip("\n").split(" ")[0] == "Tile":
            tile_id = int(line.strip("\n").split(" ")[1].strip(":"))
            tiles[tile_id] = []

        else:
            if line != "":
                tiles[tile_id].append(line)

        line = input.readline()

class Tile:
    def __init__(self, tile_id, input_tile):
        self.tile_id = tile_id
        self.up = input_tile[0]
        self.down = input_tile[-1]
        self.left = [value[0] for value in input_tile]
        self.right = [value[-1] for value in input_tile]
        self.tile = input_tile

    def gen_image(self):
        output_image = Image.new('RGBA', (1000,1000))
        # place a watermark for the tile id in a blank spot
        watermark = True
        for i in range(0,1000,100):
            for j in range(0,1000,100):
                if self.tile[int(j/100)][int(i/100)] == "#":
                    output_image.paste(image, (i,j))
                elif watermark:
                    watermark_img = Image.new("RGBA", (100, 100))
                    d = ImageDraw.Draw(watermark_img)
                    d.text((10,10), f"tile id: {self.tile_id}", fill=(0,0,0))
                    output_image.paste(watermark_img, (i,j))
                    watermark = False

            output_image.save(f"./output/{self.tile_id}.png")


tiles_data = {}
for tile in tiles:
    t = Tile(tile, tiles[tile])
    tiles_data[tile] = t
    
tiles_data[1171].gen_image()

for tile in tiles_data:
    tiles_data[tile].gen_image()


