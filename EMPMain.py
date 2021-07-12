from EMP import EMP
from EMPService import EMPService


emp = EMP(123, 'Steven', 'King', 'SKING', '1234567',
                    '2003-06-17', 'AD_PRES', 24000, '', '', 90)

print(emp)

# empsrv = EMPService()   # 객체 생성 후 호출
# emp = empsrv.readEmp()  # 메서드 호출
# print(emp)

emp = EMPService.readEmp()  # 객체생성없이 바로 메서드 호출
print(emp)

###
#from datetime import datetime

#now = datetime(2021,7,12)
#hire = datetime(2003,6,17)
#days = now - hire  #근무일수
#print(days)

EMPService.computeDuty(emp)
