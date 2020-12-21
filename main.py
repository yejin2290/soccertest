import Pannel
import stat_players
import calcul_score
import make_excel


def main():
    # team_list와 team_list_eng에 언어 버전 팀 리스트 할당
    team_list = ["웨스트햄", "레스터시티" , "리버풀" , "맨시티", "맨유", "에버튼", "아스날",  "첼시", "토트넘", "사우스햄튼"]
    team_list_eng = ["west ham united", "leicester city", "liverpool", "manchester city", "manchester united", "everton", "arsenal", "chelsea", "tottenham hotspur", "southampton"]
    # result_dict은 최종 팀과 선수 스탯을 저장하기 위한 dictionary
    result_dict = {}
    print("팀을 선택해주세요(번호만 입력):")
    while True:
        # try exception 구문을 활용하여 사용자가 팀 선택, 능력치 할당 방법의 입력을 제어함.
        try:
            select_1 = int(input("첫번째 팀: 0.웨스트햄, 1. 레스터시티, 2.리버풀, 3.맨시티, 4.맨유, 5.에버튼, 6.아스날,  7.첼시, 8.토트넘, 9.사우스햄튼 : "))
            select_2 = int(input("두번째 팀: 0.웨스트햄, 1. 레스터시티, 2.리버풀, 3.맨시티, 4.맨유, 5.에버튼, 6.아스날,  7.첼시, 8.토트넘, 9.사우스햄튼 : "))
            print("stat 설정 방식을 정하겠습니다. 다음 보기 중 번호만 입력해주세요")
            select_1_mode = input("첫번 째 팀 선수들의 스탯을 어떻게 정하시겠습니까? 1.랜덤, 2. 피파 게임 기반: ")
            select_2_mode = input("두번 째 팀 선수들의 스탯을 어떻게 정하시겠습니까? 1.랜덤, 2. 피파 게임 기반: ")
            if (select_1 < 0 or select_1 > 9) or (select_2 < 0 or select_2 > 9):
                print("0부터 9번까지의 팀을 입력하셔야 합니다.")
                continue
            elif ((select_1_mode != '1' and select_1_mode != '2') or (select_2_mode != '1' and select_2_mode != '2')):
                print("능력치 선정은 1번이나 2번을 입력해야 합니다.")
                continue
            else:
                pannel = Pannel.Pannel()
                # 첫 번째 팀 랜덤 or 오토로 능력치 할당. 랜덤일때는 stat_players.py의 set_start_random 호출/ 오토일때는 set_start_auto 호출
                if select_1_mode == '1':
                    # team_stat_1과 team_stat_2에는 스탯이 할당됨(ex. p_name, p_position, stat_dict)
                    team_stat_1 = stat_players.set_start_random(team_list[select_1])
                else:
                    team_stat_1 = stat_players.set_start_auto(team_list[select_1])
                # 두 번째 팀 역시 첫 번째 팀과 같은 방식으로 설정
                if select_2_mode == '1':
                    team_stat_2 = stat_players.set_start_random(team_list[select_2])
                else:
                    team_stat_2 = stat_players.set_start_auto(team_list[select_2])
                print("stat 설정 완료")

                # calcul_score.py에 team_stat_1과 team_stat_2을 매개 변수로 넘겨 경기 결과를 예측
                calcul = calcul_score.Calculate(team_stat_1,
                                                team_stat_2)
                # calcul.py의 get_result 호출. get_result()는 슈팅, 점유율, 패스르 계산함.
                result_dict = calcul.get_result()

                # make_excel.py를 통해 결과를 엑셀에 쓰기. 엑셀은 바로 Open함.
                to_make_excel = make_excel.Make_Excel(team_list_eng[select_1], team_list_eng[select_2], result_dict)
                excel = to_make_excel.start()
                excel.Visible = True
                # Pannel에 결과가 담겨있는 result_dict을 넘김. 이 결과는 pygame을 통해 그림형식으로 오픈됨.
                pannel.initGame(team_list[select_1], team_list[select_2])
                pannel.runGame(result_dict)
                # pannel 종료 시 excel파일도 닫음
                excel.quit()
                break
        # 오류 제어 부분
        except Exception as e:
            print("주어진 명령대로 프로그램을 실행시켜주세요: ", e)
            continue
        finally:
            if input("다시 시작하려면 0, 끝내려면 아무키나 입력해주세요: ") == '0':
                continue
            else:
                print("끝내겠습니다!!", end=" ")
                return


main(