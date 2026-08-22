prompts = [
    {
        "title": "영어 학습 자료 만들기",
        "content": "중학생 영어 학습자를 위한 학습 자료를 만들어주세요.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "교육용 이미지 만들기",
        "content": "학생들이 이해하기 쉬운 교육용 이미지를 만들어주세요.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "영어 교사 페르소나",
        "content": "당신은 경험이 풍부한 영어 교사입니다. 학생의 수준에 맞게 친절하게 설명해주세요.",
        "category": "페르소나",
        "favorite": True
    }
]

def show_list():
    print("=== 프롬프트 목록 ===")

    for i, prompt in enumerate(prompts, start=1):
        star = "⭐" if prompt["favorite"] else ""
        print(f"{i}. [{prompt['category']}] {prompt['title']} {star}")

def show_menu():
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


while True:
    show_menu()

    choice = input("선택: ")

    if choice == "2":
        show_list()
    elif choice == "0":
        print("프로그램을 종료합니다.")
        break