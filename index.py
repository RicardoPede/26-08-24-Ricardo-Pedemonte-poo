import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

class DatabaseConnector:
    def __init__(self, user, password, host, database):
        self.user = user
        self.password = password
        self.host = host
        self.database = database
        self.engine = None
        self.df = None

# La clase DatabaseConnector se encarga de la conexión a la base de datos y de la lectura de los datos.
# Recibe los parámetros necesarios para la conexión en el constructor y tiene un método connect que se encarga de establecer la conexión.
    def connect(self):
        try:
            self.engine = create_engine(f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}')
            self.df = pd.read_sql_query('SELECT * FROM EmployeePerformance', self.engine)
            print('Connection to database successful')
            
        except OperationalError as e:
            print('Error:', e)

# El método fetch_data recibe una query y devuelve un DataFrame con los resultados de la consulta.
    def fetch_data(self, query):
        if self.engine:
            return pd.read_sql_query(query, self.engine)
        else:
            print('No connection to database')
            return None

# La clase DataAnalyzer se encarga de realizar análisis de los datos.
# Recibe un DataFrame en el constructor y tiene dos métodos: get_statistics y get_correlations.
class DataAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def get_statistics(self):
        if self.df is None:
            return None
        
        return self.df.groupby('departament').agg({
            'performance_score': ['mean', 'median', 'std'],
            'salary': ['mean', 'median', 'std'],
            'employee_id': 'count'
        }).rename(columns={'employee_id': 'total_employees'})

    def get_correlations(self):
        if self.df is None:
            return None

        correlacion_years_performance = np.corrcoef(self.df['years_with_company'], self.df['performance_score'])[0, 1]
        correlacion_salary_performance = np.corrcoef(self.df['salary'], self.df['performance_score'])[0, 1]
        return correlacion_years_performance, correlacion_salary_performance

# La clase DataVisualizer se encarga de visualizar los datos.
# Recibe un DataFrame en el constructor y tiene dos métodos: plot_histograms y plot_scatter.
class DataVisualizer:
    def __init__(self, df):
        self.df = df
    
    def plot_histograms(self):
        if self.df is None:
            return

        for departament in self.df['departament'].unique():
            plt.figure()
            self.df[self.df['departament'] == departament]['performance_score'].hist()
            plt.title(f'Performance for {departament}')
            plt.xlabel('Performance')
            plt.ylabel('Employees')

    def plot_scatter(self):
        if self.df is None:
            return

        plt.figure()
        plt.scatter(self.df['years_with_company'], self.df['performance_score'])
        plt.title('Years with company vs Performance')
        plt.xlabel('Years with company')
        plt.ylabel('Performance')

        plt.figure()
        plt.scatter(self.df['salary'], self.df['performance_score'])
        plt.title('Salary vs Performance')
        plt.xlabel('Salary')
        plt.ylabel('Performance')

        plt.show()

# Se crea una instancia de DatabaseConnector, se conecta a la base de datos y se obtienen los datos.
# Luego se crean instancias de DataAnalyzer y DataVisualizer con el DataFrame obtenido.
# Se obtienen las estadísticas y correlaciones con DataAnalyzer y se imprimen.
# Se grafican los histogramas y scatter plots con DataVisualizer.
if __name__ == '__main__':
    db = DatabaseConnector('root', '', 'localhost', 'CompanyData')
    db.connect()

    analyzer = DataAnalyzer(db.df)
    statistics = analyzer.get_statistics()
    print(statistics)

    correlations = analyzer.get_correlations()
    print(correlations)

    visualizer = DataVisualizer(db.df)
    visualizer.plot_histograms()
    visualizer.plot_scatter()

