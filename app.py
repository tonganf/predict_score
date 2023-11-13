import streamlit as st
import pandas as pd
# app title
st.title("Hệ thống dự đoán điểm thi HSA")

# Tạo một widget để tải file
file_upload = st.file_uploader("Tải file Excel lên") #, accept=[".xlsx", ".xls"]

# Nếu người dùng tải file lên
if file_upload is not None:
    # Đọc dữ liệu từ file
    data = pd.read_excel(file_upload)

    # Hiển thị dữ liệu
    st.dataframe(data)


gioitinh = st.selectbox(
    'Giới tính',
    ('Nam', 'Nữ'))


col1, col2, col3 = st.columns(3)
with col1:
    tongket10 = st.number_input('Điểm tổng kết lớp 10', min_value=0.0, max_value=9.9)
    toan10 = st.number_input('Điểm tổng kết môn Toán lớp 10', min_value=0.0, max_value=9.9)
    van10 = st.number_input('Điểm tổng kết môn Văn lớp 10', min_value=0.0, max_value=9.9)
    ly10 = st.number_input('Điểm tổng kết môn Vật Lý lớp 10', min_value=0.0, max_value=9.9)
    hoa10 = st.number_input('Điểm tổng kết môn Hóa lớp 10', min_value=0.0, max_value=9.9)
    sinh10 = st.number_input('Điểm tổng kết môn Sinh lớp 10', min_value=0.0, max_value=9.9)
    su10 = st.number_input('Điểm tổng kết môn Sử lớp 10', min_value=0.0, max_value=9.9)
    dia10 = st.number_input('Điểm tổng kết môn Địa lớp 10', min_value=0.0, max_value=9.9)
    gdcd10 = st.number_input('Điểm tổng kết môn Công Dân lớp 10', min_value=0.0, max_value=9.9)
    ngoaingu10 = st.number_input('Điểm tổng kết môn Ngoại Ngữ lớp 10', min_value=0.0, max_value=9.9)
    hocluc10 = st.selectbox(
        'Học lực lớp 10',
        ('Giỏi', 'Khá', 'Trung bình'))
with col2:
    tongket11 = st.number_input('Điểm tổng kết lớp 11', min_value=0.0, max_value=9.9)
    toan11 = st.number_input('Điểm tổng kết môn Toán lớp 11', min_value=0.0, max_value=9.9)
    van11 = st.number_input('Điểm tổng kết môn Văn lớp 11', min_value=0.0, max_value=9.9)
    ly11 = st.number_input('Điểm tổng kết môn Vật Lý lớp 11', min_value=0.0, max_value=9.9)
    hoa11 = st.number_input('Điểm tổng kết môn Hóa lớp 11', min_value=0.0, max_value=9.9)
    sinh11 = st.number_input('Điểm tổng kết môn Sinh lớp 11', min_value=0.0, max_value=9.9)
    su11 = st.number_input('Điểm tổng kết môn Sử lớp 11', min_value=0.0, max_value=9.9)
    dia11 = st.number_input('Điểm tổng kết môn Địa lớp 11', min_value=0.0, max_value=9.9)
    gdcd11 = st.number_input('Điểm tổng kết môn Công Dân lớp 11', min_value=0.0, max_value=9.9)
    ngoaingu11 = st.number_input('Điểm tổng kết môn Ngoại Ngữ lớp 11', min_value=0.0, max_value=9.9)
    hocluc11 = st.selectbox(
        'Học lực lớp 11',
        ('Giỏi', 'Khá', 'Trung bình'))
with col3:
    tongket12 = st.number_input('Điểm tổng kết lớp 12', min_value=0.0, max_value=9.9)
    toan12 = st.number_input('Điểm tổng kết môn Toán lớp 12', min_value=0.0, max_value=9.9)
    van12 = st.number_input('Điểm tổng kết môn Văn lớp 12', min_value=0.0, max_value=9.9)
    ly12 = st.number_input('Điểm tổng kết môn Vật Lý lớp 12', min_value=0.0, max_value=9.9)
    hoa12 = st.number_input('Điểm tổng kết môn Hóa lớp 12', min_value=0.0, max_value=9.9)
    sinh12 = st.number_input('Điểm tổng kết môn Sinh lớp 12', min_value=0.0, max_value=9.9)
    su12 = st.number_input('Điểm tổng kết môn Sử lớp 12', min_value=0.0, max_value=9.9)
    dia12 = st.number_input('Điểm tổng kết môn Địa lớp 12', min_value=0.0, max_value=9.9)
    gdcd12 = st.number_input('Điểm tổng kết môn Công Dân lớp 12', min_value=0.0, max_value=9.9)
    ngoaingu12 = st.number_input('Điểm tổng kết môn Ngoại Ngữ lớp 12', min_value=0.0, max_value=9.9)
    hocluc12 = st.selectbox(
        'Học lực lớp 12',
        ('Giỏi', 'Khá', 'Trung bình'))

if st.button('Dự đoán kết quả HSA'):
    st.write('Kết quả dự đoán là: ....')
#st.write('The current number is ', number)