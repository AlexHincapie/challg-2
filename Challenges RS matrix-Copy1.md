```python
import pandas as pd
import numpy as np
```


```python
Data = pd.read_csv('C:/Users/steff/OneDrive/Documents/Python Scripts/CHALL RS ALL_INTERACTIONS.csv')
Data['USER_ID'] = Data['USER_ID'].astype('str')
Data['CH_ID'] = Data['CH_ID'].astype('str')

users = Data['USER_ID'].unique() 
challenges = Data['CH_ID'].unique()
```


```python
Data
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>USER_ID</th>
      <th>CH_ID</th>
      <th>ALL_INTERACTIONS</th>
      <th>UPLOADED_DAYS_AGO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>CH_1</td>
      <td>7</td>
      <td>365</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>CH_2</td>
      <td>4</td>
      <td>361</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>CH_3</td>
      <td>11</td>
      <td>357</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>CH_4</td>
      <td>2</td>
      <td>353</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>CH_5</td>
      <td>5</td>
      <td>349</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>9995</th>
      <td>100</td>
      <td>CH_96</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9996</th>
      <td>100</td>
      <td>CH_97</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9997</th>
      <td>100</td>
      <td>CH_98</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9998</th>
      <td>100</td>
      <td>CH_99</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>9999</th>
      <td>100</td>
      <td>CH_100</td>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>10000 rows × 4 columns</p>
</div>




```python
m7= Data.pivot_table(index=["USER_ID"],columns=["CH_ID"],values=["ALL_INTERACTIONS"])
```


```python
m7
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="21" halign="left">ALL_INTERACTIONS</th>
    </tr>
    <tr>
      <th>CH_ID</th>
      <th>CH_1</th>
      <th>CH_10</th>
      <th>CH_100</th>
      <th>CH_11</th>
      <th>CH_12</th>
      <th>CH_13</th>
      <th>CH_14</th>
      <th>CH_15</th>
      <th>CH_16</th>
      <th>CH_17</th>
      <th>...</th>
      <th>CH_90</th>
      <th>CH_91</th>
      <th>CH_92</th>
      <th>CH_93</th>
      <th>CH_94</th>
      <th>CH_95</th>
      <th>CH_96</th>
      <th>CH_97</th>
      <th>CH_98</th>
      <th>CH_99</th>
    </tr>
    <tr>
      <th>USER_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>5</td>
      <td>6</td>
      <td>4</td>
      <td>3</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
      <td>9</td>
      <td>7</td>
      <td>5</td>
      <td>4</td>
      <td>9</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>8</td>
      <td>10</td>
      <td>9</td>
      <td>10</td>
      <td>5</td>
      <td>11</td>
      <td>8</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>10</td>
      <td>4</td>
      <td>2</td>
      <td>2</td>
      <td>7</td>
      <td>9</td>
      <td>7</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>6</td>
      <td>7</td>
      <td>6</td>
      <td>4</td>
      <td>5</td>
      <td>6</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>8</td>
      <td>...</td>
      <td>9</td>
      <td>5</td>
      <td>1</td>
      <td>3</td>
      <td>9</td>
      <td>7</td>
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>10</td>
      <td>3</td>
      <td>8</td>
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>9</td>
      <td>7</td>
      <td>7</td>
      <td>...</td>
      <td>8</td>
      <td>4</td>
      <td>6</td>
      <td>7</td>
      <td>10</td>
      <td>6</td>
      <td>8</td>
      <td>5</td>
      <td>6</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>8</td>
      <td>7</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>2</td>
      <td>9</td>
      <td>6</td>
      <td>7</td>
      <td>5</td>
      <td>...</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>7</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>6</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>96</th>
      <td>7</td>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>4</td>
      <td>5</td>
      <td>10</td>
      <td>7</td>
      <td>9</td>
      <td>...</td>
      <td>5</td>
      <td>7</td>
      <td>5</td>
      <td>0</td>
      <td>6</td>
      <td>9</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>3</td>
    </tr>
    <tr>
      <th>97</th>
      <td>6</td>
      <td>3</td>
      <td>11</td>
      <td>11</td>
      <td>9</td>
      <td>6</td>
      <td>7</td>
      <td>9</td>
      <td>4</td>
      <td>3</td>
      <td>...</td>
      <td>2</td>
      <td>3</td>
      <td>8</td>
      <td>2</td>
      <td>9</td>
      <td>4</td>
      <td>6</td>
      <td>6</td>
      <td>8</td>
      <td>8</td>
    </tr>
    <tr>
      <th>98</th>
      <td>8</td>
      <td>8</td>
      <td>4</td>
      <td>11</td>
      <td>3</td>
      <td>6</td>
      <td>7</td>
      <td>3</td>
      <td>8</td>
      <td>4</td>
      <td>...</td>
      <td>9</td>
      <td>2</td>
      <td>9</td>
      <td>6</td>
      <td>3</td>
      <td>8</td>
      <td>6</td>
      <td>7</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>99</th>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>8</td>
      <td>7</td>
      <td>7</td>
      <td>2</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>...</td>
      <td>4</td>
      <td>5</td>
      <td>9</td>
      <td>7</td>
      <td>9</td>
      <td>4</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>3</td>
    </tr>
    <tr>
      <th>100</th>
      <td>6</td>
      <td>7</td>
      <td>6</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>4</td>
      <td>5</td>
      <td>7</td>
      <td>3</td>
      <td>...</td>
      <td>8</td>
      <td>7</td>
      <td>8</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>6</td>
      <td>5</td>
      <td>9</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 100 columns</p>
</div>




```python
m7.shape
```




    (100, 100)




```python

```


```python

```


```python

```


```python

```


```python

```


```python

```
