import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

try:
    engine = create_engine('mysql+pymysql://root:@localhost/CompanyData')
    df = pd.read_sql_query('SELECT * FROM EmployeePerformance', engine)
    
    estadisticas = df.groupby('departament').agg({
        'performance_score': ['mean', 'median', 'std'],
        'salary': ['mean', 'median', 'std'],
        'employee_id': 'count'
    }).rename(columns={'employee_id': 'total_employees'})
    print(estadisticas)
except OperationalError as e:
    print('Error:', e)

# correlacion_years_performance = df['years_with_company'].corr(df['performance_score'])
# correlacion_salary_performance = df['salary'].corr(df['performance_score'])

correlacion_years_performance = np.corrcoef(df['years_with_company'], df['performance_score'])[0, 1]
correlacion_salary_performance = np.corrcoef(df['salary'], df['performance_score'])[0, 1]
    
for departament in df['departament'].unique():
    plt.figure()
    df[df['departament'] == departament]['performance_score'].hist()
    plt.title(f'Performance for {departament}')
    plt.xlabel('Performance')
    plt.ylabel('Employees')

plt.figure()
plt.scatter(df['years_with_company'], df['performance_score'])
plt.title('Years with company vs Performance')
plt.xlabel('Years with company')
plt.ylabel('Performance')

plt.figure()
plt.scatter(df['salary'], df['performance_score'])
plt.title('Salary vs Performance')
plt.xlabel('Salary')
plt.ylabel('Performance')

plt.show()