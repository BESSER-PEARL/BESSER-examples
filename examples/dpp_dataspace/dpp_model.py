from besser.BUML.metamodel.structural import *
from besser.generators.django import DjangoGenerator
from besser.generators.rdf import RDFGenerator

# ManualType enumeration
manualtype_enum: Enumeration = Enumeration(name="ManualType", literals={
                                EnumerationLiteral(name="Installation"),
                                EnumerationLiteral(name="Use"),
                                EnumerationLiteral(name="Recycle"),
                                EnumerationLiteral(name="Disassembly"),
                                EnumerationLiteral(name="Safety"),
                                EnumerationLiteral(name="Other")
                                })

# Source enumeration
source_enum: Enumeration = Enumeration(name="Source", literals={
                                EnumerationLiteral(name="Mined"),
                                EnumerationLiteral(name="Plant"),
                                EnumerationLiteral(name="Animal"),
                                EnumerationLiteral(name="Synthetic"),
                                EnumerationLiteral(name="Recycled"),
                                EnumerationLiteral(name="Biological"),
                                EnumerationLiteral(name="Other")
                                })

# Carrier enumeration
carrier_enum: Enumeration = Enumeration(name="Carrier", literals={
                                EnumerationLiteral(name="QRCode"),
                                EnumerationLiteral(name="Barcode"),
                                EnumerationLiteral(name="NFC")
                                })

# Product Passport
uid: Property = Property(name="code",  type=StringType)
gtin: Property = Property(name="GTIN",  type=StringType, multiplicity=Multiplicity(0, 1))
product_name: Property = Property(name="product_name",  type=StringType)
product_code: Property = Property(name="product_code",  type=StringType, multiplicity=Multiplicity(0, 1))
brand: Property = Property(name="brand",  type=StringType, multiplicity=Multiplicity(0, 1))
product_passport: Class = Class(name="ProductPassport", attributes={uid, product_code, gtin, product_name, brand})

# Chemical
threshold: Property = Property(name="threshold",  type=StringType)
disclosure: Property = Property(name="disclosure",  type=StringType)
ch_composition: Property = Property(name="composition",  type=BooleanType)
chemical: Class = Class(name="Chemical", attributes={threshold, disclosure, ch_composition})

# Hazard
very_high: Property = Property(name="very_high",  type=BooleanType)
crm: Property = Property(name="crm",  type=BooleanType)
exeed_limit: Property = Property(name="exeed_limit",  type=BooleanType)
hazard: Class = Class(name="Hazard", attributes={very_high, crm, exeed_limit})

# Recycled Material
preconsumer: Property = Property(name="preconsumer", type=StringType)
posconsumer: Property = Property(name="posconsumer", type=StringType)
renewable: Property = Property(name="renewable", type=StringType)
recycled: Class = Class(name="RecycledMaterial", attributes={preconsumer, posconsumer, renewable})

# Guideline
guid_name: Property = Property(name="name", type=StringType)
guid_descrip: Property = Property(name="description", type=StringType)
guid_type: Property = Property(name="type", type=manualtype_enum)
guid_doc: Property = Property(name="doc", type=StringType)
guideline: Class = Class(name="Guideline", attributes={guid_name, guid_descrip, guid_type, guid_doc})

# Material Use
quantity: Property = Property(name="quantity",  type=IntegerType)
material_unit: Property = Property(name="unit",  type=IntegerType)
is_direct: Property = Property(name="is_direct",  type=BooleanType)
material_use: Class = Class(name="MaterialUse", attributes={quantity, material_unit, is_direct})

# Material
mat_name: Property = Property(name="name",  type=StringType)
toxic: Property = Property(name="toxic",  type=StringType)
source: Property = Property(name="source",  type=source_enum)
material: Class = Class(name="Material", attributes={mat_name, toxic, source})

# Data Carrier
carrier_code: Property = Property(name="code",  type=StringType)
carrier_type: Property = Property(name="technology",  type=carrier_enum)
carrier: Class = Class(name="DataCarrier", attributes={carrier_code, carrier_type})

# Enviromental Impact Parameter
value: Property = Property(name="value",  type=IntegerType)
parameter: Class = Class(name="Parameter", attributes={value})

# Metric
metric_name: Property = Property(name="name",  type=StringType)
metric_unit: Property = Property(name="unit",  type=StringType)
metric: Class = Class(name="Metric", attributes={metric_name, metric_unit})

# Lifecycle Stage
stage_name: Property = Property(name="name",  type=StringType)
start_date: Property = Property(name="start_date",  type=DateTimeType)
end_date: Property = Property(name="end_date",  type=DateTimeType, multiplicity=Multiplicity(0, 1))
lifecycle_stage: Class = Class(name="LifecycleStage", attributes={stage_name, start_date, end_date}, is_abstract=True)

# Person
person_name: Property = Property(name="name",  type=StringType)
function: Property = Property(name="function",  type=StringType)
email: Property = Property(name="email",  type=StringType)
telephone: Property = Property(name="telephone",  type=IntegerType, multiplicity=Multiplicity(0, 1))
person: Class = Class(name="Person", attributes={person_name, function, email, telephone})

# Design Stage
design: Class = Class(name="Design", attributes=set())

# Manufacture Stage
p_site: Property = Property(name="production_site",  type=StringType)
p_address: Property = Property(name="address",  type=StringType)
p_city: Property = Property(name="city",  type=StringType)
p_postal_code: Property = Property(name="postal_code",  type=IntegerType)
p_country: Property = Property(name="country",  type=StringType)
manufacture: Class = Class(name="Manufacture", attributes={p_site, p_address, p_city, p_postal_code, p_country})

# DiStringTypeibution Stage
diStringType_source: Property = Property(name="source",  type=StringType)
diStringType_dest: Property = Property(name="destination",  type=StringType)
diStringTypeibution: Class = Class(name="DiStringTypeibution", attributes={diStringType_source, diStringType_dest})
# Use Stage
use: Class = Class(name="Use", attributes=set())
# Collect Stage
collect: Class = Class(name="Collect", attributes=set())
# Recycle Stage
recycle: Class = Class(name="Recycle", attributes=set())

# Reparation
rep_name: Property = Property(name="name",  type=StringType)
description: Property = Property(name="description",  type=StringType)
reparation_date: Property = Property(name="date",  type=DateTimeType)
reparation: Class = Class(name="Reparation", attributes={rep_name, description, reparation_date})

# Company
company_name: Property = Property(name="name",  type=StringType)
address: Property = Property(name="address",  type=StringType)
country: Property = Property(name="country",  type=StringType)
postal_code: Property = Property(name="postal_code",  type=IntegerType)
gln: Property = Property(name="GLN",  type=IntegerType, multiplicity=Multiplicity(0, 1))
company: Class = Class(name="Company", attributes={company_name, address, country, postal_code, gln})

types: set[Type] = {product_passport, material_use, material, carrier, parameter, metric, lifecycle_stage, person,
                      design, manufacture, diStringTypeibution, use, collect, recycle, reparation, company, chemical, recycled,
                      hazard, guideline, manualtype_enum, source_enum, carrier_enum}

# Associations
a_product_carrier: BinaryAssociation = BinaryAssociation(name="rel_product_carrier", ends={
    Property(name="data_carrier",  type=carrier, multiplicity=Multiplicity(1, "*"), is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=Multiplicity(1, 1), is_navigable=False)})
a_product_lifecycle: BinaryAssociation = BinaryAssociation(name="rel_product_lifecycle", ends={
    Property(name="stages",  type=lifecycle_stage, multiplicity=Multiplicity(0, "*"), is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True)})
a_product_hazard: BinaryAssociation = BinaryAssociation(name="rel_product_hazard", ends={
    Property(name="hazard",  type=hazard, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_product_recycled: BinaryAssociation = BinaryAssociation(name="rel_product_recycled", ends={
    Property(name="recycled_material",  type=recycled, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_product_chemical: BinaryAssociation = BinaryAssociation(name="rel_product_chemical", ends={
    Property(name="chemical",  type=chemical, multiplicity=Multiplicity(1, 1)),
    Property(name="product",  type=product_passport, multiplicity=Multiplicity(0, "*"))})
a_material_stage: BinaryAssociation = BinaryAssociation(name="rel_material_stage", ends={
    Property(name="materials",  type=material_use, multiplicity=Multiplicity(0, "*"), is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=Multiplicity(1, 1), is_navigable=False)})
a_material_raw: BinaryAssociation = BinaryAssociation(name="rel_material_raw", ends={
    Property(name="material",  type=material, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="material_use",  type=material_use, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_lifecycle_parameter: BinaryAssociation = BinaryAssociation(name="rel_lifecycle_parameter", ends={
    Property(name="enviromental_impacts",  type=parameter, multiplicity=Multiplicity(0, "*"), is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=Multiplicity(1, 1), is_navigable=False, is_composite=True)})
a_lifecycle_peson: BinaryAssociation = BinaryAssociation(name="rel_lifecycle_person", ends={
    Property(name="issuer",  type=person, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="issue",  type=lifecycle_stage, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_parameter_metric: BinaryAssociation = BinaryAssociation(name="rel_parameter_metric", ends={
    Property(name="metric",  type=metric, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="value",  type=parameter, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_use_reparation: BinaryAssociation = BinaryAssociation(name="rel_use_reparation", ends={
    Property(name="reparations",  type=reparation, multiplicity=Multiplicity(0, "*"), is_navigable=True),
    Property(name="use_stage",  type=use, multiplicity=Multiplicity(1, 1), is_navigable=False)})
a_reparation_material: BinaryAssociation = BinaryAssociation(name="rel_reparation_material", ends={
    Property(name="materials",  type=material_use, multiplicity=Multiplicity(0, "*"), is_navigable=True),
    Property(name="reparation",  type=reparation, multiplicity=Multiplicity(0, 1), is_navigable=False)})
a_manufacture_company: BinaryAssociation = BinaryAssociation(name="rel_manufacture_company", ends={
    Property(name="companies",  type=company, multiplicity=Multiplicity(1, "*"), is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=Multiplicity(0, "*"), is_navigable=False)})
a_person_company: BinaryAssociation = BinaryAssociation(name="rel_person_company", ends={
    Property(name="company",  type=company, multiplicity=Multiplicity(1, 1), is_navigable=True),
    Property(name="employee",  type=person, multiplicity=Multiplicity(0, "*"), is_navigable=False)})

# Associations
associations: set[Association] = {a_person_company, a_product_carrier, a_product_lifecycle, a_material_raw, a_product_hazard,
                                  a_material_stage, a_manufacture_company, a_lifecycle_parameter, a_parameter_metric, a_use_reparation, 
                                  a_reparation_material, a_product_recycled, a_product_chemical, a_lifecycle_peson}

# Generalizations
gen_lf_design: Generalization = Generalization(general=lifecycle_stage, specific=design)
gen_lf_manufacture: Generalization = Generalization(general=lifecycle_stage, specific=manufacture)
gen_lf_diStringTypeibution: Generalization = Generalization(general=lifecycle_stage, specific=diStringTypeibution)
gen_lf_use: Generalization = Generalization(general=lifecycle_stage, specific=use)
gen_lf_collect: Generalization = Generalization(general=lifecycle_stage, specific=collect)
gen_lf_recycle: Generalization = Generalization(general=lifecycle_stage, specific=recycle)

generalizations: set[Generalization] = {gen_lf_design, gen_lf_manufacture, gen_lf_diStringTypeibution, gen_lf_use, gen_lf_collect, 
                                        gen_lf_recycle}


# Domain Model
dpp_domain: DomainModel = DomainModel(name="Digital_Product_Passport", 
                                      types=types, 
                                      associations=associations, 
                                      generalizations=generalizations
                                      )

# Django code generation
django_generator: DjangoGenerator = DjangoGenerator(model=dpp_domain, project_name="dpp_project", app_name="dpp_app")
django_generator.generate()

# RDF vocabulary generation
rdf_generator: RDFGenerator = RDFGenerator(model=dpp_domain, output_dir="rdf_code")
rdf_generator.generate()
