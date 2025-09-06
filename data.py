import networkx as nx

# Khởi tạo đồ thị
G = nx.Graph()

# Các cạnh và khoảng cách
edges = [
    ("Cổng số 1 (1)", "Khu trò chơi cảm giác mạnh (4)", 171.5),
    ("Cổng số 1 (1)", "Quảng trường Vua Hùng (37)", 170.9),
    ("Cổng số 2 (16)", "Khu trò chơi thiếu nhi (11)", 120.7),
    ("Cổng số 2 (16)", "Quảng trường La Mã (19)", 237.1),
    ("Cổng số 2 (16)", "Bến thuyền 2", 240.8),
    ("Quảng trường Âu Lạc (40)", "Vườn xương rồng (34)", 197.1),
    ("Quảng trường Âu Lạc (40)", "Bến thuyền 1", 91.1),
    ("Quảng trường Âu Lạc (40)", "Cầu Cửu Khúc (43)", 133.8),
    ("Quảng trường Âu Lạc (40)", "Khu trò chơi cảm giác mạnh (4)", 58.2),
    ("Bến thuyền 1", "Vòng lượn tuổi thơ (9)", 72.5),
    ("Bến thuyền 1", "Hồ nước (42)", 133.4),       
    ("Vườn xương rồng (34)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 170.7),
    ("Vườn xương rồng (34)", "Quảng trường Vua Hùng (37)", 113.0),
    ("Vườn xương rồng (34)", "Xe điện đụng thế hệ mới (26)", 198.8),
    ("Lâu đài kinh dị (45)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 248.8),
    ("Lâu đài kinh dị (45)", "Vườn chim thú (49)", 210.3),
    ("Lâu đài kinh dị (45)", "Rạp xiếc (50)", 160.5),   
    ("Xe điện đụng thế hệ mới (26)", "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)", 110.3),
    ("Xe điện đụng thế hệ mới (26)", "Cầu Cửu Khúc (43)", 154.3),
    ("Xe điện đụng thế hệ mới (26)", "Đu quay đứng (25)", 131.8),
    ("Xe điện đụng thế hệ mới (26)", "Bến thuyền 2", 291.6),
    ("Bến thuyền 2", "Hồ nước (42)", 52.4),
    ("Bến thuyền 2", "Quảng trường La Mã (19)", 133.4),
    ("Bến thuyền 2", "Vòng quay thần tốc (22)", 125.2),
    ("Vườn chim thú (49)", "Rạp xiếc (50)", 82.2),
    ("Đu quay đứng (25)", "Vòng quay thần tốc (22)", 98.1),
    ("Vòng lượn tuổi thơ (9)", "Khu trò chơi thiếu nhi (11)", 181.1),
    ("Khu trò chơi cảm giác mạnh (4)", "Quảng trường Vua Hùng (37)", 163.9),
    ("Khu trò chơi cảm giác mạnh (4)", "Bến thuyền 1", 94.0),
    ("Khu trò chơi cảm giác mạnh (4)", "Vòng lượn tuổi thơ (9)", 123.8),
]

G.add_weighted_edges_from(edges)

# Vị trí giả lập
positions = {
    "Cổng số 1 (1)": (725, 666),
    "Cổng số 2 (16)": (1031, 220),

    "Hồ nước (42)": (780, 300),
    "Vườn xương rồng (34)": (528, 464),
    "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)":(415, 336),
    "Cầu Cửu Khúc (43)":(606, 380),
    "Vườn chim thú (49)": (437, 48),

    "Đu quay đứng (25)": (608, 190),
    "Lâu đài kinh dị (45)": (252, 148),
    "Xe điện đụng thế hệ mới (26)":(501, 267),
    "Khu trò chơi cảm giác mạnh (4)":(748, 496),
    "Vòng quay thần tốc (22)":(702, 162),
    "Quảng trường La Mã (19)": (817, 118),

    "Bến thuyền 1": (814, 429),
    "Bến thuyền 2": (792, 249),
    "Rạp xiếc (50)":(411, 126),
    "Vòng lượn tuổi thơ (9)":(870, 475),
    "Khu trò chơi thiếu nhi (11)": (962, 319),  
    "Quảng trường Âu Lạc (40)":(724, 443),
    "Quảng trường Vua Hùng (37)":(595, 555),    
}