import os
import pygame
import sys
import random
import time

# Pygame 초기화
pygame.init()

# 현재 작업 디렉토리를 스크립트 위치로 설정 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 화면 설정
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Chicken Game')

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 폰트 설정 (기본 시스템 폰트 대신 사용자 정의 폰트 사용)
font_path = 'images/pmsimages/custom_font.ttf'  # 사용자 정의 폰트 경로
font_size = 55
font = pygame.font.Font(font_path, font_size)


# 이미지 로드 및 크기 조정
chicken_frames = [
    pygame.transform.scale(pygame.image.load('images/pmsimages/chicken_frame1.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('images/pmsimages/chicken_frame2.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('images/pmsimages/chicken_frame3.png'), (50, 50)),
    pygame.transform.scale(pygame.image.load('images/pmsimages/chicken_frame4.png'), (50, 50))
]

# 애니메이션 상태 변수
current_frame = 0
frame_delay = 100  # 프레임 전환 간격 (밀리초)
last_update = pygame.time.get_ticks()

# 이미지 초기 위치 설정
chicken_rect = chicken_frames[0].get_rect()
chicken_rect.center = (screen_width // 2, screen_height // 2)

# 기타 이미지 로드 및 크기 조정
chicken_hit_img = pygame.image.load('images/pmsimages/chicken_hit.png')
chicken_hit_img = pygame.transform.scale(chicken_hit_img, (50, 50))

armor_chicken_img = pygame.image.load('images/pmsimages/armor_chicken.png')
armor_chicken_img = pygame.transform.scale(armor_chicken_img, (50, 50))

knife_img = pygame.image.load('images/pmsimages/knife.png')
knife_img = pygame.transform.scale(knife_img, (50, 50))

fire_img = pygame.image.load('images/pmsimages/fire.png')
fire_img = pygame.transform.scale(fire_img, (50, 50))

car_img = pygame.image.load('images/pmsimages/car.png')
car_img = pygame.transform.scale(car_img, (50, 50))

motorbike_img = pygame.image.load('images/pmsimages/motorbike.png')
motorbike_img = pygame.transform.scale(motorbike_img, (50, 50))

truck_img = pygame.image.load('images/pmsimages/truck.png')
truck_img = pygame.transform.scale(truck_img, (50, 50))

fox_img = pygame.image.load('images/pmsimages/fox.png')
fox_img = pygame.transform.scale(fox_img, (50, 50))

snake_img = pygame.image.load('images/pmsimages/snake.png')
snake_img = pygame.transform.scale(snake_img, (50, 50))

tiger_img = pygame.image.load('images/pmsimages/tiger.png')
tiger_img = pygame.transform.scale(tiger_img, (50, 50))

bg_start = pygame.image.load('images/pmsimages/start_screen.png')
bg_start = pygame.transform.scale(bg_start, (screen_width, screen_height))

bg_instructions = pygame.image.load('images/pmsimages/instructions.png')  # 설명 이미지 로드
bg_instructions = pygame.transform.scale(bg_instructions, (screen_width, screen_height))

bg_stage1 = pygame.image.load('images/pmsimages/background1.png')
bg_stage1 = pygame.transform.scale(bg_stage1, (screen_width, screen_height))
bg_stage2 = pygame.image.load('images/pmsimages/background2.png')
bg_stage2 = pygame.transform.scale(bg_stage2, (screen_width, screen_height))
bg_stage3 = pygame.image.load('images/pmsimages/background3.png')
bg_stage3 = pygame.transform.scale(bg_stage3, (screen_width, screen_height))
final_scene = pygame.image.load('images/pmsimages/nature.png')
final_scene = pygame.transform.scale(final_scene, (screen_width, screen_height))

armor_img = pygame.image.load('images/pmsimages/armor.png')
armor_img = pygame.transform.scale(armor_img, (50, 50))

gameover_img = pygame.image.load('images/pmsimages/gameover_screen.png')
gameover_img = pygame.transform.scale(gameover_img, (screen_width, screen_height))

# 전역 변수 선언
current_stage = 1

# 버튼 클래스 정의
class Button:
    def __init__(self, text, x, y, width, height, font, color):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                return True
        return False

# 장애물 초기화 함수
def create_obstacle(image, number):
    obstacles = []
    for _ in range(number):
        x = random.randint(0, screen_width - image.get_width())
        y = random.randint(0, screen_height - image.get_height())
        rect = image.get_rect(topleft=(x, y))
        speed_x = random.choice([-3, 3])
        speed_y = random.choice([-3, 3])
        obstacles.append({'rect': rect, 'speed_x': speed_x, 'speed_y': speed_y})
    return obstacles

# 보호갑옷 아이템 초기화 함수
def create_armor(image):
    x = random.randint(0, screen_width - image.get_width())
    y = random.randint(0, screen_height - image.get_height())
    rect = image.get_rect(topleft=(x, y))
    speed_x = random.choice([-2, 2])
    speed_y = random.choice([-2, 2])
    return {'rect': rect, 'speed_x': speed_x, 'speed_y': speed_y}

# 카운트다운 함수
def countdown(stage):
    for i in range(3, 0, -1):
        if stage == 1:
            screen.blit(bg_stage1, (0, 0))
            for obstacle in knife_obstacles:
                screen.blit(knife_img, obstacle['rect'])
            for obstacle in fire_obstacles:
                screen.blit(fire_img, obstacle['rect'])
        elif stage == 2:
            screen.blit(bg_stage2, (0, 0))
            for obstacle in car_obstacles:
                screen.blit(car_img, obstacle['rect'])
            for obstacle in motorbike_obstacles:
                screen.blit(motorbike_img, obstacle['rect'])
            for obstacle in truck_obstacles:
                screen.blit(truck_img, obstacle['rect'])
        elif stage == 3:
            screen.blit(bg_stage3, (0, 0))
            for obstacle in fox_obstacles:
                screen.blit(fox_img, obstacle['rect'])
            for obstacle in snake_obstacles:
                screen.blit(snake_img, obstacle['rect'])
            for obstacle in tiger_obstacles:
                screen.blit(tiger_img, obstacle['rect'])
        
        # 스테이지 번호 텍스트 추가
        stage_text = font.render(f"Stage {stage}", True, BLACK)
        stage_rect = stage_text.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(stage_text, stage_rect)
        
        # 카운트다운 텍스트 추가
        countdown_text = font.render(str(i), True, BLACK)
        countdown_rect = countdown_text.get_rect(center=(screen_width // 2, screen_height // 2 + 100))
        screen.blit(countdown_text, countdown_rect)
        
        # 닭 이미지 추가
        screen.blit(chicken_current_img, chicken_rect)
        
        pygame.display.flip()
        pygame.time.wait(1000)


# 게임 초기화 함수
def initialize_game(stage):
    global chicken_rect, chicken_speed, invincible, invincible_start_time, start_time, stage_duration, current_stage
    global knife_obstacles, fire_obstacles, car_obstacles, motorbike_obstacles, truck_obstacles, fox_obstacles, snake_obstacles, tiger_obstacles, armor_item, obstacle_speed, chicken_current_img

    # 장애물 생성
    knife_obstacles = create_obstacle(knife_img, 3)
    fire_obstacles = create_obstacle(fire_img, 3)
    car_obstacles = create_obstacle(car_img, 3)
    motorbike_obstacles = create_obstacle(motorbike_img, 3)
    truck_obstacles = create_obstacle(truck_img, 3)
    fox_obstacles = create_obstacle(fox_img, 4)
    snake_obstacles = create_obstacle(snake_img, 4)
    tiger_obstacles = create_obstacle(tiger_img, 4)
    
    # 보호갑옷 아이템 생성
    armor_item = create_armor(armor_img)
    
    # 닭 초기 위치 설정
    while True:
        chicken_rect = chicken_frames[0].get_rect()
        chicken_rect.center = (random.randint(0, screen_width), random.randint(0, screen_height))
        
        # 장애물과 겹치지 않는 위치 찾기
        is_valid_position = True
        for obstacle in knife_obstacles + fire_obstacles + car_obstacles + motorbike_obstacles + truck_obstacles + fox_obstacles + snake_obstacles + tiger_obstacles:
            if chicken_rect.colliderect(obstacle['rect']):
                is_valid_position = False
                break
        
        if is_valid_position:
            break

    # 게임 상태 초기화
    chicken_speed = 5
    invincible = False
    invincible_start_time = 0
    chicken_current_img = chicken_frames[0]  # 현재 닭 이미지
    stage_duration = 30  # 각 단계의 시간(초)
    start_time = time.time()

    # 각 스테이지별 초기 장애물 속도 설정
    if current_stage == 1:
        obstacle_speed = 1.00  # 1단계 초기 속도
    elif current_stage == 2:
        obstacle_speed = 1.1  # 2단계 초기 속도
    elif current_stage == 3:
        obstacle_speed = 1.2  # 3단계 초기 속도


# 애니메이션 업데이트 함수
def update_animation():
    global current_frame, last_update, chicken_current_img

    now = pygame.time.get_ticks()
    if now - last_update > frame_delay:
        last_update = now
        current_frame = (current_frame + 1) % len(chicken_frames)
        if not invincible:  # 무적 상태가 아닐 때만 애니메이션 업데이트
            chicken_current_img = chicken_frames[current_frame]

# 시작 화면 함수
def start_screen():
    button_width = 200
    button_height = 60
    spacing = 20
    total_width = button_width * 3 + spacing * 2
    
    start_button = Button('Start', screen_width // 2 - total_width // 2, screen_height // 2 + 120, button_width, button_height, font, WHITE)
    how_to_button = Button('How to', start_button.rect.right + spacing, screen_height // 2 + 120, button_width, button_height, font, WHITE)
    exit_button = Button('Exit', how_to_button.rect.right + spacing, screen_height // 2 + 120, button_width, button_height, font, WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if start_button.is_clicked(event):
                initialize_game(current_stage)
                countdown(current_stage)  # 스테이지 시작 전 카운트다운 추가
                return
            if how_to_button.is_clicked(event):
                show_instructions()
            if exit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        screen.blit(bg_start, (0, 0))
        start_button.draw(screen)
        how_to_button.draw(screen)
        exit_button.draw(screen)
        pygame.display.flip()

def show_instructions():
    back_button = Button('Back', screen_width // 2 - 100, screen_height - 100, 200, 60, font, WHITE)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if back_button.is_clicked(event):
                return

        screen.blit(bg_instructions, (0, 0))  # 설명 이미지 그리기
        back_button.draw(screen)
        pygame.display.flip()

# 게임 오버 화면 함수
restart_button = Button('Restart', screen_width // 2 - 200, screen_height // 2 + 100, 200, 60, font, WHITE)
quit_button = Button('Quit', screen_width // 2 + 10, screen_height // 2 + 100, 200, 60, font, WHITE)

def game_over_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if restart_button.is_clicked(event):
                current_stage = 1  # 게임 오버 후 스테이지 초기화
                initialize_game(current_stage)
                countdown(current_stage)  # 스테이지 시작 전 카운트다운 추가
                return
            if quit_button.is_clicked(event):
                pygame.quit()
                sys.exit()

        screen.blit(gameover_img, (0, 0))  # 게임 오버 이미지 그리기
        restart_button.draw(screen)
        quit_button.draw(screen)
        pygame.display.flip()

# 게임 초기화
initialize_game(current_stage)

# 시작 화면 호출
start_screen()

# 게임 루프
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 키 입력 처리 및 닭 움직이기
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        chicken_rect.x -= chicken_speed
    if keys[pygame.K_RIGHT]:
        chicken_rect.x += chicken_speed
    if keys[pygame.K_UP]:
        chicken_rect.y -= chicken_speed
    if keys[pygame.K_DOWN]:
        chicken_rect.y += chicken_speed
    
    # 닭이 화면 밖으로 나가지 않도록 위치 제한
    if chicken_rect.left < 0:
        chicken_rect.left = 0
    if chicken_rect.right > screen_width:
        chicken_rect.right = screen_width
    if chicken_rect.top < 0:
        chicken_rect.top = 0
    if chicken_rect.bottom > screen_height:
       chicken_rect.bottom = screen_height


    # 애니메이션 업데이트
    update_animation()

    # 보호갑옷 아이템 움직이기
    armor_item['rect'].x += armor_item['speed_x']
    armor_item['rect'].y += armor_item['speed_y']
    if armor_item['rect'].right > screen_width or armor_item['rect'].left < 0:
        armor_item['speed_x'] = -armor_item['speed_x']
    if armor_item['rect'].bottom > screen_height or armor_item['rect'].top < 0:
        armor_item['speed_y'] = -armor_item['speed_y']

    # 배경 그리기
    if current_stage == 1:
        screen.blit(bg_stage1, (0, 0))
    elif current_stage == 2:
        screen.blit(bg_stage2, (0, 0))
    elif current_stage == 3:
        screen.blit(bg_stage3, (0, 0))

    # 장애물 움직이기 및 화면 끝에 도달 시 반대 방향으로 이동
    if current_stage == 1:
        for obstacle in knife_obstacles + fire_obstacles:
            obstacle['rect'].x += obstacle['speed_x'] * obstacle_speed
            obstacle['rect'].y += obstacle['speed_y'] * obstacle_speed
            
            if obstacle['rect'].right > screen_width or obstacle['rect'].left < 0:
                obstacle['speed_x'] = -obstacle['speed_x']
            if obstacle['rect'].bottom > screen_height or obstacle['rect'].top < 0:
                obstacle['speed_y'] = -obstacle['speed_y']
    elif current_stage == 2:
        for obstacle in car_obstacles + motorbike_obstacles + truck_obstacles:
            obstacle['rect'].x += obstacle['speed_x'] * obstacle_speed
            obstacle['rect'].y += obstacle['speed_y'] * obstacle_speed
            
            if obstacle['rect'].right > screen_width or obstacle['rect'].left < 0:
                obstacle['speed_x'] = -obstacle['speed_x']
            if obstacle['rect'].bottom > screen_height or obstacle['rect'].top < 0:
                obstacle['speed_y'] = -obstacle['speed_y']
    elif current_stage == 3:
        for obstacle in fox_obstacles + snake_obstacles + tiger_obstacles:
            obstacle['rect'].x += obstacle['speed_x'] * obstacle_speed
            obstacle['rect'].y += obstacle['speed_y'] * obstacle_speed
            
            if obstacle['rect'].right > screen_width or obstacle['rect'].left < 0:
                obstacle['speed_x'] = -obstacle['speed_x']
            if obstacle['rect'].bottom > screen_height or obstacle['rect'].top < 0:
                obstacle['speed_y'] = -obstacle['speed_y']

    # 보호갑옷 아이템 획득 처리
    if chicken_rect.colliderect(armor_item['rect']):
        invincible = True
        invincible_start_time = time.time()
        chicken_current_img = armor_chicken_img  # 갑옷 입은 치킨 이미지로 변경
        armor_item = create_armor(armor_img)  # 아이템 재생성

    # 보호갑옷 지속시간 관리
    if invincible and time.time() - invincible_start_time > 10:
        invincible = False
        chicken_current_img = chicken_frames[0]  # 무적 상태 해제 시 원래 치킨 이미지로 변경

    # 충돌 검사
    game_over = False
    if current_stage == 1:
        for obstacle in knife_obstacles + fire_obstacles:
            if not invincible and chicken_rect.colliderect(obstacle['rect']):
                chicken_current_img = chicken_hit_img  # 치킨 이미지로 변경
                game_over = True
                break
    elif current_stage == 2:
        for obstacle in car_obstacles + motorbike_obstacles + truck_obstacles:
            if not invincible and chicken_rect.colliderect(obstacle['rect']):
                chicken_current_img = chicken_hit_img  # 치킨 이미지로 변경
                game_over = True
                break
    elif current_stage == 3:
        for obstacle in fox_obstacles + snake_obstacles + tiger_obstacles:
            if not invincible and chicken_rect.colliderect(obstacle['rect']):
                chicken_current_img = chicken_hit_img  # 치킨 이미지로 변경
                game_over = True
                break

    # 타이머 계산
    elapsed_time = time.time() - start_time
    time_left = stage_duration - elapsed_time

    # 타이머 표시
    timer_text = font.render(f'Time Left: {int(time_left)}', True, BLACK)
    screen.blit(timer_text, (10, 10))

    # 보호갑옷 그리기
    screen.blit(armor_img, armor_item['rect'])

    # 장애물 그리기
    if current_stage == 1:
        for obstacle in knife_obstacles:
            screen.blit(knife_img, obstacle['rect'])
        for obstacle in fire_obstacles:
            screen.blit(fire_img, obstacle['rect'])
    elif current_stage == 2:
        for obstacle in car_obstacles:
            screen.blit(car_img, obstacle['rect'])
        for obstacle in motorbike_obstacles:
            screen.blit(motorbike_img, obstacle['rect'])
        for obstacle in truck_obstacles:
            screen.blit(truck_img, obstacle['rect'])
    elif current_stage == 3:
        for obstacle in fox_obstacles:
            screen.blit(fox_img, obstacle['rect'])
        for obstacle in snake_obstacles:
            screen.blit(snake_img, obstacle['rect'])
        for obstacle in tiger_obstacles:
            screen.blit(tiger_img, obstacle['rect'])

    # 닭 그리기
    screen.blit(chicken_current_img, chicken_rect)

    # 화면 업데이트
    pygame.display.flip()

    # 게임 오버 처리
    if game_over:
        screen.fill(WHITE)  # 화면을 하얀색으로 지우기
        screen.blit(bg_stage1, (0, 0))  # 배경 다시 그리기 (1단계 배경 사용)
        screen.blit(chicken_current_img, chicken_rect)  # 치킨 이미지 그리기
        pygame.display.flip()
        pygame.time.wait(1000)  # 1초 대기

        screen.blit(gameover_img, (0, 0))  # 게임 오버 이미지 그리기
        pygame.display.flip()
        pygame.time.wait(2000)

        # 재시작 루프
        restart = True
        while restart:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    restart = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    current_stage = 1  # 스테이지 초기화
                    initialize_game(current_stage)
                    countdown(current_stage)  # 스테이지 시작 전 카운트다운 추가
                    restart = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if restart_button.is_clicked(event):
                        current_stage = 1  # 스테이지 초기화
                        initialize_game(current_stage)
                        countdown(current_stage)  # 스테이지 시작 전 카운트다운 추가
                        restart = False
                    elif quit_button.is_clicked(event):
                        pygame.quit()
                        sys.exit()
            restart_button.draw(screen)
            quit_button.draw(screen)
            pygame.display.flip()

    elif time_left <= 0:
        current_stage += 1
        if current_stage > 3:
            # 최종 장면 표시
            screen.fill(WHITE)
            screen.blit(final_scene, (0, 0))
            pygame.display.flip()
            pygame.time.wait(5000)
            running = False  # 모든 단계 완료 시 게임 종료
        else:
            initialize_game(current_stage)  # 다음 스테이지로 전환
            countdown(current_stage)  # 스테이지 시작 전 카운트다운 추가
            start_time = time.time()  # 타이머 초기화

    # FPS 설정
    clock.tick(30)

pygame.quit()
sys.exit()














