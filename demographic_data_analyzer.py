import pandas as pd

# Crear el DataFrame con los datos proporcionados
data = {
    'age': [39, 50, 38, 53, 28],
    'workclass': ['State-gov', 'Self-emp-not-inc', 'Private', 'Private', 'Private'],
    'fnlwgt': [77516, 83311, 215646, 234721, 338409],
    'education': ['Bachelors', 'Bachelors', 'HS-grad', '11th', 'Bachelors'],
    'education-num': [13, 13, 9, 7, 13],
    'marital-status': ['Never-married', 'Married-civ-spouse', 'Divorced', 'Married-civ-spouse', 'Married-civ-spouse'],
    'occupation': ['Adm-clerical', 'Exec-managerial', 'Handlers-cleaners', 'Handlers-cleaners', 'Prof-specialty'],
    'relationship': ['Not-in-family', 'Husband', 'Not-in-family', 'Husband', 'Wife'],
    'race': ['White', 'White', 'White', 'Black', 'Black'],
    'sex': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'capital-gain': [2174, 0, 0, 0, 0],
    'capital-loss': [0, 0, 0, 0, 0],
    'hours-per-week': [40, 13, 40, 40, 40],
    'native-country': ['United-States', 'United-States', 'United-States', 'United-States', 'Cuba'],
    'salary': ['<=50K', '<=50K', '<=50K', '<=50K', '<=50K']
}

df = pd.DataFrame(data)

# 1. ¿Cuántas personas de cada raza están representadas en este set de datos?
race_count = df['race'].value_counts()
print("Personas de cada raza:\n", race_count)

# 2. ¿Cuál es la edad promedio de los hombres?
average_age_men = df[df['sex'] == 'Male']['age'].mean()
print(f"Edad promedio de los hombres: {average_age_men:.2f}")

# 3. ¿Cuál es el porcentaje de personas que tienen un grado de licenciatura (Bachelor's degree)?
total_count = df.shape[0]
bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
percentage_bachelors = (bachelors_count / total_count) * 100
print(f"Porcentaje de personas con grado de licenciatura: {percentage_bachelors:.2f}%")

# 4. ¿Qué porcentaje de personas con una educación avanzada (Bachelors, Masters o Doctorate) ganan más de 50k?
advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
advanced_education_rich = df[advanced_education & (df['salary'] == '>50K')]
percentage_advanced_education_rich = (advanced_education_rich.shape[0] / df[advanced_education].shape[0]) * 100
print(f"Porcentaje de personas con educación avanzada que ganan más de 50k: {percentage_advanced_education_rich:.2f}%")

# 5. ¿Qué porcentaje de personas sin una educación avanzada generan más de 50k?
not_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
not_advanced_education_rich = df[not_advanced_education & (df['salary'] == '>50K')]
percentage_not_advanced_education_rich = (not_advanced_education_rich.shape[0] / df[not_advanced_education].shape[0]) * 100
print(f"Porcentaje de personas sin educación avanzada que ganan más de 50k: {percentage_not_advanced_education_rich:.2f}%")

# 6. ¿Cuál es el mínimo número de horas que una persona trabaja por semana?
min_work_hours = df['hours-per-week'].min()
print(f"Mínimo número de horas trabajadas por semana: {min_work_hours}")

# 7. ¿Qué porcentaje de personas que trabajan el mínimo de horas por semana tiene un salario de más de 50k?
min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
percentage_min_workers_rich = (min_workers_rich.shape[0] / df[df['hours-per-week'] == min_work_hours].shape[0]) * 100
print(f"Porcentaje de personas que trabajan el mínimo de horas por semana y ganan más de 50k: {percentage_min_workers_rich:.2f}%")

# 8. ¿Qué país tiene el porcentaje más alto de personas que ganan >50k y cuál es ese porcentaje?
country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
country_total = df['native-country'].value_counts()
highest_earning_country = (country_salary / country_total * 100).idxmax() if not country_salary.empty else None
highest_earning_country_percentage = (country_salary / country_total * 100).max() if not country_salary.empty else 0
print(f"País con el porcentaje más alto de personas que ganan >50k: {highest_earning_country}")
print(f"Porcentaje: {highest_earning_country_percentage:.2f}%")

# 9. Identifica la ocupación más popular de aquellos que ganan >50k en India.
india_occupation_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax() if not df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].empty else None
print(f"Ocupación más popular en India entre los que ganan >50k: {india_occupation_rich}")
