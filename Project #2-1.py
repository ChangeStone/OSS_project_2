#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd

data_df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

data_2015 = data_df.loc[data_df['year'] == 2015]
data_2016 = data_df.loc[data_df['year'] == 2016]
data_2017 = data_df.loc[data_df['year'] == 2017]
data_2018 = data_df.loc[data_df['year'] == 2018]

H_2015 = data_2015.loc[:,['batter_name','H','p_year']]
H_2016 = data_2016.loc[:,['batter_name','H','p_year']]
H_2017 = data_2017.loc[:,['batter_name','H','p_year']]
H_2018 = data_2018.loc[:,['batter_name','H','p_year']]

H_2015_sort = H_2015.sort_values(by='H', ascending=False)
H_2016_sort = H_2016.sort_values(by='H', ascending=False)
H_2017_sort = H_2017.sort_values(by='H', ascending=False)
H_2018_sort = H_2018.sort_values(by='H', ascending=False)

H_2015_top10 = H_2015_sort[:10]
H_2015_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
H_2016_top10 = H_2016_sort[:10]
H_2016_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
H_2017_top10 = H_2017_sort[:10]
H_2017_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
H_2018_top10 = H_2018_sort[:10]
H_2018_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']

avg_2015 = data_2015.loc[:,['batter_name','avg','p_year']]
avg_2016 = data_2016.loc[:,['batter_name','avg','p_year']]
avg_2017 = data_2017.loc[:,['batter_name','avg','p_year']]
avg_2018 = data_2018.loc[:,['batter_name','avg','p_year']]

avg_2015_sort = avg_2015.sort_values(by='avg', ascending=False)
avg_2016_sort = avg_2016.sort_values(by='avg', ascending=False)
avg_2017_sort = avg_2017.sort_values(by='avg', ascending=False)
avg_2018_sort = avg_2018.sort_values(by='avg', ascending=False)

avg_2015_top10 = avg_2015_sort[:10]
avg_2015_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
avg_2016_top10 = avg_2016_sort[:10]
avg_2016_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
avg_2017_top10 = avg_2017_sort[:10]
avg_2017_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
avg_2018_top10 = avg_2018_sort[:10]
avg_2018_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']

HR_2015 = data_2015.loc[:,['batter_name','HR','p_year']]
HR_2016 = data_2016.loc[:,['batter_name','HR','p_year']]
HR_2017 = data_2017.loc[:,['batter_name','HR','p_year']]
HR_2018 = data_2018.loc[:,['batter_name','HR','p_year']]

HR_2015_sort = HR_2015.sort_values(by='HR', ascending=False)
HR_2016_sort = HR_2016.sort_values(by='HR', ascending=False)
HR_2017_sort = HR_2017.sort_values(by='HR', ascending=False)
HR_2018_sort = HR_2018.sort_values(by='HR', ascending=False)

HR_2015_top10 = HR_2015_sort[:10]
HR_2015_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
HR_2016_top10 = HR_2016_sort[:10]
HR_2016_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
HR_2017_top10 = HR_2017_sort[:10]
HR_2017_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
HR_2018_top10 = HR_2018_sort[:10]
HR_2018_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']

OBP_2015 = data_2015.loc[:,['batter_name','OBP','p_year']]
OBP_2016 = data_2016.loc[:,['batter_name','OBP','p_year']]
OBP_2017 = data_2017.loc[:,['batter_name','OBP','p_year']]
OBP_2018 = data_2018.loc[:,['batter_name','OBP','p_year']]

OBP_2015_sort = OBP_2015.sort_values(by='OBP', ascending=False)
OBP_2016_sort = OBP_2016.sort_values(by='OBP', ascending=False)
OBP_2017_sort = OBP_2017.sort_values(by='OBP', ascending=False)
OBP_2018_sort = OBP_2018.sort_values(by='OBP', ascending=False)

OBP_2015_top10 = OBP_2015_sort[:10]
OBP_2015_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
OBP_2016_top10 = OBP_2016_sort[:10]
OBP_2016_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
OBP_2017_top10 = OBP_2017_sort[:10]
OBP_2017_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']
OBP_2018_top10 = OBP_2018_sort[:10]
OBP_2018_top10.index = ['Top1', 'Top2', 'Top3', 'Top4', 'Top5', 'Top6', 'Top7', 'Top8', 'Top9', 'Top10']

print(H_2015_top10)
print(H_2016_top10)
print(H_2017_top10)
print(H_2018_top10)

print(avg_2015_top10)
print(avg_2016_top10)
print(avg_2017_top10)
print(avg_2018_top10)

print(HR_2015_top10)
print(HR_2016_top10)
print(HR_2017_top10)
print(HR_2018_top10)

print(OBP_2015_top10)
print(OBP_2016_top10)
print(OBP_2017_top10)
print(OBP_2018_top10)


# In[14]:


data_catcher = data_2018.loc[data_df['cp'] == '포수']
data_first = data_2018.loc[data_df['cp'] == '1루수']
data_second = data_2018.loc[data_df['cp'] == '2루수']
data_third = data_2018.loc[data_df['cp'] == '3루수']
data_short = data_2018.loc[data_df['cp'] == '유격수']
data_left = data_2018.loc[data_df['cp'] == '좌익수']
data_center = data_2018.loc[data_df['cp'] == '중견수']
data_right = data_2018.loc[data_df['cp'] == '우익수']

data_catcher = data_catcher.loc[:,['batter_name','war','cp']]
data_first = data_first.loc[:,['batter_name','war','cp']]
data_second = data_second.loc[:,['batter_name','war','cp']]
data_third = data_third.loc[:,['batter_name','war','cp']]
data_short = data_short.loc[:,['batter_name','war','cp']]
data_left = data_left.loc[:,['batter_name','war','cp']]
data_center = data_center.loc[:,['batter_name','war','cp']]
data_right = data_right.loc[:,['batter_name','war','cp']]

data_catcher = data_catcher.sort_values(by='war', ascending=False)
data_first = data_first.sort_values(by='war', ascending=False)
data_second = data_second.sort_values(by='war', ascending=False)
data_third = data_third.sort_values(by='war', ascending=False)
data_short = data_short.sort_values(by='war', ascending=False)
data_left = data_left.sort_values(by='war', ascending=False)
data_center = data_center.sort_values(by='war', ascending=False)
data_right = data_right.sort_values(by='war', ascending=False)

print(data_catcher[:1])
print(data_first[:1])
print(data_second[:1])
print(data_third[:1])
print(data_short[:1])
print(data_left[:1])
print(data_center[:1])
print(data_right[:1])


# In[15]:


Cor = data_df.loc[:,['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]

Corp = Cor.corr(method='pearson')
Corp = Corp.loc[:,['salary']]
Corp = Corp.sort_values(by='salary',ascending=False)
Corp = Corp[1:2]

Cork = Cor.corr(method='kendall')
Cork = Cork.loc[:,['salary']]
Cork = Cork.sort_values(by='salary',ascending=False)
Cork = Cork[1:2]

Cors = Cor.corr(method='spearman')
Cors = Cors.loc[:,['salary']]
Cors = Cors.sort_values(by='salary',ascending=False)
Cors = Cors[1:2]

print(Corp)
print(Cork)
print(Cors)

print("위 결과에 따라 RBI(타점)이 salary(연봉)에 가장 높은 상관관계를 가진다.")


# In[ ]:




