def suggest_path_from_description(user_input):
    user_input = user_input.lower()

    if any(keyword in user_input for keyword in ["cảnh đẹp", "thư giãn", "hồ", "thiên nhiên"]):
        return [
            "Cổng số 1 (1)",
            "Hồ nước (42)",
            "Bến thuyền (7)",
            "Vườn xương rồng (34)",
            "Vườn chim thú (49)"
        ], "Tour thư giãn - Cảnh đẹp"

    elif any(keyword in user_input for keyword in ["cảm giác mạnh", "hồi hộp", "mạo hiểm"]):
        return [
            "Cổng số 2 (16)",
            "Đu quay đứng (25)",
            "Lâu đài kinh dị (45)",
            "Quảng trường La Mã (19)"
        ], "Tour cảm giác mạnh"

    elif any(keyword in user_input for keyword in ["trẻ em", "thiếu nhi", "gia đình"]):
        return [
            "Cổng số 2 (16)",
            "Khu trò chơi thiếu nhi (11)",
            "Bến thuyền (7)",
            "Hồ nước (42)"
        ], "Tour gia đình - Thiếu nhi"

    else:
        return [], "Không nhận diện được chủ đề phù hợp. Vui lòng nhập lại rõ hơn nhé!"
