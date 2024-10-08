import numpy as np 


#Input Parameters  
discount_rate = 0.1     #10% discounted rate 

CAPEX = 8000000   #Capital Expenditures 

Yearly_Average_Production = 2000   #boe/d (1BOE = 1 6MSCF or 6000 SCF of gas)

Yearly_Total_Production = Yearly_Average_Production*365

Annual_Taxes = 100000   # USD 

Annual_Royalties = 90000 #USD 

TotalExploration_DevelopmentCosts = 20000000   #Total Exploration and Development Costs in USD 

PDP_Reserves_Add = 12000000    #BOE 

PPPPDP_Reserves_Add = 35000000  #BOE

OPEX = 20000  #Annuel Operating Expenses (12 month period)

Monthly_OPEX = OPEX / 12

Brent_Price = 60   #$/bbl

Year1_Revenue = Yearly_Total_Production * Brent_Price

Net_Revenue = Year1_Revenue - Annual_Taxes - Annual_Royalties - OPEX 

Operating_Netback = (Year1_Revenue-OPEX-Annual_Royalties-Annual_Taxes)/(Yearly_Total_Production)

print (f"Yearly_Total_Production: {Yearly_Total_Production:,.2f} BBL - Cumulative Production on a 12 month period")
print (f"Year1_Revenue: ${Year1_Revenue:,.2f} - Total Gross Revenue Year 1")
print (f"Monthly_OPEX: ${Monthly_OPEX:,.2f} - Monthly OPEX")
print (f"Operating_Netback: {Operating_Netback:,.2f} $/BOE - Operating Netback")

#Calculate 5-year Cash flows
Net_Revenue_Year_1 = Net_Revenue 

increase_rate = 0.10       #assumes our cash flow increases by 10% yearly for the next 5 years since we will be adding new wells onstream 

Five_Year_CashFlow = [Net_Revenue_Year_1 * (1 + increase_rate)**Year for Year in range(6)]

for Year, Five_Year_CashFlow in enumerate(Five_Year_CashFlow): 

    print(f"Year {Year}: ${Five_Year_CashFlow:,.2f}")

#Profitability Indicators 

NetPresentValue_NPV = Five_Year_CashFlow / ((1+0.1)**1)

Payout = CAPEX / Five_Year_CashFlow

ReturnOnInvetnment_ROI = Five_Year_CashFlow / CAPEX 

Expected_Ultimate_Recovery_EUR_Low_Case = PDP_Reserves_Add*0.35        #Assumes a 35% Recovery factor of Low Case PDP Reserves 

Expected_Ultimate_Recovery_EUR_High_Case = PPPPDP_Reserves_Add * 0.45    #Assumes a 45% Recovery factor of High Case P+P+PDP Reserves add 

case = "PDP"    #Use if calculating F&D costs based on Low case EUR

case = "P+P+PDP"   #Use if calculating F&D costs based on High case EUR

if case == "PDP":
    Finding_Development_FDCosts = CAPEX / Expected_Ultimate_Recovery_EUR_Low_Case
    print(f"Using PDP case: EUR = {Expected_Ultimate_Recovery_EUR_Low_Case} $/BOE")

else: 
    Finding_Development_FDCosts = CAPEX / Expected_Ultimate_Recovery_EUR_High_Case
    print(f"Using PDP case: EUR = {Expected_Ultimate_Recovery_EUR_High_Case} $/BOE")

Recycle_Ratio = OPEX / Finding_Development_FDCosts                #The recycle ratio is used to measure the profitability of a company's reinvestment effots by comparing netback per barrel to the cost of finding and developing reserves. 

CAPEX_per_FlowingBarrels = CAPEX / Yearly_Average_Production      #This metric calculates the CAPEX required to add one barreil of daily production capacity

print(f"NetPresentValue_NPV: {NetPresentValue_NPV:,.2f} $ - Net Present Value")

print(f"Payout: {Payout:,.2f} months - Payout")

print(f" Return on Investment: {ReturnOnInvetnment_ROI:,.2f} - Return on Investment")

print(f"Finding & Development Costs: {Finding_Development_FDCosts:,.2f} $/BOE - Finding & Development Costs")

print(f"Recycle Ration: {Recycle_Ratio:,.2f} - Recycle Ratio")

print(f"CAPEX per Flowing Barrels: {CAPEX_per_FlowingBarrels:,.2f} $/BOE - CAPEX / Flowing Barrels")
