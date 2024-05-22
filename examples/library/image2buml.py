from besser.BUML.metamodel.structural import DomainModel
from besser.utilities import image_to_plantuml, image_to_buml
from besser.generators.python_classes.python_classes_generator import PythonGenerator
from besser.generators.django import DjangoGenerator
from besser.generators.sql_alchemy import SQLAlchemyGenerator
from besser.generators.sql import SQLGenerator

# Image to BUML model
library_model: DomainModel = image_to_buml(image_path="library_hand_draw.png", openai_token="xxxxx")

# Code Generation
python_model = Python_Generator(model=library_model)
python_model.generate()

django = DjangoGenerator(model=library_model)
django.generate()

sql_alchemy = SQLAlchemyGenerator(model=library_model)
sql_alchemy.generate()

sql = SQLGenerator(model=library_model)
sql.generate()