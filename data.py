import networkx as nx

# Khởi tạo đồ thị
G = nx.Graph()

# Các cạnh và khoảng cách
edges = [
    ("Cổng số 1 (1)", "Quảng trường Âu Lạc (40)", 223.0),
    ("Quảng trường Âu Lạc (40)", "Vườn xương rồng (34)", 197.1),
    ("Quảng trường Âu Lạc (40)", "Bến thuyền (7)", 91.1),
    ("Bến thuyền (7)", "Vòng lượn tuổi thơ (9)", 72.5),
    ("Hồ nước (42)", "Bến thuyền (7)", 133.4),                      
    ("Vòng lượn tuổi thơ (9)", "Khu trò chơi thiếu nhi (11)", 181.1),
    ("Cổng số 2 (16)", "Khu trò chơi thiếu nhi (11)", 120.7),
    ("Cổng số 2 (16)", "Quảng trường La Mã (19)", 237.1),
    ("Đu quay đứng (25)", "Quảng trường La Mã (19)", 221.1),
    ("Đu quay đứng (25)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 242.0),
    ("Vườn xương rồng (34)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 170.7),
    ("Lâu đài kinh dị (45)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 248.8),
    ("Lâu đài kinh dị (45)", "Vườn chim thú (49)", 210.3),
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
    "Quảng trường Âu Lạc (40)":(724, 443),
    "Vòng lượn tuổi thơ (9)":(870, 475),
    "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)":(415, 336),
}
