# DataMagus
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/alazia/datamagus/main/datamagus.py) [![PyPI](https://img.shields.io/badge/PyPI-0.0.3-green)](https://pypi.org/project/datamagus/)

Packages and API interface for basic data analysis processing, graphing and modeling, and practical use.


## Installation
```
pip install datamagus
```
## Model
The datamagus model module contains several analysis models, including RFM, Pareto, etc.

#### Pareto (ABC)
```python
>>> np.random.seed(1)
>>> a = np.random.randint(110000,120000,2)
>>> b = np.random.randint(20000, 80000, 3)
>>> c = np.random.randint(2000, 8000, 5)
>>> df = pd.DataFrame({
'id': np.arange(1, 11),
'M':np.append(np.append(a,b),c)
})
>>> pm=ParetoModel()
>>> pm.load_data(df)
>>> pm.unleash()
>>> pm.res
    id         M  Accumulate  Percent Class
0   2  115192.0    115192.0   26.37%     A
1   1  110235.0    225427.0   51.60%     A
2   4   70057.0    295484.0   67.64%     A
3   5   63723.0    359207.0   82.23%     B
4   3   52511.0    411718.0   94.25%     C
5   7    7056.0    418774.0   95.87%     C
6   9    6225.0    424999.0   97.29%     C
7   6    4895.0    429894.0   98.41%     C
8  10    4797.0    434691.0   99.51%     C
9   8    2144.0    436835.0  100.00%     C
>>> pm.results[1]
                                ID Count_Percent Money_Percent
Class                                                           
A                      '2', '1', '4'        30.00%        67.64%
B                                '5'        10.00%        14.59%
C      '3', '7', '9', '6', '10', '8'        60.00%        17.77%
>>> pm.visualize()
```
<img src="https://raw.githubusercontent.com/Alazia/datamagus/main/data/pic/Pareto_plot.png" width="50%">

