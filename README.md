# Đầm Sen Pathfinder 🏞️

Hệ thống tìm đường tối ưu và gợi ý tour tham quan tại công viên Đầm Sen, được xây dựng bằng Python và Streamlit. Ứng dụng sử dụng thuật toán Dijkstra để tìm đường ngắn nhất giữa hai điểm, và Greedy TSP để gợi ý tour tham quan tối ưu theo chủ đề.

---

## 🧠 Chức năng chính

- ✅ Tìm đường ngắn nhất giữa hai địa điểm trong công viên (Dijkstra)
- ✅ Gợi ý tour tham quan theo chủ đề: thiên nhiên, động vật, trò chơi, v.v.
- ✅ Vẽ đường đi trên bản đồ tĩnh của công viên (overlay bằng Matplotlib)
- ✅ Giao diện tương tác bằng Streamlit đơn giản, dễ sử dụng

---

## 🗂️ Cấu trúc thư mục
dam_sen_pathfinder/
│
├── data.py # Chứa dữ liệu bản đồ: node, cạnh, vị trí
├── utils.py # Các hàm vẽ bản đồ, tìm đường,...
├── ai_suggester.py # Thuật toán gợi ý tour Greedy TSP
├── streamlit_app.py # Giao diện người dùng Streamlit
├── dam_sen_map.png # Bản đồ công viên nền
├── requirements.txt # Danh sách thư viện cần cài đặt

---

## 🚀 Hướng dẫn chạy ứng dụng

### 1. Cài Python
- Đảm bảo bạn có **Python 3.9 hoặc mới hơn** (khuyên dùng Python 3.10)

### 2. Tạo môi trường ảo (tuỳ chọn nhưng khuyến khích)

```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
streamlit run streamlit_app.py

