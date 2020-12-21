import pygame

WHITE = (255, 255, 255)
transparent = (0, 0, 0, 0)
pad_width = 1600
pad_height = 900

class Block(pygame.sprite.Sprite):
    def __init__(self, img):
        super().__init__()
        self.image = img
        self.rect = img.get_rect()
class Pannel:
    def pannel(self, result_dict):

        hyphen_image = pygame.image.load('images/hyphen.png')
        Top_banner = pygame.image.load('images/test.png')
        gamepad.blit(Top_banner, (0,0.01))
        block_width_list = []
        temp_list = []
        number_1 = 1

        if number_1 == 1:
            number_image_team1 = pygame.image.load("images/number_" + result_dict["goal"][0] + ".png")
            number_image_team2 = pygame.image.load("images/number_" + result_dict["goal"][1] + ".png")
            gamepad.blit(number_image_team1, (600,150))
            gamepad.blit(number_image_team2, (900, 150))
            gamepad.blit(hyphen_image, (780, 210))

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("유효 공격 포인트", True, (0, 0, 0))
        gamepad.blit(text, [730, 370])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("패스 횟수", True, (0, 0, 0))
        gamepad.blit(text, [770, 500])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("골 점유율", True, (0, 0, 0))
        gamepad.blit(text, [770, 630])

        font = pygame.font.SysFont('hy견고딕', 20)
        text = font.render("선방 or 차단 횟수", True, (0, 0, 0))
        gamepad.blit(text, [730, 760])


        ###골
        key_value = result_dict["goal"][0] + "(" +result_dict["shoot"][0] +")"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [190, 430])
        #막대의 길이를 정하기 위한 작업.
        if int(result_dict["goal"][0]== 0) and int(result_dict["goal"][1]== 0) :
            block_width_list.append(0.5)
        else:
            block_width = int(result_dict["goal"][0])/( int(result_dict["goal"][0]) + int(result_dict["goal"][1]) )
            block_width_list.append(block_width)

        ###패스
        key_value = result_dict["pass"][0]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [160, 560])

        temp_list.append(result_dict["pass"][0].replace('(', ' ').split(" ")[0])
        temp_list.append(result_dict["pass"][1].replace('(', ' ').split(" ")[0])

        block_width = int(temp_list[0])/(int(temp_list[0]) + int(temp_list[1]))
        block_width_list.append(block_width)

        ###점유율
        key_value = result_dict["possession"][0] + "%"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [160, 690])
        block_width= float(result_dict["possession"][0]) * 0.01
        block_width_list.append(block_width)

        ###선방 횟수
        key_value = result_dict["save"][0]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [200, 820])
        if int(result_dict["save"][0]) == 0 and int(result_dict["save"][1]) == 0:
            block_width_list.append(0.5)
        else:
            block_width = int(result_dict["save"][0])/( int(result_dict["save"][0]) + int(result_dict["save"][1]) )
            block_width_list.append(block_width)

    ####################################
        ###골
        key_value = result_dict["goal"][1] + "(" +result_dict["shoot"][1] +")"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1400, 430])
        ###패스
        key_value = result_dict["pass"][1]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1360, 560])
        ###점유율
        key_value = result_dict["possession"][1] + "%"
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1360, 690])
        ###선방횟수
        key_value = result_dict["save"][1]
        font = pygame.font.SysFont('hy견고딕', 30)
        text = font.render(key_value, True, (0, 0, 0))
        gamepad.blit(text, [1400, 820])

    ##########################################3
        #초록색과 연두색의 block bar를 만들어주는 부분.
        pic_1 = pygame.image.load("images/green_bar.png").convert()
        pic_2 = pygame.image.load("images/yellow_bar.png").convert()
        # 막대의 가로와 길이 설정. 나중에 변수로 만들어주어야함


        block_list = pygame.sprite.Group()
        #연두와 초록색 막대 너비 조정하는 부분.
        for i in range(0, 4):
            pic_1 = pygame.transform.scale(pic_1, (int(800 * block_width_list[i]), 80))
            pic_2 = pygame.transform.scale(pic_2, (int(800 - 800 * block_width_list[i]), 80))

            block_1 = Block(pic_1)
            #list로 해서 x의 값을 변동시키면 될 듯 싶다.
            block_1.rect.x = 420
            block_1.rect.y = 400 + i * 130
            block_list.add(block_1)

            block_2 = Block(pic_2)
            block_2.rect.x = 420 + 800 * block_width_list[i]
            block_2.rect.y = 400 + i * 130
            block_list.add(block_2)

        #background = pygame.Surface(gamepad.get_size())
        block_list.draw(gamepad)
        #gamepad.blit(background,(0,0))
    def flag_1(self,x,y):
        gamepad.blit(flag_craft_1, (x,y))

    def flag_2(self,x,y):
        gamepad.blit(flag_craft_2, (x,y))

    def runGame(self, result_dict):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True

            gamepad.fill(WHITE)
            self.pannel(result_dict)
            self.flag_1(100, 100)
            self.flag_2(1300, 100)
            pygame.display.flip()
        pygame.quit()
        #quit()

    def initGame(self, flag_1, flag_2):
        global gamepad, flag_craft_1, flag_craft_2

        #pygame 라이브러리 초기화
        pygame.init()
        #특정 크기 스크린 생성
        gamepad = pygame.display.set_mode((pad_width,pad_height))
        pygame.display.set_caption('PySoccer')

        #이미지 로드, convert사용해서 더 빠르게 변환
        flag_craft_1 = pygame.image.load("images/" + flag_1 + ".jpg").convert()
        flag_craft_2 = pygame.image.load("images/" + flag_2 + ".jpg").convert()
