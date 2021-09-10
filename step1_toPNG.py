########################################################################################################################

# Supported Image File
# - Aperio (.svs, .tif)
# - Hamamatsu (.vms, .vmu, .ndpi)
# - Leica (.scn)
# - MIRAX (.mrxs)
# - Philips (.tiff)
# - Sakura (.svslide)
# - Trestle (.tif)
# - Ventana (.bif, .tif)
# - Generic tiled TIFF (.tif)

# Input SVS File Path and Name
input_path = "/home/jkim/Converter/data/histology_olympus/Image_01.vsi"

# Output PNG File Path
output_path = "/home/jkim/Converter/data/"

# Set PNG Quality and Low Resolution
# 0: LOW MODE. Reduce Quality and Low Resolution
# 1: ORIGINAL MODE. Keep Original Quality and Resolution (IT TAKES VERY LONG TIME)
resolution = 0

########################################################################################################################

import os
import time
import openslide

svs = openslide.OpenSlide(input_path)
print("Load SVS file successfully.")

if resolution == 0:
    print("Now Converting...")
    start = time.time()
    png = svs.read_region((0, 0), svs.level_count - 1, svs.level_dimensions[svs.level_count - 1])
    output_path = output_path + str(os.path.basename(input_path)[:-4]) + "_LOW.png"
    png.save(output_path)
    print("Converted PNG file successfully:", output_path)
    print("Total Time:", time.time() - start)

elif resolution == 1:
    print("Now Converting... (WARNING: ORIGINAL MODE takes very long time. Please stay tuned.)")
    start = time.time()
    png = svs.read_region((0, 0), 0, svs.level_dimensions[0])
    output_path = output_path + str(os.path.basename(input_path)[:-4]) + ".png"
    png.save(output_path)
    print("Converted PNG file successfully:", output_path)
    print("Total Time:", time.time() - start)

else:
    print("ERROR: Incorrect configuration value.")
