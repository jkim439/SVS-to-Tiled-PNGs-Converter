########################################################################################################################

# Input SVS File Path and Name
input_path = "/home/jkim/Converter/data/CMU-1.png"

# Output tiled PNG File Path
output_path = "/home/jkim/Converter/data/tiled"

########################################################################################################################

import os
os.environ["OPENCV_IO_MAX_IMAGE_PIXELS"] = pow(2,40).__str__()

import cv2
import math
import time

print("Now Loading...")
start = time.time()
img = cv2.imread(input_path)
print("Load PNG file successfully.")

img_shape = img.shape
tile_size = (512, 512)
offset = (512, 512)
for i in range(int(math.ceil(img_shape[0]/(offset[1] * 1.0)))):
    for j in range(int(math.ceil(img_shape[1]/(offset[0] * 1.0)))):
        cropped_img = img[offset[1]*i:min(offset[1]*i+tile_size[1], img_shape[0]), offset[0]*j:min(offset[0]*j+tile_size[0], img_shape[1])]
        # Debugging the tiles
        cv2.imwrite(os.path.join(output_path, str(i) + "_" + str(j) + ".png"), cropped_img)
        print("Creating tiled PNG file...", str(i) + "_" + str(j) + ".png")

print("Converted tiled PNG files successfully:", output_path)
print("Total Time:", time.time() - start)