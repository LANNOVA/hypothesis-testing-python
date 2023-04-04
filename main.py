from scipy import stats
 
def normal_test(df):
    min_value = df['cosine_similarity'].min()
    max_value = df['cosine_similarity'].max() 
    print(df.head())
    bin_count = int(np.ceil(np.log2(len(df))) + 1)
    step = (max_value - min_value) / bin_count
    bins = [min_value]
    for i in range(bin_count-1): 
        bins.append(bins[-1]+step)
    bins.append(max_value)
    frequencies = pd.cut(df["cosine_similarity"], bins).value_counts(sort=False) 
    print(frequencies)
    return stats.normaltest(frequencies.to_numpy())
    
    
    
k2, p = normal_test(cos_distances_not_mus_df)
 
significance_level = 0.05
print(pvalue)
print("p value: " + str(pvalue)) 
print("k2 value: " + str(k2)) 
if pvalue <= significance_level: 
    print('Reject NULL HYPOTHESIS') 
else: 
    print('ACCEPT NULL HYPOTHESIS') 
    
k2, p = normal_test(cos_distances_mus_df)
 
significance_level = 0.05
print(pvalue)
print("p value: " + str(pvalue)) 
print("k2 value: " + str(k2)) 
if pvalue <= significance_level: 
    print('Reject NULL HYPOTHESIS') 
else: 
    print('ACCEPT NULL HYPOTHESIS') 
  
 # DONATE SRAVstudios
"""
**BTC** - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

**USDT(ETH)**  - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

**USDT(SOLANA)**  - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

**USDT(POLYGON)**  - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

**ETH**  - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
"""
