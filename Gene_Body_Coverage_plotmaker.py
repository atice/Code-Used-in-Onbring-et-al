#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
import statistics
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = defaultdict(list)
for line in open('input_data'):
    sline = line.split(',')
    name = sline[0]
    for i in sline[1:]:
        data[name].append(float(i.strip()))
data = dict(data)


# In[3]:


repl_dict = {}
for name, values in data.items():
    identity = name.split('_')[1]
    if identity not in repl_dict:
        repl_dict[identity] = np.array(values)
    else:
        repl_dict[identity] += np.array(values)


# In[4]:


for identity, values in repl_dict.items():
    if identity == 'BP':
        repl_dict[identity] = repl_dict[identity]/7
    else:
        repl_dict[identity] = repl_dict[identity]/8


# In[7]:


full_names = {'BP': 'Biotin Primers', 'Cont': 'Control', 'HR': 'Half Reaction', 'FT': 'Freeze Thaw', 'AC': 'All Changes', 'IH': 'In-House Beans', 'odT': '1um oligo-dT'}


# In[14]:


for identity, values in repl_dict.items():
    plt.plot(values, label=full_names[identity])

plt.legend(prop={'size': 8})    
plt.ylabel('Coverage')
plt.xlabel("Gene body percentile (5'->3')")
plt.savefig('giardia_gene_body_cov.svg')

