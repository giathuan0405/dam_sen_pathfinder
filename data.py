import networkx as nx

# Khởi tạo đồ thị
G = nx.Graph()

# Các cạnh và khoảng cách
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

# Vị trí giả lập
positions = {
    "Cổng số 1 (1)": (725, 666),
    "Cổng số 2 (16)": (1031, 220),
    "Hồ nước (42)": (780, 300),
    "Bến thuyền (7)": (814, 429),
    "Vườn chim thú (49)": (437, 48),
    "Khu trò chơi thiếu nhi (11)": (962, 319),
    "Quảng trường La Mã (19)": (817, 118),
    "Lâu đài kinh dị (45)": (252, 148),
    "Vườn xương rồng (34)": (528, 464),
    "Đu quay đứng (25)": (608, 190),
}
