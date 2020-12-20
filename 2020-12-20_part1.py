from collections import deque
# print dem trees!
from PIL import Image, ImageDraw

# this is our "place holder" image
image = Image.open("advent_of_code.png")
image.thumbnail((100,100))

# with open("2020-12-20_test_input.txt") as input:
with open("2020-12-20_input.txt") as input:
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
        self.up = list(input_tile[0])
        self.up_mirror = self.up.copy()
        self.up_mirror.reverse()
        self.up_match = []

        self.down = list(input_tile[-1])
        self.down_mirror = self.down.copy()
        self.down_mirror.reverse()
        self.down_match = []

        self.left = list([value[0] for value in input_tile])
        self.left_mirror = self.left.copy()
        self.left_mirror.reverse()
        self.left_match = []

        self.right = list([value[-1] for value in input_tile])
        self.right_mirror = self.right.copy()
        self.right_mirror.reverse()
        self.right_match = []

        self.tile = input_tile

        self.match = []


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
    
# for tile in tiles_data:
#     tiles_data[tile].gen_image()


# compare each tile to the other tiles looking for matches 
for tile in tiles_data:
    for tile_compare in tiles_data:
        # don't compare the tile to itself
        if tile_compare != tile:
            compare_list = [
                tiles_data[tile].up == tiles_data[tile_compare].up,
                tiles_data[tile].up == tiles_data[tile_compare].down,
                tiles_data[tile].up == tiles_data[tile_compare].left,
                tiles_data[tile].up == tiles_data[tile_compare].right,
                tiles_data[tile].up == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].up == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].up == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].up == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].down == tiles_data[tile_compare].up,
                tiles_data[tile].down == tiles_data[tile_compare].down,
                tiles_data[tile].down == tiles_data[tile_compare].left,
                tiles_data[tile].down == tiles_data[tile_compare].right,
                tiles_data[tile].down == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].down == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].down == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].down == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].left == tiles_data[tile_compare].up,
                tiles_data[tile].left == tiles_data[tile_compare].down,
                tiles_data[tile].left == tiles_data[tile_compare].left,
                tiles_data[tile].left == tiles_data[tile_compare].right,
                tiles_data[tile].left == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].left == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].left == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].left == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].right == tiles_data[tile_compare].up,
                tiles_data[tile].right == tiles_data[tile_compare].down,
                tiles_data[tile].right == tiles_data[tile_compare].left,
                tiles_data[tile].right == tiles_data[tile_compare].right,
                tiles_data[tile].right == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].right == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].right == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].right == tiles_data[tile_compare].right_mirror,
            ]

            compare_list_mirror = [
                tiles_data[tile].up_mirror == tiles_data[tile_compare].up,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].down,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].left,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].right,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].up_mirror == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].down_mirror == tiles_data[tile_compare].up,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].down,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].left,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].right,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].down_mirror == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].left_mirror == tiles_data[tile_compare].up,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].down,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].left,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].right,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].left_mirror == tiles_data[tile_compare].right_mirror,

                tiles_data[tile].right_mirror == tiles_data[tile_compare].up,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].down,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].left,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].right,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].up_mirror,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].down_mirror,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].left_mirror,
                tiles_data[tile].right_mirror == tiles_data[tile_compare].right_mirror,
            ]

            if (True in compare_list) or (True in compare_list_mirror):
                tiles_data[tile].match.append(tile_compare)
            print()

# print()

corners = []

for tile in tiles_data:
    print(f"tile: {tile}\tmatches: {tiles_data[tile].match}")

    if len(tiles_data[tile].match) == 2:
        corners.append(tile)

print(f"corners: {corners}")

product = 1
for corner in corners:
    product = product * corner

print(product)