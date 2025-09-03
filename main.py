from PIL import Image
import matplotlib.pyplot as plt
import networkx as nx

# 1. Tạo đồ thị mô phỏng công viên Đầm Sen
G = nx.Graph()

# 2. Danh sách các đường đi (giả định khoảng cách mét)
edges = [
    ("Cổng số 1 (1)", "Hồ nước (42)", 370.1),
    ("Cổng số 1 (1)", "Bến thuyền (7)", 253.2),
    ("Cổng số 2 (16)", "Quảng trường La Mã (19)", 236.6),
    ("Cổng số 2 (16)", "Khu trò chơi thiếu nhi (11)", 122.3),
    ("Hồ nước (42)", "Bến thuyền (7)", 133.4),
    ("Hồ nước (42)", "Quảng trường La Mã (19)", 186.7),
    ("Hồ nước (42)", "Đu quay đứng (25)", 204.2),
    ("Bến thuyền (7)", "Khu trò chơi thiếu nhi (11)", 184.4),
    ("Lâu đài kinh dị (45)", "Vườn xương rồng (34)", 418.1),
    ("Vườn xương rồng (34)", "Vườn chim thú (49)", 424.9),
    ("Vườn chim thú (49)", "Đu quay đứng (25)", 222.3),
    ("Đu quay đứng (25)", "Quảng trường La Mã (19)", 221.4),
]


G.add_weighted_edges_from(edges)

# 3. Tọa độ giả định trên bản đồ (bạn chỉnh tay để khớp với ảnh dam_sen_map.png)
positions = {
    "Cổng số 1 (1)": (725, 666),
    "Cổng số 2 (16)": (1031, 220),
    "Hồ nước (42)": (780, 300),
    "Bến thuyền (7)": (814, 429),
    "Vườn chim thú (49)": (437, 48),
    "Khu trò chơi thiếu nhi (11)": (962, 319),
    "Quảng trường La Mã (19)": (817, 118),
    "Lâu đài kinh dị (45)": (252, 148),
    "Vườn xương rồng (34)":(528,464),
    "Đu quay đứng (25)":(608,190),
}


# 4. Chọn điểm bắt đầu & kết thúc
start = "Cổng số 1 (1)"
end = "Cổng số 2 (16)"

# 5. Chạy thuật toán Dijkstra
path = nx.dijkstra_path(G, start, end)
length = nx.dijkstra_path_length(G, start, end)

# 6. Load ảnh bản đồ và tự lấy kích thước
img = Image.open("dam_sen_map.png")
width, height = img.size

plt.figure(figsize=(10, 8))
# extent dựa vào kích thước ảnh, origin='lower' để trục y hướng lên
plt.imshow(img, extent=[0, width, height, 0], origin="upper")


# 7. Vẽ toàn bộ đồ thị
nx.draw(G, pos=positions, with_labels=True, node_color="lightblue", node_size=2000)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos=positions, edge_labels=edge_labels)

# 8. Tô đậm đường đi tối ưu
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(G, pos=positions, edgelist=path_edges, edge_color="red", width=3)

# 9. In kết quả và hiển thị
print("🔍 Đường đi tối ưu:", " -> ".join(path))
print("📏 Tổng khoảng cách:", length, "m")

plt.title("Đường đi tối ưu trong Công viên Đầm Sen")
plt.axis("off")
plt.tight_layout()
plt.savefig("result_path.png", dpi=150, bbox_inches="tight")  # lưu ảnh kết quả
plt.show()
