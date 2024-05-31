from besser.BUML.notations.structuralPlantUML import plantuml_to_buml
from besser.BUML.metamodel.structural import DomainModel
from besser.generators.python_classes import Python_Generator
from besser.generators.django import DjangoGenerator
from besser.generators.sql_alchemy import SQLAlchemyGenerator
from besser.generators.sql import SQLGenerator

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