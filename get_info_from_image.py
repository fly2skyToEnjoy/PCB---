import os
import cv2
# 读取图片
image_path_1_path = r"F:\script\similarity\images\7_B.jpg"
# image_path_2_path = r"F:\script\similarity\12.jpg"

image_path_1 = cv2.imread(image_path_1_path)
# image_path_2 = cv2.imread(image_path_2_path)

# 获取图片的尺寸
height, width = image_path_1.shape[:2]
print(f'Width: {width}, Height: {height}')

# height, width = image_path_2.shape[:2]
# print(f'Width: {width}, Height: {height}')

# [287,287]  ->  [525,525]
# [760,525]