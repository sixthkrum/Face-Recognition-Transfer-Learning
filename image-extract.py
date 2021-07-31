import os
import shutil

lfw_dir = "lfw-deepfunneled"
out_dir = "unedited"
folder_list = os.listdir('./' + lfw_dir)
images_listings = []
dummy_listing = []

for folder in folder_list:
    folder_path = './' + lfw_dir + '/' + folder
    num_images = len(os.listdir(folder_path))
    if num_images >= 8:
        dummy_listing += [folder_path]
        dummy_listing += ['./' + out_dir + '/' + folder]
        dummy_listing += [num_images]
        images_listings.append(dummy_listing)
        dummy_listing = []

images_listings = sorted(images_listings, key=lambda triplet: triplet[2], reverse=True)

for i in range(10):
    shutil.copytree(images_listings[i][0], images_listings[i][1], dirs_exist_ok=True)
