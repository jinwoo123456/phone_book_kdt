"""
입력 출력 검색 수정 삭제 종료

"""

import pandas as pd


class phoneBook:

    # 공통
    def __init__(self):
        self.df = pd.DataFrame(columns=["번호", "이름", "전화번호", "주소"])
        self.cnt = 0

    # 입력하기
    def insert2(self):

        self.cnt += 1
        print(f"{'입력하기':-^30}")

        input_name = input("이름 : ")
        input_phone = input("전화번호 : ")
        input_address = input("주소 : ")
        df_row = {
            "번호": self.cnt,
            "이름": input_name,
            "전화번호": input_phone,
            "주소": input_address,
        }
        # 인덱스로 값 추가
        self.df.loc[len(self.df)] = df_row
        print("=" * 20)
        print("입력완료")
        print()

    # 출력하기
    def print2(self):

        print(f"{'출력하기':-^30}")
        print()
        print("=" * 30)
        print(self.df)  # 전체 출력
        print("=" * 30)
        print()

    # 검색하기
    def find2(self):
        print(f"{'검색하기':-^30}")
        cnt = 0
        while True:
            cnt += 1
            # 틀린횟수제한
            if cnt > 3:
                print("그만 검색하세요. 메뉴로 돌아갑니다.")
                break

            try:
                print()
                input_find = input("찾을 이름 입력 : ")
                print()

                print(self.df[self.df["이름"] == input_find])  # 없으면 빈값을 나옴.
            except:
                print(f"검색 결과가 없습니다.")
                continue

            break

    # 수정하기
    def mod2(self):
        print(f"{'수정하기':-^30}")
        cnt = 0
        while True:
            cnt += 1
            # 틀린횟수제한
            if cnt > 3:
                print("그만 틀리세요. 메뉴로 돌아갑니다.")
                break
            try:
                input_mod = int(input("수정할 행 번호 선택 : "))
                input_name = input("수정할 이름 : ")
                input_phone = input("수정할 전화번호 : ")
                input_address = input("수정할 주소 : ")
                # 행번호를 인덱스 +1로 만들었기 때문에 -1을 해줘야함.
                self.df.iloc[input_mod - 1, 1] = input_name
                self.df.iloc[input_mod - 1, 2] = input_phone
                self.df.iloc[input_mod - 1, 3] = input_address
                print("=" * 20)
                print("수정완료")
                print()
            # 틀릴 시 오류 발생
            except Exception as e:
                print(f"잘못된 행 번호입니다. 다시 입력해주세요.")
                continue
            break

    def del2(self):
        print(f"{'삭제하기':-^30}")
        cnt = 0
        while True:
            cnt += 1
            # 틀린횟수제한
            if cnt > 3:
                print("그만 틀리세요. 메뉴로 돌아갑니다.")
                break
            try:
                input_del = int(input("삭제할 행 번호 선택 : "))
                # 인덱스 행기준으로 삭제
                self.df.drop(input_del - 1, axis=0, inplace=True)
            except Exception as e:
                print(f"잘못된 행 번호입니다. 다시 입력해주세요.")
                continue
            break


if __name__ == "__main__":
    # 인스턴스
    phonebook = phoneBook()

    # 터미널에 출력될것
    while True:
        # 공통
        print("1.입력  2.출력  3.검색  4.수정  5.삭제  6.종료\n")
        print()
        user_input = input("선택 : ")

        # 입력
        if user_input == "1":
            phonebook.insert2()
        # 출력
        elif user_input == "2":
            phonebook.print2()
        # 검색
        elif user_input == "3":
            phonebook.find2()
        # 수정
        elif user_input == "4":
            phonebook.mod2()
        # 삭제
        elif user_input == "5":
            phonebook.del2()
        # 종료
        elif user_input == "6":
            break
