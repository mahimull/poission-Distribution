#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[2]:


from IPython.display import Math, Latex


# In[3]:


from IPython.core.display import Image


# In[4]:


import seaborn as sns


# In[5]:


sns.set(color_codes=True)


# In[ ]:


sns.set(rc={'figure.figsize':(5,5)})


# # 1. Uniform Distribution

# In[7]:


from scipy.stats import uniform


# In[20]:


n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)


# In[21]:


ax = sns.distplot(data_uniform,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')


# # 2. Normal Distribution

# In[22]:


from scipy.stats import norm


# In[23]:


data_normal = norm.rvs(size=10000,loc=0,scale=1)


# In[26]:


ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True,
                  color='skyblue',
                  hist_kws={"linewidth": 10,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')


# # 3. Gamma Distribution

# In[30]:


from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=1000)


# In[32]:


ax = sns.distplot(data_gamma,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 10,'alpha':1})
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')


# # 4. Exponential Distribution

# In[42]:


from scipy.stats import expon
data_expon = expon.rvs(scale=1,loc=0,size=10000)


# In[46]:


ax = sns.distplot(data_expon,
                  kde=True,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Exponential Distribution', ylabel='Frequency')


# # 5. Poisson Distribution

# In[47]:


from scipy.stats import poisson
data_poisson = poisson.rvs(mu=3, size=10000)


# In[53]:


ax = sns.distplot(data_poisson,
                  bins=30,
                  kde=False,
                  color='black',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Poisson Distribution', ylabel='Frequency')


# # 6. Binomial Distribution

# In[54]:


from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=10000)


# In[55]:


ax = sns.distplot(data_binom,
                  kde=False,
                  color='skyblue',
                  hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Binomial Distribution', ylabel='Frequency')


# # 7. Bernoulli Distribution

# In[56]:


from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)


# In[57]:


ax= sns.distplot(data_bern,
                 kde=False,
                 color="skyblue",
                 hist_kws={"linewidth": 15,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')


# In[ ]:




