import cv2
import numpy as np


def ssim(img1, img2):
    # 将图像转换为灰度图像
    gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # 计算图像的均值和方差
    mean1, mean2 = np.mean(gray_img1), np.mean(gray_img2)
    var1, var2 = np.var(gray_img1), np.var(gray_img2)

    # 计算协方差和SSIM指数
    cov = np.cov(gray_img1.flatten(), gray_img2.flatten())[0, 1]
    c1 = (0.01 * 255) ** 2
    c2 = (0.03 * 255) ** 2
    ssim = (2 * mean1 * mean2 + c1) * (2 * cov + c2) / ((mean1 ** 2 + mean2 ** 2 + c1) * (var1 + var2 + c2))

    return ssim


# 读取两幅图像
image1 = cv2.imread(r'F:\script\similarity\images\test_images\7_A_scale.jpg')

# -0.05775078147650043
# -0.18602167293418592
# 0.037325918518787554

image2 = cv2.imread(r'F:\script\similarity\images\7_B_crop_11.jpg')

# 计算两幅图像的SSIM指数
ssim_index = ssim(image1, image2)

#获取两张图像的大小信息

# 获取图片的尺寸
height, width = image1.shape[:2]
print(f'Width: {width}, Height: {height}')

height, width = image2.shape[:2]
print(f'Width: {width}, Height: {height}')


# 打印SSIM指数
print("SSIM Index:", ssim_index)