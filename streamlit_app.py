import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from data import G, positions
from utils import find_path, greedy_tsp

st.set_page_config(page_title="Tìm đường Đầm Sen", layout="wide")
st.title("🗺️ Tìm đường tối ưu trong Công viên Đầm Sen")

# Load ảnh bản đồ
img = Image.open("dam_sen_map.png")
width, height = img.size

# ----- TÌM ĐƯỜNG TỪ A → B -----
st.header("📍 Tìm đường giữa hai địa điểm")

col1, col2 = st.columns(2)
with col1:
    start = st.selectbox("Điểm bắt đầu", list(G.nodes))
with col2:
    end = st.selectbox("Điểm kết thúc", list(G.nodes))

path, total = find_path(G, start, end)

fig, ax = plt.subplots(figsize=(9, 6))
ax.imshow(img, extent=[0, width, height, 0], origin='upper')

for u, v in G.edges():
    x = [positions[u][0], positions[v][0]]
    y = [positions[u][1], positions[v][1]]
    ax.plot(x, y, color='gray', linewidth=1)

if path:
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax.plot(x, y, color='red', linewidth=3)

for node, (x, y) in positions.items():
    color = "lightblue"
    if node == start:
        color = "green"
    elif node == end:
        color = "red"
    elif node in path:
        color = "orange"
    ax.scatter(x, y, s=100, color=color)
    ax.text(x, y, node, fontsize=5, ha="center", va="center", color='black')

ax.axis("off")
st.pyplot(fig)

st.markdown(f"### 📌 Lộ trình: {' ➡️ '.join(path)}")
st.markdown(f"**📏 Tổng khoảng cách:** `{total:.1f} m`")

# ----- AI GỢI Ý TOUR -----
st.header("🧠 Gợi ý tuyến đường du lịch (AI)")

default_start = "Cổng số 1 (1)"
start_point = st.selectbox("🚪 Chọn điểm bắt đầu", [default_start] + list(G.nodes), index=0)

options = st.multiselect(
    "🎯 Chọn các tuyến tham quan bạn muốn:",
    [
        "📷 Thư giãn - Cảnh đẹp thiên nhiên",
        "🎢 Cảm giác mạnh - Mạo hiểm",
        "👨‍👩‍👧‍👦 Gia đình - Thiếu nhi",
        "🌿 Dành cho người lớn tuổi - Nhẹ nhàng, dễ đi",
        "📸 Check-in sống ảo - Kiến trúc đẹp",
        "🐾 Thiên nhiên hoang dã - Động vật"
    ]
)

from ai_suggester import tour_suggestions

if options:
    chosen_points = []
    for opt in options:
        chosen_points.extend(tour_suggestions[opt])
    chosen_points = list(dict.fromkeys(chosen_points))
    if start_point in chosen_points:
        chosen_points.remove(start_point)

    tsp_path, _ = greedy_tsp(start_point, chosen_points, G)

    # Vẽ lộ trình
    full_route = []
    total_distance = 0
    for i in range(len(tsp_path) - 1):
        sub_path, sub_total = find_path(G, tsp_path[i], tsp_path[i + 1])
        if full_route:
            full_route += sub_path[1:]
        else:
            full_route += sub_path
        total_distance += sub_total

    fig2, ax2 = plt.subplots(figsize=(9, 6))
    ax2.imshow(img, extent=[0, width, height, 0], origin='upper')

    for u, v in G.edges():
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax2.plot(x, y, color='lightgray', linewidth=1)

    for i in range(len(full_route) - 1):
        u, v = full_route[i], full_route[i + 1]
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax2.plot(x, y, color='red', linewidth=3)

    for idx, node in enumerate(tsp_path):
        x, y = positions[node]
        ax2.scatter(x, y, s=500, color="orange")
        ax2.text(x, y - 12, f"{idx + 1}", fontsize=10, fontweight='bold',
                 ha="center", va="center", color='white',
                 bbox=dict(facecolor='black', boxstyle='circle,pad=0.3'))
        ax2.text(x, y + 15, node, fontsize=7, ha="center", va="center", color='black')

    ax2.axis("off")
    st.pyplot(fig2)

    st.markdown("### 📌 Lộ trình tối ưu gợi ý:")
    st.markdown(" ➡️ ".join(full_route))
    st.markdown(f"**📏 Tổng khoảng cách:** `{total_distance:.1f} m`")
