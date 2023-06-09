import streamlit as st

st.set_page_config(
    page_title="선택과목 조사",
    page_icon='👍'
)
st.header('선택과목 선택')
학년 = st.selectbox("당신은 몇 학년 입니까?", ('선택', '2학년'))

if 학년 == '2학년':
    반 = st.selectbox("당신은 몇 반 입니까?", ('선택', '1반', '2반', '3반', '4반', '5반', '6반', '7반', '8반', '9반'))
    번호 = st.selectbox("당신은 몇 번 입니까?", ('선택', '1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번', '9번', '10번', '11번', '12번', '13번', '14번', '15번', '16번', '17번', '18번', '19번', '20번', '21번', '22번', '23번', '24번', '25번', '26번', '27번', '28번'))
    이름 = st.text_input('당신의 이름은 무엇인가요?', '')

    과목1 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '화학1', '생명과학1', '지구과학1'))

    if 과목1 == '물리학1':
        과목2 = st.selectbox("과목을 선택하십시오", ('선택','화학1', '생명과학1', '지구과학1'))
        if 과목2 == '화학1':
            과목3 = st.selectbox("과목을 선택하십시오", ('선택', '생명과학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목2 == '생명과학1':
            과목4 = st.selectbox("과목을 선택하십시오", ('선택', '화학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목2 == '지구과학1':
            과목5 = st.selectbox("과목을 선택하십시오", ('선택', '화학1', '생명과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')

    if 과목1 == '화학1':
        과목21 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '생명과학1', '지구과학1'))
        if 과목21 == '물리학1':
            과목31 = st.selectbox("과목을 선택하십시오", ('선택', '생명과학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목21 == '생명과학1':
            과목41 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목21 == '지구과학1':
            과목51 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '생명과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')

    if 과목1 == '생명과학1':
        과목22 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '화학1', '지구과학1'))
        if 과목22 == '물리학1':
            과목32 = st.selectbox("과목을 선택하십시오", ('선택', '화학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목22 == '화학1':
            과목42 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '지구과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목22 == '지구과학1':
            과목52 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '화학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')

    if 과목1 == '지구과학1':
        과목2 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '화학1', '생명과학1'))
        if 과목2 == '물리학1':
            과목3 = st.selectbox("과목을 선택하십시오", ('선택', '화학1', '생명과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목2 == '화학1':
            과목4 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '생명과학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')
        if 과목2 == '생명과학1':
            과목5 = st.selectbox("과목을 선택하십시오", ('선택', '물리학1', '화학1'))
            st.write('선택과목을 모두 선택하셨습니다')
            if st.button('제출'):
                st.write('제출되었습니다')









