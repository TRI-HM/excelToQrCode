import os
import pandas as pd
import qrcode
import urllib.parse

# Đường dẫn file Excel và thư mục xuất QR code
input_file = "apec_hn.xlsx"  # Đổi thành đường dẫn tới file Excel của bạn
project_name = "apec_hn_jpg"
output_dir = f"export/{project_name}"

# Tạo thư mục export nếu chưa tồn tại
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Đọc file Excel
df = pd.read_excel(input_file)

# Duyệt qua từng dòng trong DataFrame
for index, row in df.iterrows():
    # Lấy giá trị id và name từ dòng hiện tại
    user_id = row['no']
    name = row['name']
    name = str(name).replace("|", "")
    link = row['link'] if 'link' in row else ''

    # Lấy giá trị dob từ dòng hiện tại và chuyển sang định dạng dd-mm-yyyy
    # dob = row['dob']
    # dob = str(dob).replace("/", "-")

    # Mã hóa name sang Base64
    # encoded_name = urllib.parse.quote(name)
    # decode_name = urllib.parse.unquote(encoded_name)
    
    # Thay thế dấu "+" và "/" thành "-"
    # encoded_name = encoded_name.replace("+", "-").replace("/", "-").replace("=", "")

    # Tạo giá trị cho QR code với name đã mã hóa
    # qr_value = f"https://huynhminhtri.dev?uuid={user_id}&name={encoded_name}&dob={dob}"
    # qr_value = f"id={user_id}&name={encoded_name}&title={encoded_title}"
    
    # Tạo QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)
    
    # Tạo ảnh QR code
    img = qr.make_image(fill_color="black", back_color="white") # back_color="transparent"
    
    # Đường dẫn lưu file QR code
    output_path = os.path.join(output_dir, f"{user_id}_{name}.jpg") #.png
    img.save(output_path)
    print(f"Đã tạo QR code cho {name}. Lưu tại {output_path}")
    print(f"Giá trị QR code: {link}")
