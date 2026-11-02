import os

# 출석 데이터를 저장할 파일 이름
FILENAME = "attendance.txt"

def check_attendance(date, name):
    """날짜와 이름을 받아 파일에 추가(append)로 기록한다."""
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write(f"{date}, {name}\n")

def show_list():
    """저장된 출석 명단을 보여준다."""
    if not os.path.exists(FILENAME):
        print("기록된 출석 명단이 없습니다.")
        return
    with open(FILENAME, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if not lines:
        print("기록된 출석 명단이 없습니다.")
        return
    for line in lines:
        print(line.strip())

def main():
    while True:
        print("\n--- 스터디 출석 관리 프로그램 ---")
        print("1. 출석 체크 (날짜와 이름 입력)")
        print("2. 출석 명단 보기")
        print("3. 종료")

        choice = input("원하는 메뉴 번호를 선택하세요: ")

        if choice == '1':
            date = input("날짜를 입력하세요 (예: 2023-10-27): ")
            name = input("이름을 입력하세요: ")
            check_attendance(date, name)
            print(f"✅ {name}님의 출석이 기록되었습니다.")
        elif choice == '2':
            print("\n--- 현재까지의 출석 명단 ---")
            show_list()
        elif choice == '3':
            print("프로그램을 종료합니다. 열공하세요!")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해 주세요.")

if __name__ == "__main__":
    main()