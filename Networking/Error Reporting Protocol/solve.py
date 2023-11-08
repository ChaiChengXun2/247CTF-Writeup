with open('output.txt', 'r') as file:
    hex_data = file.read()

jpeg_data = bytes.fromhex(hex_data)

with open('output.jpg', 'wb') as jpg_file:
    jpg_file.write(jpeg_data)