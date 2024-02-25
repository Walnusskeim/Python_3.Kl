from Aktien_Classes import Player, Stock, LowRiskStock, MedRiskStock, HighRiskStock

### Market###

Market = []
Market.append(LowRiskStock("PhillipsFischereiAG", 230))
Market.append(LowRiskStock("StableBankingAG", 230))
Market.append(LowRiskStock("ReliableUtilitiesAG", 230))
Market.append(MedRiskStock("MaximalGerüstbauAG", 500))
Market.append(MedRiskStock("DynamicTechAG", 500))
Market.append(MedRiskStock("ProgressiveAutoAG", 500))
Market.append(HighRiskStock("R&B RechtskanzleiAG", 727))
Market.append(HighRiskStock("VolatileCryptoAG", 727))
Market.append(HighRiskStock("RiskyStartUpAG", 727))


Market[0].desc = "Fischerei"
Market[1].desc = "Banking"
Market[2].desc = "Utilities"
Market[3].desc = "Gerüstbau"
Market[4].desc = "Tech"
Market[5].desc = "Auto"
Market[6].desc = "Rechtskanzlei"
Market[7].desc = "Crypto"
Market[8].desc = "StartUp"



### Player##
name = "Testosteronus Maximus"
Pl = Player(name, 1000)



for st in Market:
    st.update_current_value()

for st in Market:
    print(st.name, end = ": ")
    print(st.current_value)