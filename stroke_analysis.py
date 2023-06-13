import pandas as pd

df = pd.read_csv('~/Desktop/healthcare-dataset-stroke-data.csv')

# change avg_glucise_level to int
round(df["avg_glucose_level"])
df= df.astype({"avg_glucose_level": int})

# drop N/A values from bmi
df = df.dropna(subset=['bmi'])

df['stroke']

df.to_csv('stoke.csv', index=False)



# Tableau Public Link: https://public.tableau.com/views/StrokeAnalysis_16866691283780/Dashboard1?:language=en-US&:display_count=n&:origin=viz_share_link