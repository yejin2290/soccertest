from math import factorial, exp

class Poisson:
    def __init__(self, team_1_score, team_2_score):
        # 리그의 평균 득점은 1.492이고 평균 실점은 1.207로 고정
        self.league_goalFor = 1.492
        self.league_goalAgainst = 1.207
        # attack은 팀의 공격력, defense는 팀의 방어력
        # 팀의 공격력은 해당 팀의 평균 득점 / 리그 평균 득점
        # 팀의 방어력은 해당 팀의 평균 실점 / 리그 평균 실점
        self.team_1_attack = team_1_score /self.league_goalFor
        self.team_1_defense = team_2_score / self.league_goalAgainst
        self.team_2_attack = team_2_score / self.league_goalFor
        self.team_2_defense = team_1_score /self.league_goalAgainst

        # team1의 골 득점 확률은 team1의 공격력 * team2의 방어력 * leage 평균 득점
        self.team_1_goal_pb = self.team_1_attack * self.team_2_defense * self.league_goalFor
        self.team_2_goal_pb = self.team_2_attack * self.team_1_defense * self.league_goalFor

    def get_poisson_list(self):
        team1_poisson_list = []
        team2_poisson_list = []
        for i in range(0, 10):
            team1_poisson_list.append([i, self.result(i, self.team_1_goal_pb)] )
            team2_poisson_list.append( [i, self.result(i, self.team_2_goal_pb)] )
        return team1_poisson_list, team2_poisson_list

    def result(self, number, win_prob):
        x = number
        miu = win_prob
        poisson_prob = ((miu ** x) * exp(-miu)) / factorial(x)

        return poisson_prob
