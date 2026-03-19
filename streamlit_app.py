import streamlit as st

st.title("答對題數與總分計算系統")
st.write(
    "為各組輕鬆計算答對題數與總分"
)
val1 = st.text_input("請輸入第1組的kahoot分數")
val2 = st.text_input("請輸入第2組的kahoot分數")
val3 = st.text_input("請輸入第3組的kahoot分數")
val4 = st.text_input("請輸入第4組的kahoot分數")
val5 = st.text_input("請輸入第5組的kahoot分數")
radio_btn1 = st.radio("請選擇第1組填充題答對題數",("0","1","2","3","4","5"))
radio_btn2 = st.radio("請選擇第2組填充題答對題數",("0","1","2","3","4","5"))
radio_btn3 = st.radio("請選擇第3組填充題答對題數",("0","1","2","3","4","5"))
radio_btn4 = st.radio("請選擇第4組填充題答對題數",("0","1","2","3","4","5"))
radio_btn5 = st.radio("請選擇第5組填充題答對題數",("0","1","2","3","4","5"))
st.divider()
st.subheader("各組總分")

# 計算各組總分
groups = [
    ("第1組", val1, radio_btn1),
    ("第2組", val2, radio_btn2),
    ("第3組", val3, radio_btn3),
    ("第4組", val4, radio_btn4),
    ("第5組", val5, radio_btn5),
]

for group_name, kahoot_score, fill_score in groups:
    try:
        if kahoot_score:
            kahoot_val = int(kahoot_score)  # 文字轉整數
            fill_val = int(fill_score)      # 文字轉整數
            total = fill_val * 900 + kahoot_val
            st.write(f"{group_name}: {fill_val} × 900 + {kahoot_val} = **{total}**")
        else:
            st.write(f"{group_name}: 請輸入kahoot分數")
    except ValueError:
        st.write(f"{group_name}: 請輸入有效的kahoot分數")
