import random
import requests
from bs4 import BeautifulSoup
import time

# 포지션과 팀 별 선수 입력
random_position = ['GK', 'RB', 'LB', 'LCB', 'RCB', 'LCM', 'CM', 'RCM', 'LS', 'ST', 'RS']
team_dict = {"토트넘": ['Heung-Min-Son', 'Hugo-Lloris', 'matt-doherty', 'sergio-reguilon-rodriguez', 'toby-alderweireld',
                     'Davinson-Sanchez', 'harry-winks', 'gareth-bale', 'harry-kane', 'erik-lamela', 'eric-dier'],
             "레스터시티": ['vardy', 'maddison', 'harvey-barnes', 'Ndidi', 'choudhury', 'Tielemans', 'Pereira', 'evans',
                       'soyuncu', 'wes-Morgan', 'kasper-schmeichel'],
             "에버튼": ['Jordan Pickford', 'Mason Holgate','Séamus Coleman', 'Lucas Digne', 'Yerry Mina',  'Allan Marques', 'Fabian Delph', 'Gylfi', 'Richarlison de Andrade',
                     'Dominic Calvert-Lewin', 'Yannick Bolasie'],
             "첼시": ['Arrizabalaga', 'rudiger', 'zouma', 'reece-james', 'tanco', 'kante', 'luiz-frello-filho-jorge',
                    'ross', 'olivier', 'Odoi', 'michy-batshuayi'],
             "웨스트햄": ['Łukasz Fabiański' , 'Aaron Cresswell', 'Fabián Balbuena', 'Vladimír Coufal', 'Andriy Yarmolenko', 'Saïd Benrahma', 'Jarrod Bowen', 'Craig Dawson',
                    'Mark Noble', 'Manuel Lanzini', 'Robert Snodgrass'],
             "리버풀": ["Alisson Ramses Becker", "Fábio Henrique Tavares", "Virgil van Dijk", "Trent Alexander-Arnold", "Andrew Robertson"
                 , "JAMES MILNER", "Mohamed Salah", "Jordan Henderson", "Roberto Firmino", "Sadio", "Divock"],
             "맨시티": ["Ederson", "Kyle Walker", "Rúben Santos Gato Alves Dias", "Benjamin Mendy", "Cancelo",
                     "Kevin De Bruyne", "Zinchenko", "Rodrigo", "Sergio Agüero", "Ferran", "Gabriel"],
             "맨유": ["David De Gea", "Paul Pogba", "Harry Maguire", "Phil Jones", "Eric Bailly", "Victor Lindelöf", "Juan Mata"
                 , "Jesse Lingard", "Anthony Martial", "Marcus Rashford", "Mason Greenwood"],
             "사우스햄튼": ['Alex McCarthy', 'Kyle Walker-Peters', 'Ryan Bertrand', 'Jannik Vestergaard', 'Jack Stephens',  'Oriol Romeu', 'James Ward-Prowse', 'Mario Lemina',
                       'Shane Long', 'Danny Ings', 'Nathan Redmond'],
             "아스날": ["Bernd Leno", "Héctor Bellerín", "Kieran Tierney", "William Saliba", "Sokratis Papastathopoulos", "Dani Ceballos"
                 , "Mesut Özil", "Thomas Partey", "Bukayo Saka", "Willian", "Gabriel Martinelli"]}

# Player class는 축구 선수 한명에 대한 stat 설정
class Player:
    def __init__(self, p_name, p_position):
        self.p_name = p_name
        self.p_position = p_position
        self.stat_dict = {}

# random으로 선수 능력치 할당
    def set_stat_random(self):
        if self.p_position == 'GK':
            self.stat_dict['반사신경'] = random.randrange(40,100)
            self.stat_dict['볼 핸들링'] = random.randrange(40,100)
            self.stat_dict['골킾'] = random.randrange(40,100)
            self.stat_dict['공중볼'] = random.randrange(40,100)
            self.stat_dict['수비조율'] =random.randrange(40,100)
            self.stat_dict['공던지기'] =random.randrange(40,100)
        else :
            self.stat_dict['주력'] = random.randrange(40,100)
            self.stat_dict['슈팅'] = random.randrange(40,100)
            self.stat_dict['패스'] = random.randrange(40,100)
            self.stat_dict['드리블'] = random.randrange(40,100)
            self.stat_dict['수비'] = random.randrange(40,100)
            self.stat_dict['체력'] = random.randrange(40,100)

# 축구 게임 홈페이지에서 능력치 가져옮
    def set_stat_auto(self):
        # 손흥민: url = 'https://www.futbin.com/players?page=1&search=' + 'Heung-Min-Son'
        url = 'https://www.futbin.com/21/players?page=1&search=' + self.p_name
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        # 홈페이지 엤는 table을 찾는 과정. 해당 table 이름이 홈페이지에 있는 선수들 스탯 창을 의미함
        table = soup.find("table",
                          {"class": "table table-bordered table-hover table-responsive w-100 d-block d-md-table"})
        # print(table)
        data = []
        for a in table.find_all("tr"):
            for b in a.find_all("td"):
                data.append(b.get_text())

        # 포지션도 피파 홈페이지에 있는 포지션으로 할당. data[2]에 저장되어 있음.
        self.p_position = data[2]

        # Gk와 다른 선수들은 스탯의 종류가 다르므로 if 문을 통해 따로 처리.
        if self.p_position == 'GK':
            self.stat_dict['반사신경'] = int(data[8])
            self.stat_dict['볼 핸들링'] = int(data[9])
            self.stat_dict['골킾'] = int(data[10])
            self.stat_dict['공중볼'] = int(data[11])
            self.stat_dict['수비조율'] = int(data[12])
            self.stat_dict['공던지기'] = int(data[13])
        else:
            self.stat_dict['주력'] = int(data[8])
            self.stat_dict['슈팅'] = int(data[9])
            self.stat_dict['패스'] = int(data[10])
            self.stat_dict['드리블'] = int(data[11])
            self.stat_dict['수비'] = int(data[12])
            self.stat_dict['체력'] = int(data[13])

    # 선수들에 할당된 stat 을 print 함
    def print_player_info(self):
        print(self.p_name, end=", ")
        print(self.p_position)
        print(self.stat_dict)

# 처음 선수들의 포지션과 능력치를 각각 랜덤하게 할당함
def set_start_random(team1):
    p_list = []
    players_list = []
    position_list = []
    players = team_dict[team1]

    # 선수들은 11명이므로, 11명을 while 문을 이용해서 포지션과 스탯 랜덤하게 설정. 스탯은 Player 클래스의 set_stat_random 을 이용
    while len(players_list) != 11:
        n = random.randrange(0, len(players))
        new_player = players[n]
        n = random.randrange(0, len(random_position))
        new_position = random_position[n]
        if new_position not in position_list and new_player not in players_list:
            position_list.append(new_position)
            players_list.append(new_player)
            p = Player(new_player, new_position)
            p_list.append(p)
    # 스탯을 랜덤으로 설정하기 위해 Player 클래스의 set_stat_random 호출
    for p in p_list:
        p.set_stat_random()
    for p in p_list:
        p.print_player_info()
    return p_list

# 선수들은 11명이므로, 11명 범위 내에서 Player 객체를 11개 만들고 스탯은 Player 클래스의 set_stat_auto 을 이용
def set_start_auto(team1):
    p_list = []
    players = team_dict[team1]
    count = 0

    for i in range(0, 11):
        new_player = players[i]
        new_position = ""
        p = Player(new_player, new_position)
        p_list.append(p)

    # 웹 스크랩을 sleep 을 주지 않으면 해당 사이트에서 차단시키거나 오류가 발생함. sleep 을 주되 진행 상황을 묘사하였음.
    # stat 은 Player 클래스의 set_stat_auto 호출
    for p in p_list:
        print("Capability allocation in progress... " + str(count) + "%")
        p.set_stat_auto()
        count = count + 10
        time.sleep(1)

    for p in p_list:
        p.print_player_info()
    return p_list
