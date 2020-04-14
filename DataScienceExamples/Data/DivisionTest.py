from DataScienceExamples.Data.Division import inverseNumber
from DataScienceExamples.Data.Division import dividertoint
from DataScienceExamples.Data.Division import division
from DataScienceExamples.Data.Division import binary
from DataScienceExamples.Data.AdditionMultiplicationTables import addition
from DataScienceExamples.Data.AdditionMultiplicationTables import multiplication
from DataScienceExamples.Data.AdditionMultiplicationTables import performull
from DataScienceExamples.Data.AdditionMultiplicationTables import muls
from DataScienceExamples.Data.AdditionMultiplicationTables import subtract
from DataScienceExamples.Data.NumbersProperties import overturn
from DataScienceExamples.Data.NumbersProperties import compare
from DataScienceExamples.Data.NumbersProperties import isSimple
from DataScienceExamples.Data.NumbersProperties import simplesc
from DataScienceExamples.Data.AdditionMultiplicationTables import subtraction
from DataScienceExamples.Data.AdditionMultiplicationTables import fillzeroes
"""Arithmetics on strings. For Big Numbers. (Greater, than 1E(+|-)308) """

print(addition('623','91')) # 714
for i in range(0,1000):
    print(str(i)+' + '+str(i+10)+' = '+addition(str(i),str(i+10)))
print(addition('322','2450000'))
print(addition('0.3','0.61')) # 0.91
print(0.3+0.61)
print(addition('7.33','12')) # 19.33
print(addition('12','7.33'))
print(addition('28.33333','721.5')) # 749.83333
print(addition('0.25','0.25'))
print(addition('5.509','6.501'))#
print(addition('1.5','1.51'))
print(performull('592','112',muls)) # 66304
print(multiplication('592','112'))
print(multiplication('500','25'))
print(multiplication('5','0.25')) #1.25
print(multiplication('5','0.5'))# 2.5 = 50 * 5 /100 = 250/100 = 2.5
print(multiplication('500','25')) # 120 * 0.5 = 1200 * 5 / 100 = 6000/100 = 60.00 = 60
print(multiplication('128','2'))
print(multiplication('333','3'))
print(multiplication('592','2'))
print(multiplication('383','2'))
print(multiplication('1200','5'))# 60
print(multiplication('120','0.5'))
print(multiplication('0.5','120'))
print(multiplication('','120'))
print(multiplication('120',''))
print(multiplication('0','120'))
print(multiplication('123582356346348768678','0'))
print(multiplication('','325760234250235801'))
print(multiplication('1','25015997'))
print(multiplication('25015997','1')) #0.9 * 0.9 = 9 * 9 /100 = 81
print(multiplication('9','9')) # 9*9 / 100 = 81 /100 = 0.81
# print(backtoint('0','0','99','99'))
print(multiplication('99','99')) #0.81  0.99 * 0.99 = 0.9801 => 9999
#print(multiplication('120','1'))
print(multiplication('0.99','0.99'))
print(multiplication('52','52'))
print(multiplication('5.2','5.2'))
print(multiplication('5.2','5.25')) # 27.3
print(multiplication('0.2','0.25'))# 0.05
# if '2704'!='0': print('True')
print(multiplication('52.3','1.11'))
print(multiplication('2.5','1.9'))
print(multiplication('0.2','99'))
# print(multiplication('99','0.2'))
print(multiplication('3383','3')) # 10149
# # for i in range(1,21):
# #     for j in range(1,21):
# #         print(str(i)+' * '+str(j)+' = '+multiplication(str(i),str(j)))
# print(multiplication('3383','3'))
print(multiplication('383','3')) #
print(multiplication('0.27','0.009'))
print(addition('888','791'))
print(subtract('-782','-347'))# -782 + 347 = 347 - 782
print(subtract('347','782'))
print(subtract('782','347'))
print(subtract('782','-347'))
print(addition('782','347')) #1129
print(subtract('-782','347'))
print(subtract('10','2'))
print(subtract('377','799'))
print(subtract('999','10'))
print(subtract('555','555'))
print(multiplication('5','0.03'))
print(addition('42567420985704629','3457249635345')) # 42570878235339974

print(inverseNumber('2')) # 1/2 = 0.5
print(inverseNumber('4')) # 1/4 = 0.25
print(inverseNumber('3',6)) # 1/3 = 0.(3) 6 times => 0.333333
print(inverseNumber('33',3)) # 1/33 = 0.(03) 3 times => 0.030303
print(inverseNumber('11',5))
aaa,bbb = dividertoint('5.5','2.95')
print(aaa+' : '+bbb)
print(division('5','25'))# 2.5
print(overturn(binary('4'))) # 10000000
print(division('0.0625','2'))
print(multiplication('2020','5'))
for i in range(1,257): #256, 16384
    print(overturn(binary(str(i)))+' : '+str(i))
print(subtraction('0.6','0.0'))
# print(subtraction('0.3669984','0.36629856')) #0.366 998 40   0.366 298 56 = 0.000701-1
# print(subtraction('0.366998','0.366297')) #0.000701
# print(subtraction('3669984','36629856'))
print(subtraction('36629856','3669984'))#32 959 872     (33 0-7)
print(subtraction('0.36629856','0.3669984')) # -0.00069984
print(subtraction('0.3669984','0.36629856')) # 0.00069984
print(subtraction('0.36629856','0.36699840')) # the same
print(subtraction('999','1000'))
print(subtraction('999','10000'))# 999 - 10000 = - 9001 (10000 - 999)
print(fillzeroes('36629856','3669984'))
print(subtraction('36699856','3669984'))
print(subtraction('-0.9','-0.2'))
print(subtraction('-0.5','1.7'))
print(isSimple(7))
print(simplesc)
print(inverseNumber('11',5))