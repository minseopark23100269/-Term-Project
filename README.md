# I don't want to be fried chicken 게임 파이썬으로 구현하기 🐔
- 23100269 박민서
## 프로젝트 설명
이 치킨 게임은 플레이어가 닭이 되어 다양한 장애물을 피하면서 여러 스테이지를 통해 생존하는 게임입니다.
각 스테이지마다 다른 환경과 도전이 기다리고 있으며, 보호갑옷 아이템을 통해 잠시 동안 무적 상태가 될 수 있습니다. 이 게임은 Pygame 라이브러리를 사용하여 개발했습니다.
## 게임 설명

1. **스테이지 1: 주방의 공포**
   - **장애물**: 칼, 불길
   - **설명**: 주방에서 날아다니는 칼과 불길을 피하며 닭이 무사히 탈출해야 합니다. 아직 까진 장애물이 많이 빠르지 않아요!

2. **스테이지 2: 도로의 지옥**
   - **장애물**: 자동차, 오토바이, 트럭
   - **설명**: 닭이 도로 위를 지나가며 질주하는 차량들을 피해 이동해야 합니다. 장애물이 많아졌고 빨라졌습니다!

3. **스테이지 3: 야생의 도전**
   - **장애물**: 여우, 뱀, 호랑이
   - **설명**: 닭이 야생 동물들이 사는 숲 속에서 살아남아야 합니다. 장애물이 더 많아졌고 더 빨라졌습니다!

4. **보호갑옷 아이템**
   - **설명**: 보호갑옷 아이템을 획득할 때마다 10초 동안 무적 상태가 되어 장애물에 부딪혀도 생존할 수 있습니다. 전략적으로 아이템을 사용하여 위험을 피하세요.

## 메뉴설명
1. **시작 화면** - 게임을 시작할 때 처음으로 표시되는 화면입니다.
   
![게임 화면](images/게임화면/시작화면.png)

화면을 보면 
- Start
- How to
- Exit
  
세가지 버튼으로 구성되어 있습니다.

Exit를 누르면 게임이 종료됩니다. 

How to 버튼을 누르면

![게임 화면](images/게임화면/설명화면.png)
이렇게 게임을 설명하는 화면이 나옵니다. back 버튼을 누르면 다시 시작화면으로 돌아갑니다. 

2. **stage 1 화면**
   
![게임 화면](images/게임화면/1단계시작전카운트.png)

모든 stage는 시작 전에 3초간 카운트를 하고 시작합니다.

![게임 화면](images/게임화면/2단계게임중.png)

stage 1 게임이 진행되는 화면입니다. 닭이 있고, 칼과 불의 장애물, 아이템이 있는 걸 확인할 수 있습니다.

3. **stage 2 화면**
   
![게임 화면](images/게임화면/2단계게임중.png)

stage 2 게임이 진행되는 화면입니다. 차와 트럭, 오토바이로 장애물이 바뀐 걸 확인할 수 있습니다. 그리고 타이머 옆의 그림도 닭이 목적지에 더 가까워 진 것으로 변했습니다.

4. **stage 3 화면**
   
![게임 화면](images/게임화면/아이템획득.png)

stage 3 게임이 진행되는 화면입니다. 여기서 닭이 아이템을 획득해서 갑옷을 입은 닭으로 변한 것을 볼 수 있고, 또 타이머 옆의 그림도 닭이 목적지에 더더욱 가까워졌습니다.

5. **성공화면**
   
![게임 화면](images/게임화면/게임성공화면.png)

stage 3까지 게임을 성공하면, 닭이 가고싶었던 목장으로 도착한 모습이 보입니다.

6. **실패화면**
    
![게임 화면](images/게임화면/게임실패시.png)

만약 게임 실패 시 닭이 식당에서 치킨이 된 화면이 나타납니다.

7. **실패후**
    
![게임 화면](images/게임화면/실패후메뉴화면.png)

실패하면 game over화면이 뜹니다. 버튼은
- Restart
- Quit

Restart버튼은 stage1 부터 재시작하는 것이고, Quit버튼은 게임을 끝내는 버튼입니다.

## 요구사항 
이 프로젝트를 실행하려면 다음이 필요합니다: 
- Python 3.x
- Pygame 라이브러리
-  이미지 및 폰트 파일 (제가 이미지는 images 파일 안 pmsimages에 저장해두었고, 폰트파일은 images파일 안 font에 저장해두었어요.)

## 설치 및 실행 방법 
1. Python 3.x 설치:
   - [Python 공식 웹사이트](https://www.python.org/)에서 Python을 다운로드하고 설치하세요.
   
2.  Pygame 라이브러리 설치:
   ```bash
   pip install pygame
 ```

3. 리포지토리를 클론합니다:
git clone https://github.com/minseopark23100269/Term-Project.git

4. 이미지 및 폰트 파일을 프로젝트 디렉토리에 배치합니다:

- 이미지 파일: C:/Users/customer/OneDrive/pmsimages 경로에 저장되어야 합니다.
- 사용자 정의 폰트 파일: C:/Users/customer/OneDrive/pmsimages/custom_font.ttf 경로에 저장되어야 합니다.

5. Spyder에서 게임을 실행합니다:

Spyder를 실행하고, 프로젝트 디렉토리에 있는 23100269박민서텀프로젝트.py 파일을 엽니다.

상단의 "Run" 버튼을 클릭하여 코드를 실행합니다.

   
   









