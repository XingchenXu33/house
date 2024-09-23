import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# Load the data

df = pd.read_csv('housing.csv')

# Set the title of the app
st.title('California Housing Data (1990) Xingchen Xu')

# Price Slider
min_price = 0
max_price = int(df['median_house_value'].max())
price_filter = st.slider('Minimal Median House Price', min_price, max_price, min_price)


location_filter = st.sidebar.multiselect(
     'Capital Selector',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())

income_level=st.sidebar.radio(
    "Select income level:",
    ('Low','Medium','High')
)
if income_level =='Low(<=2.5)':
    filtered_df=df[df['median_income']<=2.5]
elif income_level=='Medium(>2.5&4.5)':
    filtered_df=df[(df['median_income']>2.5)&(df['median_income']<4.5)]
else:
    filtered_df=df[df['median_income']>4.5]
if location_filter:
    filtered_data = df[df.ocean_proximity.isin(location_filter)]
else:
    filtered_data = df


# Filter the data based on the slider
filtered_data = df[df['median_house_value'] >= price_filter]

df=df[df.ocean_proximity.isin(location_filter)]

# Show filtered data on a map (if you have latitude/longitude in your dataset)
if 'longitude' in df.columns and 'latitude' in df.columns:
    st.map(filtered_data[['latitude', 'longitude']])


# 创建直方图
fig, ax = plt.subplots()


# 筛选出 median_house_value 在 200000 到 500000 之间的数据
filtered_data = df[(df['median_house_value'] >= 200000) & (df['median_house_value'] <= 500000)]

# 绘制筛选后的直方图，设置 30 个区间
plt.hist(filtered_data['median_house_value'], bins=30)

ax.set_xlabel('Median House Value')
ax.set_ylabel('Frequency')
ax.set_title('Distribution of Median House Value')

# 显示直方图
st.pyplot(fig)
plt.grid(True)
fig, ax = plt.subplots()


