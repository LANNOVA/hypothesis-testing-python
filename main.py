from scipy import stats
 
def normal_test(df):
    min_value = df['cosine_similarity'].min()
    max_value = df['cosine_similarity'].max() # для расчета интервалов
    print(df.head())
    bin_count = int(np.ceil(np.log2(len(df))) + 1) # кол-во интервалов
    step = (max_value - min_value) / bin_count
    bins = [min_value]
    for i in range(bin_count-1): # цикл расчета границ интервалов
        bins.append(bins[-1]+step)
    bins.append(max_value)
    frequencies = pd.cut(df["cosine_similarity"], bins).value_counts(sort=False) # расчет частот
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
