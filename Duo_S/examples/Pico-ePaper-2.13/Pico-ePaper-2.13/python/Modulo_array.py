from PIL import Image

def image_to_vertical_bitmap_array(image_path):
    # 打开图像并转换为单色模式
    img = Image.open(image_path).convert('1').transpose(Image.FLIP_LEFT_RIGHT)
    pixels = img.load()
    width, height = img.size
    bitmap_array = []

    # 遍历每一列像素
    for x in range(width):
        column_bytes = []
        current_byte = 0
        bit_index = 0

        # 遍历列中的每个像素
        for y in range(height):
            # 检查像素是白色还是黑色（255为白色，0为黑色）
            if pixels[x, y] == 255:
                bit = 0
            else:
                bit = 1

            # 将位添加到当前字节
            current_byte |= bit << bit_index
            bit_index += 1

            # 如果已经收集了8位或者到达列的末尾
            if bit_index == 8 or y == height - 1:
                column_bytes.append(current_byte)
                current_byte = 0
                bit_index = 0

        # 将这一列的字节添加到总数组
        bitmap_array.append(column_bytes)

    return bitmap_array

# 使用这个函数
if __name__ == "__main__":
    bitmap = image_to_vertical_bitmap_array("/path/to/output.bmp")
    for column in bitmap:
        print(','.join('0x{:02X}'.format(byte) for byte in column) + ',')
    
