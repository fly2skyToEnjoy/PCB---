from PIL import Image

def increase_image_size(input_image_path, output_image_path, scale_factor):
    with Image.open(input_image_path) as image:
        width, height = image.size
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        new_image = image.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(output_image_path)

# 使用函数增大图片尺寸，例如增大2.5倍
increase_image_size(r'F:\script\similarity\images\7_A.jpg', r'F:\script\similarity\images\7_A_scale.jpg', 525/285)