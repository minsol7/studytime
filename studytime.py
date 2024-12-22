import streamlit as st

# 고정된 과목 중요도 가중치
subject_weights = {
    '국어': 0.15, '수학': 0.15, '확통': 0.07, '영어': 0.15, 
    '탐구1': 0.12, '탐구2': 0.12, '탐구3': 0.12, '외국어': 0.12
}

# 제목
st.title('과목별 공부 비율 계산기')

# 등급과 선호도 입력 받기
grades = {}
preferences = {}
for subject in subject_weights.keys():
    grades[subject] = st.number_input(f'{subject} 등급 (0-10)', 0, 10)
    preferences[subject] = st.slider(f'{subject} 선호도 (1~5)', 1, 5)

# 등급 가중치 계산
total_grade = sum(grades.values())
grade_weights = {subject: grade / total_grade for subject, grade in grades.items()}

# 선호도 가중치 계산
total_preference = sum(preferences.values())
preference_weights = {subject: preference / total_preference for subject, preference in preferences.items()}

# 최종 가중치 계산
final_weights = {
    subject: subject_weights[subject] + grade_weights[subject] + preference_weights[subject]
    for subject in subject_weights.keys()
}

# 공부 비율 계산
total_weight = sum(final_weights.values())
study_percentage = {subject: (weight / total_weight) * 100 for subject, weight in final_weights.items()}

# 결과 출력
st.write('각 과목의 공부 비율은 다음과 같습니다:')
st.write(study_percentage)
