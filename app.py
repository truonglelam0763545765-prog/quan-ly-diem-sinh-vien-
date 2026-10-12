Python 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import matplotlib.pyplot as plt
... import numpy as np
... import pandas as pd
... import streamlit as st
... 
... # --- 1. TẠO DỮ LIỆU VÀ TÍNH TOÁN (PANDAS) ---
... data = {
...     "Ho_ten": [
...         "Nguyễn Văn An",
...         "Trần Thị Bích",
...         "Lê Hoàng Cường",
...         "Phạm Thị Dung",
...         "Hoàng Văn Em",
...         "Vũ Thị Phương",
...         "Đỗ Minh Giang",
...         "Bùi Thị Hoa",
...         "Ngô Quang Huy",
...         "Hồ Thị Kim",
...     ],
...     "Chuyen_can": [8.0, 9.0, 7.5, 6.0, 9.5, 8.5, 4.0, 7.0, 8.5, 6.5],
...     "Giua_ky": [7.5, 8.0, 6.5, 5.5, 9.0, 7.0, 3.5, 6.5, 8.0, 6.0],
...     "Cuoi_ky": [8.0, 8.5, 7.0, 5.0, 9.5, 7.5, 4.5, 6.5, 8.5, 5.5],
... }
... 
... df = pd.DataFrame(data)
... 
... # Tính điểm tổng kết (Yêu cầu 2)
... df["Tong_ket"] = (
...     0.2 * df["Chuyen_can"] + 0.3 * df["Giua_ky"] + 0.5 * df["Cuoi_ky"]
... ).round(2)
... 
... 
... # Xếp loại sinh viên (Yêu cầu 3)
... def xep_loai(score):
...   if score >= 8.5:
...     return "Giỏi"
...   elif score >= 7.0:
    return "Khá"
  elif score >= 5.0:
    return "Trung bình"
  else:
    return "Yếu"


df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# Thống kê cơ bản (Yêu cầu 4)
dtb_lop = df["Tong_ket"].mean()
max_sv = df.loc[df["Tong_ket"].idxmax()]
min_sv = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = len(df[df["Tong_ket"] >= 5.0])

# --- 2. XÂY DỰNG GIAO DIỆN WEB APP (STREAMLIT) ---
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Hiển thị bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True)

# Hiển thị thống kê
st.subheader("Thống kê lớp học")
col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label="Điểm trung bình lớp", value=f"{dtb_lop:.2f}")
with col2:
  st.metric(
      label="Điểm cao nhất",
      value=f"{max_sv['Ho_ten']} ({max_sv['Tong_ket']}đ)",
  )
with col3:
  st.metric(
      label="Điểm thấp nhất",
      value=f"{min_sv['Ho_ten']} ({min_sv['Tong_ket']}đ)",
  )

st.info(f"Số sinh viên đạt (Điểm tổng kết >= 5.0): **{so_sv_dat} / 10**")

# Danh sách chọn sinh viên xem chi tiết
st.subheader("Tra cứu thông tin cá nhân sinh viên")
selected_student = st.selectbox(
    "Chọn tên sinh viên cần xem:", df["Ho_ten"].tolist()
)
student_info = df[df["Ho_ten"] == selected_student].iloc[0]

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Chuyên cần", student_info["Chuyen_can"])
c2.metric("Giữa kỳ", student_info["Giua_ky"])
c3.metric("Cuối kỳ", student_info["Cuoi_ky"])
c4.metric("Tổng kết", student_info["Tong_ket"])
c5.metric("Xếp loại", student_info["Xep_loai"])

# Biểu đồ cột (Yêu cầu 5)
st.subheader("Biểu đồ điểm tổng kết của lớp")
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"], color="skyblue", edgecolor="black")
ax.set_xlabel("Họ và tên sinh viên", fontsize=11)
ax.set_ylabel("Điểm tổng kết", fontsize=11)
ax.set_title("Biểu đồ điểm tổng kết 10 sinh viên", fontsize=13, weight="bold")
plt.xticks(rotation=45, ha="right")
ax.set_ylim(0, 10)
st.pyplot(fig)

# Chân trang (Footer)
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray; font-size: small;'>Người tạo ứng"
    " dụng: LÊ LÂm TRường  - MSSV: 051208013991
    </p>",
    unsafe_allow_html=True,
