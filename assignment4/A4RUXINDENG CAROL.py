
# coding: utf-8

# # Titanic passenger dataset

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns

df = pd.read_csv('train.csv', header = 0)


# ##In this process I want to figure out and compare the variables of Pclass, Age, Gender.To see which one more easier to survived.

# In[12]:


##survived number and rate

sns.countplot(x='Survived',data=titanic)
sur_num=df['Survived'].sum()
deathtoll = 891 - sur_num

labels = 'Survived', 'death'
sizes = [deathtoll,sur_num]
explode = (0, 0.1,) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title('survival rate and mortality') 

plt.show()


# # survived passengers of total

# In[8]:


##Compare the survival rate of different passenger’s class

tr = pd.DataFrame()

tr['PassengerNum'] = titanic[['Pclass','Survived']].groupby(['Pclass'])['Survived'].count()
tr['Pclass'] = tr.index.values
tr['Survived'] = titanic[['Pclass','Survived']].groupby(['Pclass'])['Survived'].sum()
tr['Ratio'] = tr.Survived / tr.PassengerNum * 100

fig = plt.figure()

ax = fig.add_subplot(111)
width = 0.7

tr.Survived.plot(kind='line', color='red', ax=ax, label = 'Survived Passenger', xticks = tr['Pclass'])
tr.PassengerNum.plot(kind='line', color='blue', ax=ax, label = 'Total Passenger')
ax.legend()

ax.scatter(tr.Pclass,tr.Survived, color='red')
ax.scatter(tr.Pclass,tr.PassengerNum, color='blue')

plt.show()
tr


# # Pclass

# In[9]:


##Divided age into 3 group: children (<18) , aldult(18-65) and elderly (65+).
##Compare the survival rate of different assenger’s ages


df = pd.read_csv('train.csv', header = 0)


##children (<18)
Survived = df.loc[(df["Survived"] == 1) & (df["Age"] < 18)].Sex.count()
Died = df.loc[(df["Survived"] == 0) & (df["Age"] < 18)].Sex.count()

labels = 'Survived (<18)', 'Died (<18)'
sizes = [Survived, Died]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')



##aldult(18-65)
Survived = df.loc[(df["Survived"] == 1) & (df["Age"][18:65])].Sex.count()
Died = df.loc[(df["Survived"] == 0) & (df["Age"][18:65])].Sex.count()

labels = 'Survived (18:65)', 'Died (18:65)'
sizes = [Survived, Died]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')


##elderly (65+)
Survived = df.loc[(df["Survived"] == 1) & (df["Age"] > 65)].Sex.count()
Died = df.loc[(df["Survived"] == 0) & (df["Age"] > 65)].Sex.count()

labels = 'Survived (>65)', 'Died (>65)'
sizes = [Survived, Died]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')


plt.show()


# # Age

# In[10]:


#The number of men and women alive and the proportion of men and women 
survived_df = titanic[titanic[ 'Survived'] == 1 ]
survived_male_sum = survived_df['Sex'][survived_df['Sex'] == 'male'].count()
survived_female_sum = survived_df['Sex'][survived_df['Sex'] == 'female'].count()
print(survived_male_sum, survived_female_sum)
plt.figure(figsize=(10,5))
plt.subplot(121)
sns.countplot(x='Sex', data=survived_df)
plt.subplot(122)
plt.pie([survived_male_sum, survived_female_sum],        labels=['male', 'female'],autopct='%1.0f%%')
plt.show()


# # Gender

# # Conclusion
# From all of the analysis above we can see the relationship of these three variables,gender is more likely to determine the survival rate, and the survival rate of women is much higher than that of men. PClass also influence the survival rate, just a little less than the variable of gender. Finally, the survival rate of the age between 18 to 65 years of survival is also higher.
