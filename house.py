import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# Load the data
# Set the title of the app
st.title('California Housing Data (1990) Xingchen Xu')

df = pd.read_csv('housing.csv')
# Price Slider
min_price = 0
max_price = int(df['median_house_value'].max())
price_filter = st.slider('Minimal Median House Price', min_price, max_price, min_price)

location_filter = st.sidebar.multiselect(
     'location Selector',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())

#if location_filter:
    #filtered_data = df[df.ocean_proximity.isin(location_filter)]
#else:
    #filtered_data = df

# 创建 radio 按钮选择收入级别
income_level=st.sidebar.radio(
    "Select income level:",
    ('Low','Medium','High')
)

# 筛选出 median_house_value 在 200000 到 500000 之间的数据
#df = df[(df['median_house_value'] >= 200000) & (df['median_house_value'] <= 500000)]

# 根据选择过滤数据
if income_level == 'Low':
    df = df[df['median_income'] <= 2.5]
elif income_level == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
else:
    df = df[df['median_income'] > 4.5]

# Filter the data based on the slider
df = df[df['median_house_value'] >= price_filter]

df=df[df['ocean_proximity'].isin(location_filter)]

st.map(df)
# Show filtered data on a map (if you have latitude/longitude in your dataset)
#if 'longitude' in df.columns and 'latitude' in df.columns:
   #st.map(filtered_data[['latitude', 'longitude']])




# 创建直方图
fig, ax = plt.subplots()


# 绘制筛选后的直方图，设置 30 个区间
plt.hist(df['median_house_value'], bins=30,)

ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Median House Value')

# 显示直方图
st.pyplot(fig)
fig, ax = plt.subplots()


