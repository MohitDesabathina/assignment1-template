#Write 2 unit tests to test:
#1. calculate_return
#2. avg_return
from Portfolio import portfolios
from Stock import stocks
from return_calc import avg_return, calculate_return

s1 = stocks('TSLA',.18)
s2 = stocks('AAPL',.27)
s3 = stocks('AMZN',-.36)
s4 = stocks('MSFT',.45)
s5 = stocks('NIO',.54)
s6 = stocks('NVDA',-.63)
s7 = stocks('MRNA',.72)
s8 = stocks('PYPL',.81)

Tech_Portfolio = portfolios(1,'Technology', [s2,s3,s4,s6,s8])
Trans_Portfolio = portfolios(2,'Transportation',[s1,s5])
Bio_Portfolio = portfolios(3,'BioMedical',[s7])
portfolios = [Tech_Portfolio,Trans_Portfolio,Bio_Portfolio]


#print(avg_return(stocks))
print(calculate_return(portfolios))
