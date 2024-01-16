#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
file_path = r'C:\Users\NIHAAL\Downloads\data.csv'
df = pd.read_csv(file_path)

# Sidebar - Slicers
selected_campaign = st.sidebar.selectbox('Select Campaign', df['campaign'].unique())
selected_age = st.sidebar.selectbox('Select Age Group', df['age'].unique())
selected_gender = st.sidebar.selectbox('Select Gender', df['gender'].unique())

# Filter the data based on the selected slicers
filtered_df = df[(df['campaign'] == selected_campaign) & (df['age'] == selected_age) & (df['gender'] == selected_gender)]

# Main content
st.title('Facebook Ad Campaign Dashboard')

# Display the filtered data
st.write(f"### Data for {selected_campaign} Campaign, Age Group {selected_age}, Gender {selected_gender}")
st.dataframe(filtered_df)

# Line chart - Impressions, Clicks, Spent
st.line_chart(filtered_df.set_index('date')[['Impressions', 'Clicks', 'Spent']])

# Bar chart - Total Conversion and Approved Conversion
st.bar_chart(filtered_df.groupby('date')[['Total_Conversion', 'Approved_Conversion']].sum())

# Pie chart - Distribution of Approved Conversion
fig_pie = px.pie(filtered_df, names='Approved_Conversion', title='Distribution of Approved Conversion')
st.plotly_chart(fig_pie)

# Scatter plot - Spent vs. Clicks
fig_scatter = px.scatter(filtered_df, x='Spent', y='Clicks', color='Total_Conversion', size='Impressions',
                         title='Spent vs. Clicks with Total Conversion as Color')
st.plotly_chart(fig_scatter)

# Additional visualizations or insights can be added based on your requirements

# You can run this script by saving it as a .py file and then running:
# streamlit run filename.py


#  #                                    045035_DEV-II (TERM-02) PROJECT-02

# #                                           REPORT-ANALYSIS 
# ###                                                                              ON 
# #                                      "Facebook Ad Campaign"

# ### OBJECTIVE -:
# 
# **Overall:**
# 
# Evaluate the effectiveness of your Facebook ad campaign and identify areas for improvement.
# 
# **Specific Objectives:**
# 
# **1. Assess Campaign Performance:**
# 
# **Measure key metrics:** Analyze impressions, reach, clicks, engagement, conversions, and cost per acquisition (CPA).
# **Compare performance to goals:** Determine if the campaign achieved its intended objectives (e.g., increased brand awareness, website traffic, sales).
# **Identify trends and patterns:** Analyze data over time to understand how the campaign performed at different stages.
# 
# **2. Analyze Targeting Effectiveness:**
# 
# **Evaluate audience demographics:** Assess the effectiveness of targeting based on age, gender, location, interests, and other demographic factors.
# 
# **Identify high-performing segments:** Determine which audience segments generated the most engagement and conversions.
# 
# **Refine targeting strategy:** Based on insights, recommend adjustments to targeting parameters for future campaigns.
# 
# **3. Optimise Ad Creative and Messaging:**
# 
# **Analyze ad performance by format:** Compare the effectiveness of different ad formats (e.g., images, videos, carousels) and messaging styles.
# 
# **Identify resonating elements:** Determine which ad elements (e.g., visuals, headlines, calls to action) generated the most clicks and conversions.
# 
# **Develop creative recommendations:** Based on insights, suggest improvements to ad creative and messaging for future campaigns.
# 
# **4. Cost Optimization:**
# 
# **Analyze campaign budget allocation:** Evaluate the effectiveness of budget distribution across different ad sets and targeting parameters.
# 
# **Identify cost-saving opportunities:** Recommend strategies to reduce campaign costs while maintaining performance.
# 
# **Develop bidding optimization recommendations:** Suggest bidding strategies to improve campaign efficiency and maximize ROI.
# 
# **Managerial Report Writing:**
# 
# Present key findings and insights in a clear and concise manner.
# Focus on actionable recommendations for improving future campaigns.
# Tailor the report to the specific needs and interests of your manager or stakeholders.
# Include data visualizations and charts to support your findings.
# Quantify the potential impact of recommended changes.
# 
# **Additional Considerations:**
# 
# Align analysis objectives with overall business goals.
# Use industry benchmarks to compare campaign performance.
# Consider external factors that may have influenced campaign results.
# Be prepared to answer questions and address concerns from stakeholders.
# 
# 

# ### BRIEF DESCRIPTION OF DATA SET -:
# 
# **Data Overview-:**
# 
# The data set appears to be a screenshot of a Facebook ad campaign report. It shows performance data for one of the three campaign called "Campaign B" from January 24, 2021, to March 21, 2021. The data includes the following columns:
# 
# **Date:** The date the ad was shown
# **ad_id:** The unique identifier for the ad
# **campaign:** The name of the campaign
# **fb_campaign_id:** The Facebook campaign ID
# **age:** The age range of the targeted audience
# **gender:** The gender of the targeted audience
# **interest:** The interests of the targeted audience
# **Impressions:** The number of times the ad was shown
# **Clicks:** The number of times someone clicked on the ad
# **Spent:** The amount of money spent on the ad
# **Total_Conversion:** The number of conversions that occurred from the ad
# **Approved_Conversion:** The number of conversions that were approved
# 
# **Observations-:**
# 
# The campaign reached a total of 524,274 people over the two-month period.
# The total number of clicks was 81,460, with a click-through rate (CTR) of 15.54%.
# The total cost of the campaign was $20.29, with a cost per click (CPC) of $0.25.
# The total number of conversions was 14, with a conversion rate of 0.17%.
# The data shows that the campaign was most successful in reaching women aged 30-34.
# The most successful ad in terms of clicks and conversions was shown on January 29, 2021.
# 
# **Analysis-:**
# 
# Based on these observations, it appears that the Facebook ad campaign was relatively successful in reaching its target audience and generating clicks. However, the conversion rate was low. This could be due to a number of factors, such as:
# 
# **The ad creative may not have been effective in converting clicks into conversions.**
# **The landing page may not have been optimized for conversions.**
# **The offer may not have been compelling enough.**
# 

# ### OBSERVATIONS-:
# 
# #### Dashboard View-:
# 

# ![Screenshot%202024-01-16%20215334.png](attachment:Screenshot%202024-01-16%20215334.png)

# ![Screenshot%202024-01-16%20225617.png](attachment:Screenshot%202024-01-16%20225617.png)

# ##### OBSERVATION -01

# ![Screenshot%202024-01-16%20220752.png](attachment:Screenshot%202024-01-16%20220752.png)

# 
# 
# **Overall Trends:** All three metrics appear to be **increasing** over time. This suggests that the organization is reaching a larger audience and spending more on its marketing efforts.
# 
# **Clicks and Impressions:** The **Clicks** line appears to be **tracking closely** with the **Impressions** line, which suggests that the organization's ads are effective at generating interest from viewers.
# * **Spent:** The **Spent** line appears to be **increasing at a faster rate** than the Clicks and Impressions lines. This could be due to a number of factors, such as rising advertising costs or the organization increasing its bids for ad placements.
# * **Seasonality:** There appears to be some **seasonality** in the data, with Clicks, Impressions, and Spent all dipping in the first few months of each year. This could be due to a number of factors, such as decreased spending during the holiday season or changes in consumer behavior.
# 
# The x-axis labels appear to be dates, but they are not evenly spaced. This makes it difficult to compare the performance of the campaign across different time periods.
# The y-axis labels are not visible in the image. This makes it difficult to know the scale of the metrics being measured.
# There is no legend in the image. This makes it difficult to tell which line corresponds to which metric.
# 
# Overall, the image suggests that the organization's Facebook ad campaign is **performing well**.
# 

# ##### OBSERVATION -02

# ![Screenshot%202024-01-16%20220802.png](attachment:Screenshot%202024-01-16%20220802.png)

# **Overall Trend:** Both **Approved_Conversion** and **Total_Conversion** appear to be **increasing** over time. This suggests that the app is being downloaded by more users.
# 
# **Approved_Conversion vs. Total_Conversion:** The **Approved_Conversion** line is generally **below** the **Total_Conversion** line. This suggests that there is a **discrepancy** between the number of downloads that are counted as "approved" and the total number of downloads. This could be due to a number of factors, such as a lag in reporting, or different criteria for what constitutes an "approved" conversion.
# 
# **Specific Dates:** There are a few **spikes** in both lines on specific dates, such as January 5, 2021, and March 3, 2021. This suggests that there were periods of time when the app was downloaded by a significantly larger number of users.
# 
# **Additional details :-**
# The x-axis labels appear to be dates, but they are not evenly spaced. This makes it difficult to compare the performance of the app across different time periods.
# 
# The y-axis labels are not visible in the image. This makes it difficult to know the scale of the downloads being measured.
# 
# There is no legend in the image. This makes it difficult to tell which line corresponds to which category of downloads.
# 
# Overall, the app is being downloaded by more users over time.

# ##### OBSERVATION -03

# ![Screenshot%202024-01-16%20220835.png](attachment:Screenshot%202024-01-16%20220835.png)

# **Overall, the majority of approved conversions (63.9%) come from the "3" category.** This suggests that this category is the most effective at driving conversions for this campaign.
# 
# **The "2" category represents 33% of approved conversions.** This is significantly lower than the "3" category, but still a noteworthy portion of the overall conversions.
# 
# **The "1.03%-2.06%" category represents a small percentage of approved conversions (less than 3%).** This suggests that these categories are not as effective at driving conversions as the "3" and "2" categories.
# 
# **Additional -:**
# What do the numbers in the categories represent (e.g., age groups, purchase amounts, website clicks)?
# What is the timeframe for the data?
# What are the overall goals of the Facebook ad campaign?

# ##### OBSERVATION -04

# ![Screenshot%202024-01-16%20220853.png](attachment:Screenshot%202024-01-16%20220853.png)

# **Overall Trends:**
# 
# **Spent:** The **Spent** line appears to be **increasing** over time. This suggests that the organization is spending more on its marketing efforts.
# 
# **Clicks with Total Conversion as Color:** It's difficult to discern the trend for **Clicks with Total Conversion as Color** due to the way the data is presented. The color gradient used for "Total Conversion" makes it hard to see the underlying trend in the number of clicks.
# 
# **Specific Observations:**
# 
# The **Spent** line has several **fluctuations** throughout the timeframe. These could be due to various factors like seasonality, changes in campaign budget, or specific marketing initiatives.
# 
# **The color gradient for **Total Conversion** appears to be **concentrated towards the lower end**, suggesting that a majority of clicks have lower conversion rates. However, without knowing the exact values represented by the color gradient, it's difficult to draw specific conclusions.
# 
# **Additional notes:**
# 
# The x-axis labels appear to be dates, but they are not evenly spaced. This makes it difficult to compare the performance across different time periods.
# The y-axis labels are not visible in the image. This makes it difficult to know the scale of the metrics being measured.
# There is no legend in the image. This makes it unclear what the color gradient represents in terms of "Total Conversion."
# 
# Overall,the organization's spending on marketing is increasing, but it's difficult to assess the trend in clicks and the effectiveness of the campaign due to the limitations of the graph's presentation.
# 

# ### MANAGERIAL INSIGHTS -:

# **1. Overall Campaign Performance:**
# 
# **Positive:** The increasing trends in impressions, clicks, and conversions suggest the campaign is reaching a wider audience and generating results.
# **Areas for Improvement:** Despite the positive trends, the faster growth in spending compared to clicks and conversions indicates potential for optimization. Analyze cost-effectiveness of different ad formats and target segments to improve return on investment (ROI).
# **Seasonality:** Consider seasonal patterns and adjust campaign budgets or strategies accordingly.
# 
# **2. App Download Performance:**
# 
# **Growth:** The rising approved and total conversions indicate the app is gaining traction.
# **Discrepancy:** Investigate the reasons behind the difference between approved and total conversions. Is it due to delayed reporting, verification issues, or different definitions? Addressing this discrepancy can improve data accuracy and campaign optimization.
# **Spikes:** Analyze the factors behind the download spikes on specific dates. Were they due to targeted promotions, app updates, or external events? Understanding these drivers can help replicate success in future campaigns.
# 
# **3. Facebook Ad Conversion Categories:**
# 
# **Focus on Category 3:** This category clearly drives the majority of conversions. Analyze the characteristics of this category (e.g., demographics, interests) and double down on targeting similar audiences.
# **Review Category 2:** While not as effective as Category 3, it still contributes significantly. Investigate the reasons for its lower conversion rate and consider potential optimization strategies.
# **Monitor Category 1.03%-2.06%:** While conversions are low, keep an eye on this category. If it shows positive trends, it could be worth further exploration and optimization.
# 
# **4. Spent vs. Clicks and Conversions:**
# 
# **Spending Efficiency:** Analyze the relationship between spending and clicks/conversions. Identify if there are opportunities to reduce spending while maintaining performance.
# **Fluctuations in Spent:** Investigate the reasons behind the fluctuations in spending. Are they due to campaign adjustments, budget allocation changes, or external factors? Understanding these drivers helps with future budgeting and planning.
# **Color Gradient Analysis:** Although the color gradient makes it difficult to discern trends, it suggests a concentration of clicks with lower conversion rates. Analyze the characteristics of these clicks and consider strategies to improve their conversion potential (e.g., ad creative, landing page optimization).
# 
# **Additional Recommendations:**
# 
# **Invest in data visualization:** Improve the clarity of the graphs by adding labels, legends, and proper spacing. This will make it easier to analyze trends and identify key insights.
# **Set specific goals and track progress:** Define clear goals for your campaigns (e.g., website visits, app downloads) and track key metrics (e.g., conversion rates, ROI) to measure progress and success.
# **Regularly test and iterate:** Continuously test different ad creatives, targeting parameters, and campaign strategies to identify the most effective approaches.
# 
# By implementing these insights and recommendations, we can optimize your marketing efforts, improve campaign performance, and achieve your desired goals.
# 

# In[ ]:




