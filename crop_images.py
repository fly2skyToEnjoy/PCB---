import os
import cv2
# 读取图片
# image_path = r"F:\script\similarity\images"
# for file in os.listdir(image_path):
#     root_path= os.getcwd() + "\\images\\"
#     image = cv2.imread(root_path + file)
#     # 获取图片的尺寸
#     height, width = image.shape[:2]
#     print(f'Width: {width}, Height: {height}')
#     roi_image_001 = image[241:528,89:376]
#     # roi_image_002 = image[380:241, 1140:766]
#     roi_image_002 = image[241:766, 380:1140]
#
#     # cv2.circle(image,(89,241),10,color=(255, 0,0))
#     # cv2.circle(image, (376,528),10, color=(255, 0, 0))
#     save_path = root_path + file.split(".")[0] + "_A.jpg"
#     # roi_image_001 = image
#     cv2.imwrite(save_path,roi_image_001)
#     cv2.imwrite(root_path + file.split(".")[0] + "_B.jpg", roi_image_002)

#获取一张图片(525,525)
# image_path = r"F:\script\similarity\images\7_B.jpg"
# image = cv2.imread(image_path)
#
# x,y,w,h = 50,50,525,525
#
# roi_image = image[y:y+h, x:x+w]
# cv2.imwrite(r"F:\script\similarity\images\7_B_crop.jpg",roi_image)

from PIL import Image

# 读取图片
image = Image.open(r'F:\script\similarity\images\7_B.jpg')

# 定义x, y, w, h 的值，这里需要你根据实际情况设置
x,y,w,h = 50,50,525,525

# 根据坐标和宽高抠图
cropped_image = image.crop((x, y, x + w, y + h))

# 保存抠图
cropped_image.save(r'F:\script\similarity\images\7_B_crop_11.jpg')