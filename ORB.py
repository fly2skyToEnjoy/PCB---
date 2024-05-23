import cv2
import numpy as np

# 读取图像
img1 = cv2.imread(r'F:\script\similarity\images\1.jpg', 0)  # 查询图像
img2 = cv2.imread(r'F:\script\similarity\images\1.jpg', 0)  # 训练(目标)图像

# 初始化ORB检测器
orb = cv2.ORB_create()

# 检测ORB特征点并计算描述符
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# 创建BFMatcher对象
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# 进行匹配
matches = bf.match(des1, des2)

# 根据距离排序，距离小的是更好的匹配点
matches = sorted(matches, key=lambda x: x.distance)
print(matches)
# 绘制前N个匹配
N = 100 # 可以调整这个值来看更多或更少的匹配
matched_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:N], None, flags=2)

# 显示图像
cv2.imshow('Matches', matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()