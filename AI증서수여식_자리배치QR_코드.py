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
# 학생 데이터
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
    {"name": "강동화", "course": "석사", "dob": "961016", "seat": "A-1"},
    {"name": "강병준", "course": "석사", "dob": "990817", "seat": "A-2"},
    {"name": "강세영", "course": "석사", "dob": "021224", "seat": "A-3"},
    {"name": "구동현", "course": "석사", "dob": "010110", "seat": "A-4"},
    {"name": "권다훈", "course": "석사", "dob": "021103", "seat": "A-5"},
    {"name": "권도혁", "course": "석사", "dob": "990625", "seat": "A-6"},
    {"name": "권예진", "course": "석사", "dob": "000623", "seat": "A-7"},
    {"name": "김건호", "course": "석사", "dob": "020910", "seat": "A-8"},
    {"name": "김경훈", "course": "석사", "dob": "980330", "seat": "A-9"},
    {"name": "김기원", "course": "석사", "dob": "010612", "seat": "A-10"},
    {"name": "김다솔", "course": "석사", "dob": "980425", "seat": "A-11"},
    {"name": "김미연", "course": "석사", "dob": "940330", "seat": "A-12"},
    {"name": "김성민", "course": "석사", "dob": "980726", "seat": "A-13"},
    {"name": "김시우", "course": "석사", "dob": "990817", "seat": "A-14"},
    {"name": "김예란", "course": "석사", "dob": "000812", "seat": "A-15"},
    {"name": "김예진", "course": "석사", "dob": "010206", "seat": "A-16"},
    {"name": "김예찬", "course": "석사", "dob": "000629", "seat": "A-17"},
    {"name": "김용진", "course": "석사", "dob": "970425", "seat": "A-18"},
    {"name": "김용훈", "course": "석사", "dob": "990227", "seat": "A-19"},
    {"name": "김윤진", "course": "석사", "dob": "010629", "seat": "A-20"},
    {"name": "김은지", "course": "석사", "dob": "000606", "seat": "A-21"},
    {"name": "김이레", "course": "석사", "dob": "011214", "seat": "A-22"},
    {"name": "김이현", "course": "석사", "dob": "000502", "seat": "A-23"},
    {"name": "김재승", "course": "석사", "dob": "980506", "seat": "A-24"},
    {"name": "김지은", "course": "석사", "dob": "020705", "seat": "A-25"},
    {"name": "김지은", "course": "석사", "dob": "010430", "seat": "A-26"},
    {"name": "김지훈", "course": "석사", "dob": "981007", "seat": "A-27"},
    {"name": "김진호", "course": "석사", "dob": "001221", "seat": "A-28"},
    {"name": "김태현", "course": "석사", "dob": "001111", "seat": "A-29"},
    {"name": "김혁수", "course": "석사", "dob": "991009", "seat": "A-30"},
    {"name": "김혜진", "course": "석사", "dob": "000921", "seat": "B-1"},
    {"name": "두하영", "course": "석사", "dob": "001205", "seat": "B-2"},
    {"name": "류한율", "course": "석사", "dob": "980817", "seat": "B-3"},
    {"name": "문다은", "course": "석사", "dob": "010403", "seat": "B-4"},
    {"name": "민경준", "course": "석사", "dob": "000811", "seat": "B-5"},
    {"name": "박규태", "course": "석사", "dob": "001209", "seat": "B-6"},
    {"name": "박민영", "course": "석사", "dob": "010720", "seat": "B-7"},
    {"name": "박상은", "course": "석사", "dob": "030219", "seat": "B-8"},
    {"name": "박선현", "course": "석사", "dob": "021219", "seat": "B-9"},
    {"name": "박성균", "course": "석사", "dob": "990408", "seat": "B-10"},
    {"name": "박승운", "course": "석사", "dob": "990614", "seat": "B-11"},
    {"name": "박시언", "course": "석사", "dob": "000318", "seat": "B-12"},
    {"name": "박은섭", "course": "석사", "dob": "001106", "seat": "B-13"},
    {"name": "박찬호", "course": "석사", "dob": "000121", "seat": "B-14"},
    {"name": "박채린", "course": "석사", "dob": "001211", "seat": "B-15"},
    {"name": "박채림", "course": "석사", "dob": "980626", "seat": "B-16"},
    {"name": "박채원", "course": "석사", "dob": "020208", "seat": "B-17"},
    {"name": "박형동", "course": "석사", "dob": "990526", "seat": "B-18"},
    {"name": "박황선", "course": "석사", "dob": "980421", "seat": "B-19"},
    {"name": "방지민", "course": "석사", "dob": "020725", "seat": "B-20"},
    {"name": "배성은", "course": "석사", "dob": "000928", "seat": "B-21"},
    {"name": "변진모", "course": "석사", "dob": "000502", "seat": "B-22"},
    {"name": "석혜원", "course": "석사", "dob": "010719", "seat": "B-23"},
    {"name": "성백륜", "course": "석사", "dob": "970802", "seat": "B-24"},
    {"name": "성시열", "course": "석사", "dob": "991005", "seat": "B-25"},
    {"name": "성재이", "course": "석사", "dob": "980709", "seat": "B-26"},
    {"name": "손가영", "course": "석사", "dob": "010227", "seat": "B-27"},
    {"name": "손서영", "course": "석사", "dob": "011222", "seat": "B-28"},
    {"name": "손수경", "course": "석사", "dob": "010807", "seat": "B-29"},
    {"name": "손예진", "course": "석사", "dob": "990101", "seat": "B-30"},
    {"name": "손재희", "course": "석사", "dob": "020421", "seat": "C-1"},
    {"name": "신민용", "course": "석사", "dob": "010224", "seat": "C-2"},
    {"name": "신서영", "course": "석사", "dob": "021017", "seat": "C-3"},
    {"name": "신수현", "course": "석사", "dob": "010217", "seat": "C-4"},
    {"name": "신예원", "course": "석사", "dob": "021031", "seat": "C-5"},
    {"name": "심예린", "course": "석사", "dob": "000425", "seat": "C-6"},
    {"name": "안학서", "course": "석사", "dob": "010911", "seat": "C-7"},
    {"name": "양시현", "course": "석사", "dob": "020119", "seat": "C-8"},
    {"name": "양재혁", "course": "석사", "dob": "001108", "seat": "C-9"},
    {"name": "양지웅", "course": "석사", "dob": "990412", "seat": "C-10"},
    {"name": "오승은", "course": "석사", "dob": "010831", "seat": "C-11"},
    {"name": "오주선", "course": "석사", "dob": "000509", "seat": "C-12"},
    {"name": "우나륜", "course": "석사", "dob": "031028", "seat": "C-13"},
    {"name": "원민재", "course": "석사", "dob": "011006", "seat": "C-14"},
    {"name": "유다나", "course": "석사", "dob": "020405", "seat": "C-15"},
    {"name": "유미진", "course": "석사", "dob": "020214", "seat": "C-16"},
    {"name": "유현준", "course": "석사", "dob": "000621", "seat": "C-17"},
    {"name": "윤다빈", "course": "석사", "dob": "020727", "seat": "C-18"},
    {"name": "윤소영", "course": "석사", "dob": "030927", "seat": "C-19"},
    {"name": "윤효의", "course": "석사", "dob": "011122", "seat": "C-20"},
    {"name": "이강준", "course": "석사", "dob": "000409", "seat": "C-21"},
    {"name": "이건우", "course": "석사", "dob": "001011", "seat": "C-22"},
    {"name": "이경렬", "course": "석사", "dob": "010930", "seat": "C-23"},
    {"name": "이다예", "course": "석사", "dob": "030131", "seat": "C-24"},
    {"name": "이도현", "course": "석사", "dob": "010106", "seat": "C-25"},
    {"name": "이동훈", "course": "석사", "dob": "991126", "seat": "C-26"},
    {"name": "이민서", "course": "석사", "dob": "030318", "seat": "C-27"},
    {"name": "이세빈", "course": "석사", "dob": "990109", "seat": "C-28"},
    {"name": "이수인", "course": "석사", "dob": "010303", "seat": "D-1"},
    {"name": "이승재", "course": "석사", "dob": "990811", "seat": "D-2"},
    {"name": "이승한", "course": "석사", "dob": "980411", "seat": "D-3"},
    {"name": "이신행", "course": "석사", "dob": "980922", "seat": "D-4"},
    {"name": "이재인", "course": "석사", "dob": "030825", "seat": "D-5"},
    {"name": "이정민", "course": "석사", "dob": "990730", "seat": "D-6"},
    {"name": "이지석", "course": "석사", "dob": "030828", "seat": "D-7"},
    {"name": "이지운", "course": "석사", "dob": "000127", "seat": "D-8"},
    {"name": "이철우", "course": "석사", "dob": "990528", "seat": "D-9"},
    {"name": "이태호", "course": "석사", "dob": "990117", "seat": "D-10"},
    {"name": "이혜성", "course": "석사", "dob": "960917", "seat": "D-11"},
    {"name": "이효준", "course": "석사", "dob": "990507", "seat": "D-12"},
    {"name": "임건호", "course": "석사", "dob": "981107", "seat": "D-13"},
    {"name": "임지인", "course": "석사", "dob": "011022", "seat": "D-14"},
    {"name": "장유림", "course": "석사", "dob": "000812", "seat": "D-15"},
    {"name": "장진우", "course": "석사", "dob": "000710", "seat": "D-16"},
    {"name": "장하나", "course": "석사", "dob": "001004", "seat": "D-17"},
    {"name": "전민서", "course": "석사", "dob": "000103", "seat": "D-18"},
    {"name": "전희정", "course": "석사", "dob": "010216", "seat": "D-19"},
    {"name": "정강현", "course": "석사", "dob": "011205", "seat": "D-20"},
    {"name": "정호경", "course": "석사", "dob": "020608", "seat": "D-21"},
    {"name": "정환희", "course": "석사", "dob": "000325", "seat": "D-22"},
    {"name": "조건희", "course": "석사", "dob": "000927", "seat": "D-23"},
    {"name": "조금주", "course": "석사", "dob": "980630", "seat": "D-24"},
    {"name": "조찬영", "course": "석사", "dob": "020220", "seat": "D-25"},
    {"name": "주다윤", "course": "석사", "dob": "020707", "seat": "D-26"},
    {"name": "주세진", "course": "석사", "dob": "010203", "seat": "D-27"},
    {"name": "주영석", "course": "석사", "dob": "991015", "seat": "D-28"},
    {"name": "지현빈", "course": "석사", "dob": "000211", "seat": "E-1"},
    {"name": "차수빈", "course": "석사", "dob": "020123", "seat": "E-2"},
    {"name": "차승언", "course": "석사", "dob": "001127", "seat": "E-3"},
    {"name": "차승주", "course": "석사", "dob": "990201", "seat": "E-4"},
    {"name": "최린", "course": "석사", "dob": "010126", "seat": "E-5"},
    {"name": "최예진", "course": "석사", "dob": "040222", "seat": "E-6"},
    {"name": "최이슬", "course": "석사", "dob": "011227", "seat": "E-7"},
    {"name": "최재민", "course": "석사", "dob": "000225", "seat": "E-8"},
    {"name": "최하람", "course": "석사", "dob": "021113", "seat": "E-9"},
    {"name": "표주은", "course": "석사", "dob": "010309", "seat": "E-10"},
    {"name": "허동욱", "course": "석사", "dob": "950617", "seat": "E-11"},
    {"name": "황지원", "course": "석사", "dob": "980821", "seat": "E-12"},
    {"name": "강주헌", "course": "석사", "dob": "990218", "seat": "E-13"},
    {"name": "강택현", "course": "석사", "dob": "990902", "seat": "E-14"},
    {"name": "권윤형", "course": "석사", "dob": "970910", "seat": "E-15"},
    {"name": "김민서", "course": "석사", "dob": "000409", "seat": "E-16"},
    {"name": "김민섭", "course": "석사", "dob": "000305", "seat": "E-17"},
    {"name": "김민주", "course": "석사", "dob": "011213", "seat": "E-18"},
    {"name": "김병민", "course": "석사", "dob": "970520", "seat": "E-19"},
    {"name": "김진우", "course": "석사", "dob": "960929", "seat": "E-20"},
    {"name": "류보곤", "course": "석사", "dob": "981023", "seat": "E-21"},
    {"name": "박나은", "course": "석사", "dob": "030114", "seat": "E-22"},
    {"name": "박민영", "course": "석사", "dob": "010918", "seat": "E-23"},
    {"name": "박수빈", "course": "석사", "dob": "011219", "seat": "E-24"},
    {"name": "박준영", "course": "석사", "dob": "000502", "seat": "E-25"},
    {"name": "박지석", "course": "석사", "dob": "000916", "seat": "E-26"},
    {"name": "최한준", "course": "석사", "dob": "000420", "seat": "E-27"},
    {"name": "박창현", "course": "석사", "dob": "991121", "seat": "E-28"},
    {"name": "박채원", "course": "석사", "dob": "990220", "seat": "F-1"},
    {"name": "박하린", "course": "석사", "dob": "020429", "seat": "F-2"},
    {"name": "배수현", "course": "석사", "dob": "990525", "seat": "F-3"},
    {"name": "최준서", "course": "석사", "dob": "010126", "seat": "F-4"},
    {"name": "백도윤", "course": "석사", "dob": "991031", "seat": "F-5"},
    {"name": "백승호", "course": "석사", "dob": "980325", "seat": "F-6"},
    {"name": "서수연", "course": "석사", "dob": "020327", "seat": "F-7"},
    {"name": "서준영", "course": "석사", "dob": "990921", "seat": "F-8"},
    {"name": "소예림", "course": "석사", "dob": "000514", "seat": "F-9"},
    {"name": "송원준", "course": "석사", "dob": "000428", "seat": "F-10"},
    {"name": "신동석", "course": "석사", "dob": "991217", "seat": "F-11"},
    {"name": "안가영", "course": "석사", "dob": "020924", "seat": "F-12"},
    {"name": "유서현", "course": "석사", "dob": "010924", "seat": "F-13"},
    {"name": "이경주", "course": "석사", "dob": "011218", "seat": "F-14"},
    {"name": "이도현", "course": "석사", "dob": "000414", "seat": "F-15"},
    {"name": "이동욱", "course": "석사", "dob": "981028", "seat": "F-16"},
    {"name": "이우경", "course": "석사", "dob": "011126", "seat": "F-17"},
    {"name": "최하현", "course": "석사", "dob": "990610", "seat": "F-18"},
    {"name": "이은규", "course": "석사", "dob": "000407", "seat": "F-19"},
    {"name": "이은세", "course": "석사", "dob": "020912", "seat": "F-20"},
    {"name": "이재성", "course": "석사", "dob": "951030", "seat": "F-21"},
    {"name": "이진권", "course": "석사", "dob": "980613", "seat": "F-22"},
    {"name": "이채린", "course": "석사", "dob": "011112", "seat": "F-23"},
    {"name": "이체영", "course": "석사", "dob": "020211", "seat": "F-24"},
    {"name": "임규일", "course": "석사", "dob": "010107", "seat": "F-25"},
    {"name": "임채연", "course": "석사", "dob": "011112", "seat": "F-26"},
    {"name": "임하은", "course": "석사", "dob": "020225", "seat": "G-1"},
    {"name": "최장호", "course": "석사", "dob": "991009", "seat": "G-2"},
    {"name": "전현민", "course": "석사", "dob": "010215", "seat": "G-3"},
    {"name": "정다현", "course": "석사", "dob": "000919", "seat": "G-4"},
    {"name": "정서영", "course": "석사", "dob": "020826", "seat": "G-5"},
    {"name": "정윤아", "course": "석사", "dob": "001024", "seat": "G-6"},
    {"name": "정태성", "course": "석사", "dob": "990320", "seat": "G-7"},
    {"name": "조대호", "course": "석사", "dob": "990527", "seat": "G-8"},
    {"name": "채영재", "course": "석사", "dob": "250224", "seat": "G-9"},
    {"name": "최영", "course": "석사", "dob": "000714", "seat": "G-10"},
    {"name": "전동윤", "course": "석사", "dob": "980828", "seat": "G-11"},
    {"name": "이원정", "course": "석사", "dob": "990507", "seat": "G-12"},
    {"name": "배진성", "course": "석사", "dob": "000217", "seat": "G-13"},
    {"name": "박지안", "course": "석사", "dob": "000801", "seat": "G-14"}
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
    name_input = st.text_input("이름", placeholder="예: 홍길동")
    dob_input = st.text_input("생년월일 (6자리)", placeholder="예: 980101", max_chars=6)
    course_input = st.radio("과정", ("석사과정", "박사과정"), horizontal=True)
    submit_button = st.form_submit_button("🔎 내 자리 찾기")


# -----------------------------
# 검색 & 결과 표시
# -----------------------------
if submit_button:
    # 입력값 전처리
    name_input = name_input.strip().lower()
    dob_input = dob_input.strip().lower()

    # 유효성 검사
    if not name_input or not dob_input:
        st.warning("이름과 생년월일을 모두 입력해주세요.")
    elif len(dob_input) != 6 or not dob_input.isdigit():
        st.warning("생년월일 6자리(YYMMDD)를 숫자로 정확히 입력해주세요.")
    else:
        # 데이터프레임에서 검색
        result = df[
            (df["name"].str.strip().str.lower() == name_input) &
            (df["dob"].str.strip().str.lower() == dob_input) &
            (df["course"].str.strip().str.lower() == course_input[:2].lower())
        ]

        if result.empty:
            st.error("일치하는 정보를 찾을 수 없습니다. 이름, 생년월일, 과정을 다시 확인해주세요.")
        else:
            row = result.iloc[0]
            name = row["name"]
            seat = row["seat"]

            st.markdown(f'<div class="seat-line">💺 배정된 좌석 : <b>{seat}</b></div>', unsafe_allow_html=True)

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

