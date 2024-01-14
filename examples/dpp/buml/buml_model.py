from BUML.metamodel.structural import NamedElement, DomainModel, Type, Class, \
        Property, PrimitiveDataType, Multiplicity, Association, BinaryAssociation, Generalization, \
        GeneralizationSet, AssociationClass 

# Primitive Data Types 
int_type = PrimitiveDataType("int")
str_type = PrimitiveDataType("str")
date_type = PrimitiveDataType("date")

# ProductPassport class definition 
ProductPassport_code: Property = Property(name="code", property_type=str_type, visibility="public")
ProductPassport_product_name: Property = Property(name="product_name", property_type=int_type, visibility="public")
ProductPassport_brand: Property = Property(name="brand", property_type=str_type, visibility="public")
ProductPassport: Class = Class(name="ProductPassport", attributes={ProductPassport_code, ProductPassport_product_name, ProductPassport_brand})

# LifecycleStage class definition 
LifecycleStage_start: Property = Property(name="start", property_type=date_type, visibility="public")
LifecycleStage_end: Property = Property(name="end", property_type=date_type, visibility="public")
LifecycleStage: Class = Class(name="LifecycleStage", attributes={LifecycleStage_start, LifecycleStage_end})

# Design class definition 
Design: Class = Class(name="Design", attributes=set())

# Use class definition 
Use: Class = Class(name="Use", attributes=set())

# Manufacture class definition 
Manufacture: Class = Class(name="Manufacture", attributes=set())

# Distribution class definition 
Distribution: Class = Class(name="Distribution", attributes=set())

# RawMaterial class definition 
RawMaterial_name: Property = Property(name="name", property_type=str_type, visibility="public")
RawMaterial: Class = Class(name="RawMaterial", attributes={RawMaterial_name})

# Reparation class definition 
Reparation_description: Property = Property(name="description", property_type=str_type, visibility="public")
Reparation_date_set: Property = Property(name="date_set", property_type=date_type, visibility="public")
Reparation: Class = Class(name="Reparation", attributes={Reparation_description, Reparation_date_set})

# Relationships
stage: BinaryAssociation = BinaryAssociation(name="stage", ends={
        Property(name="stage", property_type=ProductPassport, multiplicity=Multiplicity(0, "*"), is_navigable=False),
        Property(name="stage", property_type=LifecycleStage, multiplicity=Multiplicity(1, "*"), is_navigable=True)})
composition: BinaryAssociation = BinaryAssociation(name="composition", ends={
        Property(name="composition", property_type=LifecycleStage, multiplicity=Multiplicity(0, "*"), is_navigable=False),
        Property(name="composition", property_type=RawMaterial, multiplicity=Multiplicity(1, "*"), is_navigable=True)})
reparations: BinaryAssociation = BinaryAssociation(name="reparations", ends={
        Property(name="reparations", property_type=Use, multiplicity=Multiplicity(1, 1), is_navigable=False),
        Property(name="reparations", property_type=Reparation, multiplicity=Multiplicity(0, "*"), is_navigable=True)})

# Generalizations
gen_LifecycleStage_Design: Generalization = Generalization(general=LifecycleStage, specific=Design)
gen_LifecycleStage_Use: Generalization = Generalization(general=LifecycleStage, specific=Use)
gen_LifecycleStage_Manufacture: Generalization = Generalization(general=LifecycleStage, specific=Manufacture)
gen_LifecycleStage_Distribution: Generalization = Generalization(general=LifecycleStage, specific=Distribution)


# Domain Model
domain: DomainModel = DomainModel(name="Domain Model", types={ProductPassport, LifecycleStage, Design, Use, Manufacture, Distribution, RawMaterial, Reparation}, associations={stage, composition, reparations}, generalizations={gen_LifecycleStage_Design, gen_LifecycleStage_Use, gen_LifecycleStage_Manufacture, gen_LifecycleStage_Distribution})