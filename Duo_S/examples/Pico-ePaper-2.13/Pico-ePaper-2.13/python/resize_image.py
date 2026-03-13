from PIL import Image

# 打开图像文件
image = Image.open('/path/to/input.jpg')

# 新的尺寸
new_width = 250
new_height = 122

# 改变图像尺寸
resized_image = image.resize((new_width, new_height))

# 显示图像
resized_image.show()

# 保存图像
resized_image.save('output.jpg')
