import random

class Calculate:
    def __init__(self, team_stat_1, team_stat_2):
        self.team_stat_1 = team_stat_1
        self.team_stat_2 = team_stat_2
        self.team_1_sum_dict = {"패스" : 0, "슈팅": 0, "드리블": 0, "주력": 0, "수비": 0, "체력": 0}
        self.team_2_sum_dict = {"패스" : 0, "슈팅": 0, "드리블": 0, "주력": 0, "수비": 0, "체력": 0}
        self.team_1_GK = 0
        self.team_2_GK = 0
        self.result_dict = {}

    # 각 선수들의 능력치들을 같은 능력치대로 합하는 메소드. 합한 능력치들로 결과를 도출시키기 위함.
    def caclulate_sum(self):
        for i in self.team_stat_1:
            if i.p_position != 'GK':
                self.team_1_sum_dict["패스"] = self.team_1_sum_dict["패스"] + i.stat_dict["패스"]
                self.team_1_sum_dict["슈팅"] = self.team_1_sum_dict["슈팅"] + i.stat_dict["슈팅"]
                self.team_1_sum_dict["드리블"] = self.team_1_sum_dict["드리블"] + i.stat_dict["드리블"]
                self.team_1_sum_dict["주력"] = self.team_1_sum_dict["주력"] + i.stat_dict["주력"]
                self.team_1_sum_dict["수비"] = self.team_1_sum_dict["수비"] + i.stat_dict["수비"]
                self.team_1_sum_dict["체력"] = self.team_1_sum_dict["체력"] + i.stat_dict["체력"]
            else:
                self.team_1_GK = i.stat_dict['반사신경'] +i.stat_dict['볼 핸들링'] + i.stat_dict['골킾'] + i.stat_dict['공중볼'] + \
                                 i.stat_dict['수비조율'] + i.stat_dict['공던지기']
        for i in self.team_stat_2:
            if i.p_position != 'GK':
                self.team_2_sum_dict["패스"] = self.team_2_sum_dict["패스"] + i.stat_dict["패스"]
                self.team_2_sum_dict["슈팅"] = self.team_2_sum_dict["슈팅"] + i.stat_dict["슈팅"]
                self.team_2_sum_dict["드리블"] = self.team_2_sum_dict["드리블"] + i.stat_dict["드리블"]
                self.team_2_sum_dict["주력"] = self.team_2_sum_dict["주력"] + i.stat_dict["주력"]
                self.team_2_sum_dict["수비"] = self.team_2_sum_dict["수비"] + i.stat_dict["수비"]
                self.team_2_sum_dict["체력"] = self.team_2_sum_dict["체력"] + i.stat_dict["체력"]
            else:
                self.team_2_GK = i.stat_dict['반사신경'] + i.stat_dict['볼 핸들링'] + i.stat_dict['골킾'] + i.stat_dict['공중볼'] + \
                                 i.stat_dict['수비조율'] + i.stat_dict['공던지기']

    # 합한 능력치 따라 선방 횟수와 유효 공격 포인트, 골 넣는 횟수를 구하는 메소드
    def calculate_shoot(self):
        team_1_attack = int((self.team_1_sum_dict["슈팅"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] + self.team_1_sum_dict["주력"] +self.team_1_sum_dict["체력"])/5)
        team_2_defense = int((self.team_2_sum_dict["수비"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] + self.team_2_sum_dict["주력"] +self.team_2_sum_dict["체력"])/5)
        team_2_attack = int((self.team_2_sum_dict["슈팅"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] +
                             self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"]) / 5)
        team_1_defense = int((self.team_1_sum_dict["수비"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] +
                              self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"]) / 5)

        print("team_1의 공격 값: %.3f" % team_1_attack)
        print("team_2의 공격 값: %.3f" % team_2_attack)
        print("team_1의 수비 값(골키퍼 제외): %.3f" % team_1_defense)
        print("team_2의 수비 값(골키퍼 제외): %.3f" % team_2_defense)
        print("team_1의 GK: %.3f" % self.team_1_GK)
        print("team_2의 GK: %.3f" % self.team_1_GK)

        save_count = 0
        goal_team_1 = 0
        goal_team_2 = 0
        save_team_1 = 0
        save_team_2 = 0

        # team1의 공격에 관한 것.
        for i in range(0, 100):
            attck_range = random.randrange(0, team_1_attack)
            defense_range = random.randrange(0, team_2_defense)
            if attck_range <= defense_range:
                save_count = save_count + 1
            else:
                # 선수들의 평균 슈팅을 GK의 합으로 나눈다음 100을 곱하면 골을 넣을 확률이 됨. 여기다가 다시 100을 넣어서 range(0, 100)과 비교
                # 수비력에 대한 슈팅 percentage
                shoot_range = int(((self.team_1_sum_dict["슈팅"]/10) / (self.team_2_sum_dict["수비"]/10 )) * 100 )
                if random.randrange(0, int(shoot_range)) >= random.randrange(0, self.team_2_GK):
                    goal_team_1 = goal_team_1 + 1
                else:
                    save_team_2 = save_team_2 + 1
                if goal_team_1 >= 10:
                    i = 0
                    goal_team_1 = 0
                    save_count = 0
                    continue

        shoot_count_1 = save_count - goal_team_1
        if shoot_count_1 > 0:
            shoot_count_1 = random.randrange(goal_team_1, shoot_count_1)
        else:
            shoot_count_1 = random.randrange(save_count, goal_team_1)

        save_count = 0
        # team2의 공격에 관한 것
        for i in range(0, 100):
            attck_range = random.randrange(0, team_2_attack)
            defense_range = random.randrange(0, team_1_defense)
            if attck_range <= defense_range:
                save_count = save_count + 1
            else:
                # 선수들의 평균 슈팅을 GK의 합으로 나눈다음 100을 곱하면 골을 넣을 확률이 됨. 여기다가 다시 100을 넣어서 range(0, 100)과 비교
                # 수비력에 대한 슈팅 percentage
                # if random.randrange(0, attck_range) >= random.randrange(0, defense_range):
                # shoot_count = shoot_count + 1
                shoot_range = int(((self.team_2_sum_dict["슈팅"] / 10) / (self.team_1_sum_dict["수비"] / 10)) * 100)
                if random.randrange(0, int(shoot_range)) >= random.randrange(0, self.team_1_GK):
                    goal_team_2 = goal_team_2 + 1
                else:
                    save_team_1 = save_team_1 + 1
                if goal_team_2 >= 10 :
                    i = 0
                    goal_team_2 = 0
                    save_count = 0
                    continue
        shoot_count_2 = save_count - goal_team_2
        if shoot_count_2 > 0:
            shoot_count_2 = random.randrange(goal_team_2, shoot_count_2)
        else:
            shoot_count_2 = random.randrange(save_count, goal_team_2)
        print("save_count %d " %save_count)
        print("TEAM1 goal, TEAM2save %d %d" %((goal_team_1), (save_team_2)))
        print("TEAM2 goal, TEAM1save %d %d" % ((goal_team_2), (save_team_1)))

        self.result_dict["goal"] = [str(goal_team_1), str(goal_team_2)]
        self.result_dict["save"] = [str(save_team_1), str(save_team_2)]
        self.result_dict["shoot"] = [str(shoot_count_1), str(shoot_count_2)]
        #이 부분이 중요. 결국에 calcul에서도 통합한 반환 값이 필요함 ex)딕셔너리. 그래야 pannel에 매개하기가 수월함.
        #공격수가 수비를 뚫을 것을 랜덤으로 구하고, 뚫고 나서는 슈팅의 평균치와 GK의 값으로 확률을 또 구함.

    def calculate_possesion(self):
        team_1_sum = int((self.team_1_sum_dict["슈팅"] + self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] +
                             self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"] + self.team_1_sum_dict["수비"]) / 6)
        team_2_sum = int((self.team_2_sum_dict["수비"] + self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] +
                              self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"] + self.team_2_sum_dict["슈팅"]) / 6)

        possession_team_1 = format((team_1_sum) / (team_1_sum + team_2_sum) * 100, ".2f")
        possession_team_2 = format((team_2_sum) / (team_1_sum + team_2_sum) * 100, ".2f")

        self.result_dict["possession"] = [str(possession_team_1), str(possession_team_2)]

    def calculate_pass(self):
        pass_count_1 = 0
        pass_false_1 = 0

        pass_count_2 = 0
        pass_false_2 = 0

        pass_team_1 = int((self.team_1_sum_dict["패스"] + self.team_1_sum_dict["드리블"] +  self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"]) / 4)
        pass_team_2 = int((self.team_2_sum_dict["패스"] + self.team_2_sum_dict["드리블"] + self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"]) / 4)
        pass_defense_team_1 = int((self.team_1_sum_dict["수비"] * 2 + self.team_1_sum_dict["주력"] + self.team_1_sum_dict["체력"]) / 4)
        pass_defense_team_2 = int((self.team_2_sum_dict["수비"] * 2 + self.team_2_sum_dict["주력"] + self.team_2_sum_dict["체력"]) / 4)
        for i in range(0, random.randrange(100, 300)):
            if random.randrange(0, pass_team_1) > random.randrange(0, pass_defense_team_2):
                pass_count_1 = pass_count_1 + 1
            else:
                pass_false_1 = pass_false_1 + 1
        for i in range(0, random.randrange(100, 300)):
            if random.randrange(0, pass_team_2) > random.randrange(0, pass_defense_team_1):
                pass_count_2 = pass_count_2 + 1
            else:
                pass_false_2 = pass_false_2 + 1
        print("pass_count_1 %d pass_false_1 %d" % (pass_count_1, pass_false_1))
        print("pass_count_2 %d pass_false_2 %d" % (pass_count_2, pass_false_2))
        self.result_dict["pass"] = [str(pass_count_1) + "(" + str(pass_count_1 + pass_false_1) + ")", str(pass_count_2) + "(" + str(pass_count_2 + pass_false_2) + ")"]

    def get_result(self):
        self.caclulate_sum()
        self.calculate_shoot()
        self.calculate_possesion()
        self.calculate_pass()

        return self.result_dict