"""
입력 출력 검색 수정 삭제 종료

"""

import pymysql
import pandas as pd

from sqlalchemy import create_engine, text
import pymysql


class phoneBook:

    # 공통
    def __init__(self):

        self.table = "phone_book"
        self.DBConn()
        self.df = pd.read_sql_table(self.table, con=self.engine)

    def DBConn(self):
        user = "root"
        password = "123456"
        host = "localhost"  # 보통 localhost 또는 127.0.0.1
        port = 3307  # 기본 포트 번호
        database = "phone_book_db"
        self.engine = create_engine(
            f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        )

    # 입력하기
    def insert2(self):
        print(f"{'입력하기':-^30}")

        input_name = input("이름 : ")
        input_phone = input("전화번호 : ")
        input_address = input("주소 : ")
        df_row = {
            "이름": input_name,
            "전화번호": input_phone,
            "주소": input_address,
        }
        self.df.loc[len(self.df)] = df_row
        self.df.to_sql(self.table, self.engine, if_exists="append", index=False)
        print("=" * 20)
        print("입력완료")
        print()

    # 출력하기
    def print2(self):

        print(f"{'출력하기':-^30}")
        print()
        print("=" * 30)
        # print_query = f"""
        # SELECT * FROM {self.table}1
        # """
        # with self.engine.connect() as connection:
        #     result = connection.execute(print_query)

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

                with self.engine.connect() as connection:
                    find_query = text("SELECT * FROM phone_book WHERE 이름 = :이름")
                    result = connection.execute(find_query, 이름=input_find)
                    rows = result.fetchall()

                    if rows:
                        for row in rows:
                            print(row)
                    else:
                        print("검색 결과가 없습니다")
                        break
                # 없으면 빈값을 나옴.
            except:
                print(f"검색 결과가 없습니다.")
                continue

            break

    # 수정하기
    def mod2(self):
        print(f"{'수정하기':-^30}")

        try:

            input_number = input("수정할 행의 번호 입력 : ")
            input_name = input("이름 : ")
            input_phone = input("전화번호 : ")
            input_address = input("주소 : ")
            df_row = {
                "번호": input_number,
                "이름": input_name,
                "전화번호": input_phone,
                "주소": input_address,
            }
            # 인덱스로 값 추가
            self.df.loc[len(self.df)] = df_row
            self.df.to_sql(self.table, self.engine, if_exists="append", index=False)
            print("=" * 20)
            print("입력완료")
            print()
            # 틀릴 시 오류 발생
        except Exception as e:
            print(f"잘못된 행 번호입니다. ")

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
