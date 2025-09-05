import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from data import G, positions
from utils import find_path

st.set_page_config(page_title="Tìm đường Đầm Sen", layout="wide")
st.title("🗺️ Tìm đường tối ưu trong Công viên Đầm Sen")

# Chọn điểm bắt đầu và kết thúc
col1, col2 = st.columns(2)
with col1:
    start = st.selectbox("📍 Điểm bắt đầu", list(G.nodes))
with col2:
    end = st.selectbox("🏁 Điểm kết thúc", list(G.nodes))

# Tính đường đi
path, total = find_path(G, start, end)

# Load ảnh bản đồ
img = Image.open("dam_sen_map.png")
width, height = img.size

# Vẽ đồ thị trên bản đồ
fig, ax = plt.subplots(figsize=(9, 6))

ax.imshow(img, extent=[0, width, height, 0], origin='upper')

# Vẽ tất cả các cạnh (xám)
for u, v in G.edges():
    x = [positions[u][0], positions[v][0]]
    y = [positions[u][1], positions[v][1]]
    ax.plot(x, y, color='gray', linewidth=1)

# Vẽ đường đi tối ưu (đỏ)
if path:
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax.plot(x, y, color='red', linewidth=3)

# Vẽ các nút
for node, (x, y) in positions.items():
    color = "lightblue"
    if node == start:
        color = "green"
    elif node == end:
        color = "red"
    elif node in path:
        color = "orange"
    ax.scatter(x, y, s=500, color=color)
    ax.text(x, y, node, fontsize=9, ha="center", va="center", color='black')

ax.axis("off")
st.pyplot(fig)

if path:
    st.markdown(f"### 📌 Lộ trình: {' ➡️ '.join(path)}")
    st.markdown(f"**📏 Tổng khoảng cách:** `{total:.1f} m`")
