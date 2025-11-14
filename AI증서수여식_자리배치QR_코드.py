import os
import streamlit as st
import pandas as pd

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(page_title="25년 2학기 AI서울테크 대학원 장학금 증서수여식 자리안내", page_icon="💺", layout="wide")


# -----------------------------
# 스타일
# -----------------------------
st.markdown("""
<style>
div[data-testid="stForm"] {
    background: #E7ECF7 !important;
    border: 1px solid #CAD6EC;
    border-radius: 12px;
    padding: 24px 20px;
    margin: 6px 0 24px 0;
}

.result-line{
  padding:12px 16px;border-radius:12px;
  background:#0b2536;color:#d8f1ff;border:1px solid #15394f;
  font-size:1.2rem;font-weight:600;margin-top:.0rem;
}
.seat-line{
  margin-top:10px;
  padding:10px 14px;border-radius:10px;
  background:#132b3a;color:#e6f4ff;border:1px solid #1a3a4e;
  font-size:1.2rem;font-weight:700;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# 학생 데이터 (여기에 네 리스트 전체 붙여넣기)
# -----------------------------
student_data_list = [
    {"name": "강범진", "course": "박사", "dob": "980404", "seat": "TA-1"},
    {"name": "강세일", "course": "박사", "dob": "970301", "seat": "TA-1"},
    {"name": "김규동", "course": "박사", "dob": "980406", "seat": "TA-1"},
    {"name": "김남준", "course": "박사", "dob": "950908", "seat": "TA-1"},
    {"name": "한우경", "course": "박사", "dob": "960727", "seat": "TA-2"},
    {"name": "김지원", "course": "석사", "dob": "000816", "seat": "TA-2"},
    {"name": "김동윤", "course": "석사", "dob": "010810", "seat": "TA-2"},
    {"name": "김덕건", "course": "박사", "dob": "980427", "seat": "TA-2"},
    {"name": "김다솔", "course": "박사", "dob": "940303", "seat": "TA-3"},
    {"name": "김도윤", "course": "박사", "dob": "950303", "seat": "TA-3"},
    {"name": "김도윤", "course": "박사", "dob": "951111", "seat": "TA-3"},
    {"name": "김동재", "course": "박사", "dob": "970223", "seat": "TA-3"},
    {"name": "김동희", "course": "박사", "dob": "960405", "seat": "TA-3"},
    {"name": "김미르", "course": "박사", "dob": "001123", "seat": "TA-3"},
    {"name": "김민선", "course": "박사", "dob": "000528", "seat": "TA-3"},
    {"name": "김민제", "course": "박사", "dob": "980912", "seat": "TA-3"},
    {"name": "김선민", "course": "박사", "dob": "990216", "seat": "TA-4"},
    {"name": "김승희", "course": "박사", "dob": "990110", "seat": "TA-4"},
    {"name": "김연수", "course": "박사", "dob": "990423", "seat": "TA-4"},
    {"name": "김용민", "course": "박사", "dob": "940927", "seat": "TA-4"},
    {"name": "김유원", "course": "박사", "dob": "970525", "seat": "TA-4"},
    {"name": "김응엽", "course": "박사", "dob": "930625", "seat": "TA-4"},
    {"name": "김제현", "course": "박사", "dob": "941010", "seat": "TA-4"},
    {"name": "김준혁", "course": "박사", "dob": "970729", "seat": "TA-4"},
    {"name": "김찬하", "course": "박사", "dob": "981011", "seat": "TA-5"},
    {"name": "김한영", "course": "박사", "dob": "960615", "seat": "TA-5"},
    {"name": "김현석", "course": "박사", "dob": "010321", "seat": "TA-5"},
    {"name": "남승태", "course": "박사", "dob": "940705", "seat": "TA-5"},
    {"name": "남형우", "course": "박사", "dob": "980430", "seat": "TA-5"},
    {"name": "노승영", "course": "박사", "dob": "981210", "seat": "TA-5"},
    {"name": "박보겸", "course": "박사", "dob": "990727", "seat": "TA-5"},
    {"name": "박석환", "course": "박사", "dob": "970616", "seat": "TA-5"},
    {"name": "박유현", "course": "박사", "dob": "950224", "seat": "TA-6"},
    {"name": "박진우", "course": "박사", "dob": "970913", "seat": "TA-6"},
    {"name": "박찬우", "course": "박사", "dob": "941203", "seat": "TA-6"},
    {"name": "박찬울", "course": "박사", "dob": "970827", "seat": "TA-6"},
    {"name": "박철훈", "course": "박사", "dob": "970416", "seat": "TA-6"},
    {"name": "박현지", "course": "박사", "dob": "991228", "seat": "TA-6"},
    {"name": "손민주", "course": "박사", "dob": "970512", "seat": "TA-6"},
    {"name": "송치현", "course": "박사", "dob": "980918", "seat": "TA-6"},
    {"name": "신호수", "course": "박사", "dob": "890103", "seat": "TA-7"},
    {"name": "안소정", "course": "박사", "dob": "950926", "seat": "TA-7"},
    {"name": "양요셉", "course": "박사", "dob": "970811", "seat": "TA-7"},
    {"name": "오세빈", "course": "박사", "dob": "000224", "seat": "TA-7"},
    {"name": "우승윤", "course": "박사", "dob": "960308", "seat": "TA-7"},
    {"name": "우승정", "course": "박사", "dob": "730710", "seat": "TA-7"},
    {"name": "유승욱", "course": "박사", "dob": "000128", "seat": "TA-7"},
    {"name": "윤예진", "course": "박사", "dob": "951016", "seat": "TA-7"},
    {"name": "이동엽", "course": "박사", "dob": "990706", "seat": "TA-8"},
    {"name": "이병원", "course": "박사", "dob": "960413", "seat": "TA-8"},
    {"name": "이소현", "course": "박사", "dob": "980515", "seat": "TA-8"},
    {"name": "이승민", "course": "박사", "dob": "010114", "seat": "TA-8"},
    {"name": "이우준", "course": "박사", "dob": "980216", "seat": "TA-8"},
    {"name": "이원석", "course": "박사", "dob": "981017", "seat": "TA-8"},
    {"name": "이정연", "course": "박사", "dob": "980402", "seat": "TA-8"},
    {"name": "이주호", "course": "박사", "dob": "001102", "seat": "TA-8"},
    {"name": "이진민", "course": "박사", "dob": "010212", "seat": "TA-9"},
    {"name": "이진호", "course": "박사", "dob": "940620", "seat": "TA-9"},
    {"name": "이태영", "course": "박사", "dob": "990415", "seat": "TA-9"},
    {"name": "이현정", "course": "박사", "dob": "750724", "seat": "TA-9"},
    {"name": "이호성", "course": "박사", "dob": "990205", "seat": "TA-9"},
    {"name": "장보아", "course": "박사", "dob": "970311", "seat": "TA-9"},
    {"name": "장영동", "course": "박사", "dob": "961124", "seat": "TA-9"},
    {"name": "장은비", "course": "박사", "dob": "010604", "seat": "TA-9"},
    {"name": "정서우", "course": "박사", "dob": "000221", "seat": "TA-10"},
    {"name": "정은희", "course": "박사", "dob": "991112", "seat": "TA-10"},
    {"name": "정지완", "course": "박사", "dob": "940207", "seat": "TA-10"},
    {"name": "조재은", "course": "박사", "dob": "001025", "seat": "TA-10"},
    {"name": "최소윤", "course": "박사", "dob": "971119", "seat": "TA-10"},
    {"name": "최인수", "course": "박사", "dob": "981029", "seat": "TA-10"},
    {"name": "최지웅", "course": "박사", "dob": "001026", "seat": "TA-10"},
    {"name": "추교빈", "course": "박사", "dob": "981216", "seat": "TA-10"},
    {"name": "하승운", "course": "박사", "dob": "970109", "seat": "TA-11"},
    {"name": "하지연", "course": "박사", "dob": "980913", "seat": "TA-11"},
    {"name": "한지헌", "course": "박사", "dob": "991224", "seat": "TA-11"},
    {"name": "허재혁", "course": "박사", "dob": "940223", "seat": "TA-11"},
    {"name": "황동준", "course": "박사", "dob": "990427", "seat": "TA-11"},
    {"name": "황인성", "course": "박사", "dob": "970725", "seat": "TA-11"},
]

df = pd.DataFrame(student_data_list)

# -----------------------------
# UI
# -----------------------------
st.markdown("""
<div style="
    background:#0A2540;
    padding:22px 16px;
    border-radius:12px;
    text-align:center;
    color:#FFFFFF;
    font-weight:700;
    font-size:1.35rem;
    margin-bottom:16px;
">
    🎓25-2학기 AI서울테크 증서수여식🎓<br>
    <span style="font-size:1.05rem; font-weight:500;">
        💺 장학생 자리배치 안내
    </span>
</div>
""", unsafe_allow_html=True)
st.caption("이름, 생년월일(6자리), 과정을 선택 후 버튼을 눌러주세요.")



with st.form(key="search_form"):
    name_input  = st.text_input("이름", placeholder="예: 홍길동")
    dob_input = st.text_input("생년월일 (6자리)", placeholder="예: 980101", max_chars=6)
    # ✅ 과정 선택을 생년월일 아래로 배치
    course_input = st.radio("과정", ("석사과정", "박사과정"), horizontal=True)
    submit_button = st.form_submit_button("🔎 내 자리 찾기")


# -----------------------------
# 검색 & 결과 표시
# -----------------------------
if submit_button:
    if not name_input or not dob_input:
        st.warning("이름과 생년월일을 모두 입력해주세요.")
    elif len(dob_input) != 6 or not dob_input.isdigit():
        st.warning("생년월일 6자리(YYMMDD)를 숫자로 정확히 입력해주세요.")
    else:
        result = df[
            (df["name"] == name_input.strip()) &
            (df["dob"] == dob_input.strip()) &
            (df["course"] == course_input)
        ]

        if result.empty:
            st.error("일치하는 정보를 찾을 수 없습니다. 이름, 생년월일, 과정을 다시 확인해주세요.")
        else:
            row = result.iloc[0]
            name   = row["name"]
            seat   = row["seat"]

            # ✅ 좌석은 텍스트로만
            st.markdown(f'<div class="seat-line">💺 배정된 좌석 : <b>{seat}</b></div>',
                        unsafe_allow_html=True)

            # 전체 좌석표
            st.markdown(
    "<h4 style='margin-top:28px; font-size:20px; font-weight:700;'>📌 전체 좌석표</h4>",
    unsafe_allow_html=True
)
            default_map_path = "AI증서수여식 다목적홀 도면도.png"  # 같은 폴더에 넣어두면 자동 표시
            if os.path.exists(default_map_path):
                st.image(default_map_path, use_column_width=True)
            else:
                up = st.file_uploader("좌석표 이미지를 업로드하세요 (PNG/JPG)", type=["png", "jpg", "jpeg"])
                if up is not None:
                    st.image(up, use_column_width=True)
                else:
                    st.info("앱 폴더에 `AI증서수여식 다목적홀 도면도.png`를 추가하거나 위에서 이미지를 업로드하면 전체 좌석표가 표시됩니다.")
