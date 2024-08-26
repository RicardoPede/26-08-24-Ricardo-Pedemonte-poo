# Para le presente trabajo consistente en:

Aplicar los principios de la programación orientada a objetos (POO) en el contexto del ejercicio de repaso de Numpy, Pandas, y Matplotlib realizado el 05/08/2024, se ha extraído el archivo main.py y adjuntado al presente repositorio.

## Instrucciones

    Refactorización: Tomar el ejercicio mencionado y refactorizar el código utilizando conceptos de POO, tales como clases, herencia, encapsulamiento, y polimorfismo, donde sea pertinente.
    Creación de Rama: Antes de comenzar la implementación, crea una nueva rama en tu repositorio. El nombre de la rama debe seguir este formato: dd-mm-aa-nombre-apellido-poo
    Implementación: Implementa la solución en la nueva rama creada, asegurándote de que el código siga los principios de POO y que la estructura del proyecto sea organizada y modular.

### Inicio:

Se ha creado un entorno de trabajo virtual con el comando:
```bash
python -m venv env
```

Se ha activado el entorno de trabajo virtual con el comando:
```bash
source env/Scripts/activate
```

Se han instalado las librerías necesarias con el comando:
```bash
pip install pandas numpy matplotlib sqlalchemy
```

Se ha creado el archivo "index.py" con el código necesario para realizar el análisis de datos avanzados.

## Ejecución del trabajo:
La libreria sqlalchemy se ha utilizado para la conexión con la base de datos MySQL, en la cual 
se ha creado primeramente una base de datos llamada "CompanyData" y una tabla llamada "EmployeePerformance", creandose en ella 1000 registros de datos ficticios.

La librería pandas se ha utilizado para la extracción de los datos de la tabla EmployeePerformance.

La librería matplotlib se ha utilizado para la visualización de los datos, obteniendo los gráficos solicitados.

## Aplicando los principios de la POO:
Se ha creado una clase llamada "DatabaseConnector" que se encarga de la conexión con la base de datos MySQL.

Se ha creado una clase llamada "DataAnalyzer" que se encarga de la extracción de los datos de la tabla EmployeePerformance.

Se ha creado una clase llamada "DataVisualizer" que se encarga de la visualización de los datos.
