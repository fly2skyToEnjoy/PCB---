import os
import numpy as np
import cv2
from PIL import Image

#增加图片的大小
def increase_image_size(input_image_path, output_image_path, scale_factor):
    with Image.open(input_image_path) as image:
        width, height = image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        new_image = image.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(output_image_path)

def ssim(img1, img2):
    # 将图像转换为灰度图像
    image1 = cv2.imread(img1)

    image2 = cv2.imread(img2)


    gray_img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 计算图像的均值和方差
    mean1, mean2 = np.mean(gray_img1), np.mean(gray_img2)
    var1, var2 = np.var(gray_img1), np.var(gray_img2)

    # 计算协方差和SSIM指数
    cov = np.cov(gray_img1.flatten(), gray_img2.flatten())[0, 1]
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2
    ssim = (2 * mean1 * mean2 + c1) * (2 * cov + c2) / ((mean1 ** 2 + mean2 ** 2 + c1) * (var1 + var2 + c2))

    return ssim



image_path = r"F:\script\similarity\images\test_images_all"

#获取源图片
#A图左上角(90,242)、右下角(375、527),x,y,w,h = 90,242,285,285
#B图左上角(382,242)、右下角(1142,767),x,y,w,h =382,242,760,525

for file in os.listdir(image_path):
    print("图片名为：",str(file))
    # 根据坐标截取图片
    image = Image.open(r"F:\script\similarity\images\test_images_all" + "\\"+   file)

    #抠A图
    # 定义x, y, w, h 的值，这里需要你根据实际情况设置
    x,y,w,h = 90,242,285,285

    # 根据坐标和宽高抠图
    A_cropped_image = image.crop((x, y, x + w, y + h))
    # 保存抠图
    save_path = r"F:\script\similarity\images\test_images_all"
    A_cropped_image.save(save_path + "\\" + file.split(".")[0] + "_A.jpg")

    #抠B图
    # 定义x, y, w, h 的值，这里需要你根据实际情况设置
    x,y,w,h = 382,242,760,525

    # 根据坐标和宽高抠图
    B_cropped_image = image.crop((x, y, x + w, y + h))

    # 保存抠图
    B_cropped_image.save(save_path + "\\" + file.split(".")[0] + "_B.jpg")

    #将左上角图片放大
    increase_image_size(save_path + "\\" + file.split(".")[0] + "_A.jpg", save_path + "\\" + file.split(".")[0] + "_A_scale.jpg", 525/285)

    #(760,525)
    #对 _B的图片进行遍历截取
    image = Image.open(save_path + "\\" + file.split(".")[0] + "_B.jpg")

    #B图
    # 定义x, y, w, h 的值，这里需要你根据实际情况设置
    y, w, h =  0, 525, 525
    for x in range(0,230,23):
        # 根据坐标和宽高抠图
        cropped_image_range = image.crop((x, y, x + w, y + h))

        # 保存抠图
        cropped_image_range.save(save_path + "\\" + file.split(".")[0] + "_x" +"_B.jpg")

        # 与右侧裁剪图片进行比对
        # 计算两幅图像的SSIM指数
        ssim_index = ssim(save_path + "\\" + file.split(".")[0] + "_A_scale.jpg", save_path + "\\" + file.split(".")[0] + "_x" +"_B.jpg" )
        print("ssim_index" + str(x) ,ssim_index)

        if os.path.exists(save_path + "\\" + file.split(".")[0] + "_x" +"_B.jpg"):  # 先检查文件是否存在以避免错误
            os.remove(save_path + "\\" + file.split(".")[0] + "_x" +"_B.jpg")
    print("********" * 10)

    if os.path.exists(save_path + "\\" + file.split(".")[0] + "_A_scale.jpg"):  # 先检查文件是否存在以避免错误
        os.remove(save_path + "\\" + file.split(".")[0] + "_A_scale.jpg")

    if os.path.exists(save_path + "\\" + file.split(".")[0] + "_A.jpg"):  # 先检查文件是否存在以避免错误
        os.remove(save_path + "\\" + file.split(".")[0] + "_A.jpg")
    if os.path.exists(save_path + "\\" + file.split(".")[0] + "_B.jpg"):  # 先检查文件是否存在以避免错误
        os.remove(save_path + "\\" + file.split(".")[0] + "_B.jpg")

