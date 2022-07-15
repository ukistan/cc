#월 4회 스터디, 1번은 오프라인 3번은 온라인
#조건1 랜덤으로 날짜를 뽑아야함
#조건2 월별날짜는 28일까지로 감안
#조건 3 매월1-3일은 제외
from random import *
off1 = randint(4,28)
off2 = randint(4,28)
off3 = randint(4,28)
print ("오프라인 스터디 날짜는 ",off1,",",off2,",",off3,"로 선정되었습니다")