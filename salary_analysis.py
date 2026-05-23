import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# This tells Pandas: "Don't hide any columns!"
# pd.set_option('display.max_column', None)

# Load the file you just downloaded
# (Make sure the filename matches exactly!)
df = pd.read_csv('jobs_in_data.csv')

# Let's verify the columns so we don't get lost
print("Successfully loaded! Here are your columns:")
# print(df.columns.tolist())

# Quick look at the first 5 rows
# print(df.head(5))

# 1. Filter for only Entry-Level roles
# (In this dataset, 'Entry-level' is usually coded as 'EN')
df_entry_level = df[df['experience_level'] == 'Entry-level']

# 2. Find the top 5 highest-paying job titles for Entry-Level
top_5_jobs = df_entry_level.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)

print("--- Top 5 Highest Paying Entry-Level Job Titles ---")
print(top_5_jobs)

# 3. Visualize it so it looks professional
plt.figure(figsize= (10,6))
top_5_jobs.plot(kind='barh', color='skyblue')
plt.title('Highest Paying Entry-level Data Roles (USD)')
plt.ylabel('Job Title')
plt.xlabel('Average Salary ($)')
plt.gca().invert_yaxis() # Put the highest at the top
plt.show()

# 4. Filter specifically for 'Applied Scientist.'
df_applied_sci = df[df['job_title'] == 'Applied Scientist']

# 5. Compare Salary by Work Setting (Remote, In-person, Hybrid)
work_setting_comparison = df_applied_sci.groupby('work_setting')['salary_in_usd'].mean()

print("--- Average Salary by Work Setting (Applied Scientist) ---")
print(work_setting_comparison)

work_setting_comparison.plot(kind='bar' , color= ['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Applied Scientist: Remote vs. Office Salary')
plt.ylabel('Avg Salary ($)')
plt.xticks(rotation=45 )
plt.show()

print(df_applied_sci['work_setting'].value_counts())

# 6. Group the data and get both the Mean and the Count
stats = df_applied_sci.groupby('work_setting')['salary_in_usd'].agg(['mean', 'count'])

# 7. Only keep settings that have more than 5 people
significant_stats = stats[stats['count'] > 5]

print("--- Cleaned Salary Stats (Min 5 samples) ---")
print(significant_stats)

# 8. Plot the cleaned data
significant_stats['mean'].plot(kind='bar', color='teal')
plt.title('Applied Scientist: Average Salary (Cleaned)')
plt.ylabel('Salary ($)')
plt.show()

# 9. Which company size pays more (S = Small, M = Medium, L = Large)
size_counts = df_applied_sci['company_size'].value_counts()
size_salary = df_applied_sci.groupby('company_size')['salary_in_usd'].mean()

print("--- Company Size Counts ---")
print("\n--- Avg Salary by Size ---")
print(size_salary)
print(size_counts)

# -------------Visualization---------------

# 1. Load your local file
df = pd.read_csv('jobs_in_data.csv')

# 2. Filter for your target role
applied_sci = df[df['job_title'] == 'Applied Scientist'].copy()

# 3. Handle the 'Hybrid' outlier (The statistical integrity check you did)
# We only keep settings with more than 1 person to avoid skewed averages
work_counts = applied_sci['work_setting'].value_counts()
valid_settings = work_counts[work_counts > 1].index
applied_sci_filtered = applied_sci[applied_sci['work_setting'].isin(valid_settings)]

# 4. Visualization: Salary by Work Setting
plt.figure(figsize=(10, 5))
sns.barplot(data=applied_sci_filtered, x='work_setting', y='salary_in_usd', palette='viridis')
plt.title('Applied Scientist: Remote vs. In-Person Salary (2024-2025)')
plt.savefig('work_setting_comparison.png') # Saves the chart for your portfolio
plt.show()

# 5. Visualization: Salary by Company Size
plt.figure(figsize=(10, 5))
sns.barplot(data=applied_sci, x='company_size', y='salary_in_usd', order=['S', 'M', 'L'], palette='magma')
plt.title('Applied Scientist Salary by Company Size')
plt.savefig('company_size_comparison.png')
plt.show()

print("Analysis Complete. Charts saved to your folder!")
