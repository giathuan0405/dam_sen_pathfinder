import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
from data import G, positions
from utils import find_path
from ai_suggester import suggest_path_from_description
from itertools import permutations

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
    ax.scatter(x, y, s=100, color=color)
    ax.text(x, y, node, fontsize=5, ha="center", va="center", color='black')

ax.axis("off")
st.pyplot(fig)

fig.savefig("result_path.png", dpi=150, bbox_inches="tight")


if path:
    st.markdown(f"### 📌 Lộ trình: {' ➡️ '.join(path)}")
    st.markdown(f"**📏 Tổng khoảng cách:** `{total:.1f} m`")

from itertools import permutations

st.header("🧠 Gợi ý tuyến đường du lịch (AI)")

# Chọn điểm bắt đầu
default_start = "Cổng số 1 (1)"
start_point = st.selectbox(
    "🚪 Chọn điểm bắt đầu (mặc định là Cổng số 1):",
    [default_start] + list(G.nodes),
    index=0
)

# Lựa chọn loại tour
options = st.multiselect(
    "🎯 Chọn các tuyến tham quan bạn muốn:",
    [
        "📷 Thư giãn - Cảnh đẹp thiên nhiên",
        "🎢 Cảm giác mạnh - Mạo hiểm",
        "👨‍👩‍👧‍👦 Gia đình - Thiếu nhi"
    ]
)

# Định nghĩa tuyến mẫu
tour_suggestions = {
    "📷 Thư giãn - Cảnh đẹp thiên nhiên": [
        "Hồ nước (42)", "Bến thuyền (7)",
        "Vườn xương rồng (34)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)"
    ],
    "🎢 Cảm giác mạnh - Mạo hiểm": [
         "Đu quay đứng (25)", "Lâu đài kinh dị (45)", "Quảng trường La Mã (19)"
    ],
    "👨‍👩‍👧‍👦 Gia đình - Thiếu nhi": [
       "Khu trò chơi thiếu nhi (11)", "Bến thuyền (7)", "Hồ nước (42)"
    ]
}

if options:
    # Gộp tất cả các điểm
    chosen_points = []
    for opt in options:
        chosen_points.extend(tour_suggestions[opt])

    # Loại trùng và đảm bảo điểm bắt đầu đứng đầu
    chosen_points = list(dict.fromkeys(chosen_points))
    if start_point in chosen_points:
        chosen_points.remove(start_point)
    all_points = [start_point] + chosen_points

    # TSP - tìm thứ tự ghé thăm tối ưu (giữ nguyên điểm đầu)
    min_path = None
    min_total = float("inf")

    for perm in permutations(chosen_points):
        candidate = [start_point] + list(perm)
        total = 0
        valid = True
        for i in range(len(candidate) - 1):
            try:
                _, sub_total = find_path(G, candidate[i], candidate[i + 1])
                total += sub_total
            except:
                valid = False
                break
        if valid and total < min_total:
            min_total = total
            min_path = candidate

    # Nối đường đi đầy đủ
    full_route = []
    total_distance = 0
    for i in range(len(min_path) - 1):
        sub_path, sub_total = find_path(G, min_path[i], min_path[i + 1])
        if full_route:
            full_route += sub_path[1:]
        else:
            full_route += sub_path
        total_distance += sub_total

    # Vẽ bản đồ
    fig4, ax4 = plt.subplots(figsize=(9, 6))
    ax4.imshow(img, extent=[0, width, height, 0], origin='upper')

    # Vẽ các cạnh (xám)
    for u, v in G.edges():
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax4.plot(x, y, color='lightgray', linewidth=1)

    # Vẽ đường đi (đỏ)
    for i in range(len(full_route) - 1):
        u, v = full_route[i], full_route[i + 1]
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax4.plot(x, y, linewidth=3, color="red")

    # Tô màu cam và đánh số THỨ TỰ CHỈ CHO CÁC ĐIỂM GHÉ
    for idx, node in enumerate(min_path):
        x, y = positions[node]
        ax4.scatter(x, y, s=500, color="orange")  # chỉ tô các điểm ghé
        ax4.text(
            x, y - 12, f"{idx + 1}",
            fontsize=10, fontweight='bold',
            ha="center", va="center",
            color='white',
            bbox=dict(facecolor='black', boxstyle='circle,pad=0.3')
        )
        ax4.text(
            x, y + 15, node,
            fontsize=7,
            ha="center", va="center",
            color='black'
        )

    ax4.axis("off")
    st.pyplot(fig4)

    # Hiển thị kết quả
    st.markdown("### 📌 Lộ trình tối ưu gợi ý:")
    st.markdown(" ➡️ ".join(full_route))
    st.markdown(f"**📏 Tổng khoảng cách:** `{total_distance:.1f} m`")
