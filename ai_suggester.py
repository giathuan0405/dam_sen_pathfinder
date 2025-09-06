def suggest_path_from_description(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["cảnh đẹp", "thư giãn", "hồ", "thiên nhiên"]):
        return [
            "Cổng số 1 (1)",
            "Hồ nước (42)",
            "Vườn xương rồng (34)",
            "Chuồng đà điểu, ngựa vằn, hươu cao cổ (33)",
            "Cầu Cửu Khúc (43)",
            "Vườn chim thú (49)"
        ], "📷 Tour thư giãn - Cảnh đẹp thiên nhiên"

    elif any(keyword in user_input for keyword in ["cảm giác mạnh", "hồi hộp", "mạo hiểm"]):
        return [
            "Cổng số 2 (16)",
            "Đu quay đứng (25)",
            "Lâu đài kinh dị (45)",
            "Xe điện đụng thế hệ mới (26)",
            "Khu trò chơi cảm giác mạnh (4)",
            "Vòng quay thần tốc (22)",
            "Quảng trường La Mã (19)"
        ], "🎢 Tour cảm giác mạnh - Mạo hiểm"

    elif any(keyword in user_input for keyword in ["trẻ em", "thiếu nhi", "gia đình"]):
        return [
            "Cổng số 2 (16)",
            "Khu trò chơi thiếu nhi (11)",
            "Bến thuyền 1",
            "Hồ nước (42)",
            "Rạp xiếc (50)",
            "Bến thuyền 2",
            "Vòng lượn tuổi thơ (9)"
        ], "👨‍👩‍👧‍👦 Tour gia đình - Thiếu nhi"

    else:
        return [], "⚠️ Không nhận diện được chủ đề phù hợp. Vui lòng nhập lại rõ hơn nhé!"

