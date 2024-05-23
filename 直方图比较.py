import cv2

# 读入两张图像
# img1 = cv2.imread('image1.jpg', cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('image2.jpg', cv2.IMREAD_GRAYSCALE)

img1 = cv2.imread(r'F:\script\similarity\images\1.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'F:\script\similarity\images\1.jpg',cv2.IMREAD_GRAYSCALE)


# 如果图像为空，输出错误信息并退出
if img1 is None or img2 is None:
    print('Failed to read image file.')
    exit()

# 计算直方图
hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

# 归一化直方图
hist1 = cv2.normalize(hist1, None, 0, 1, cv2.NORM_MINMAX)
hist2 = cv2.normalize(hist2, None, 0, 1, cv2.NORM_MINMAX)

# 计算直方图比较结果
cmp = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

# 输出直方图比较结果
print('Histogram Comparison:', cmp)
