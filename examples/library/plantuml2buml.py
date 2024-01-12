from BUML.notations.plantUML import plantuml_to_buml
from BUML.metamodel.structural import DomainModel
from generators.python_classes import Python_Generator
from generators.django import DjangoGenerator
from generators.sql_alchemy import SQLAlchemyGenerator
from generators.sql import SQLGenerator

# PlantUML to B-UML model
library_buml: DomainModel = plantuml_to_buml(plantUML_model_path='library.plantuml')

# Code Generation
python_model = Python_Generator(model=library_buml)
python_model.generate()

django = DjangoGenerator(model=library_buml)
django.generate()

sql_alchemy = SQLAlchemyGenerator(model=library_buml)
sql_alchemy.generate()

sql = SQLGenerator(model=library_buml)
sql.generate()