from besser.BUML.metamodel.structural import *
from besser.generators.django import DjangoGenerator
from besser.generators.rdf import RDFGenerator

# Primitive Data Types
str = PrimitiveDataType("str")
int = PrimitiveDataType("int")
bool = PrimitiveDataType("bool")
datetime = PrimitiveDataType("datetime")

# Multiplicity
zero_one = Multiplicity(0, 1)
zero_many = Multiplicity(0, "*")
one = Multiplicity(1, 1)
one_many = Multiplicity(1, "*")

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
uid: Property = Property(name="code",  type=str)
gtin: Property = Property(name="GTIN",  type=str, multiplicity=zero_one)
product_name: Property = Property(name="product_name",  type=str)
product_code: Property = Property(name="product_code",  type=str, multiplicity=zero_one)
brand: Property = Property(name="brand",  type=str, multiplicity=zero_one)
product_passport: Class = Class(name="ProductPassport", attributes={uid, product_code, gtin, product_name, brand})

# Chemical
threshold: Property = Property(name="threshold",  type=str)
disclosure: Property = Property(name="disclosure",  type=str)
ch_composition: Property = Property(name="composition",  type=bool)
chemical: Class = Class(name="Chemical", attributes={threshold, disclosure, ch_composition})

# Hazard
very_high: Property = Property(name="very_high",  type=bool)
crm: Property = Property(name="crm",  type=bool)
exeed_limit: Property = Property(name="exeed_limit",  type=bool)
hazard: Class = Class(name="Hazard", attributes={very_high, crm, exeed_limit})

# Recycled Material
preconsumer: Property = Property(name="preconsumer", type=str)
posconsumer: Property = Property(name="posconsumer", type=str)
renewable: Property = Property(name="renewable", type=str)
recycled: Class = Class(name="RecycledMaterial", attributes={preconsumer, posconsumer, renewable})

# Guideline
guid_name: Property = Property(name="name", type=str)
guid_descrip: Property = Property(name="description", type=str)
guid_type: Property = Property(name="type", type=manualtype_enum)
guid_doc: Property = Property(name="doc", type=str)
guideline: Class = Class(name="Guideline", attributes={guid_name, guid_descrip, guid_type, guid_doc})

# Material Use
quantity: Property = Property(name="quantity",  type=int)
material_unit: Property = Property(name="unit",  type=int)
is_direct: Property = Property(name="is_direct",  type=bool)
material_use: Class = Class(name="MaterialUse", attributes={quantity, material_unit, is_direct})

# Material
mat_name: Property = Property(name="name",  type=str)
toxic: Property = Property(name="toxic",  type=str)
source: Property = Property(name="source",  type=source_enum)
material: Class = Class(name="Material", attributes={mat_name, toxic, source})

# Data Carrier
carrier_code: Property = Property(name="code",  type=str)
carrier_type: Property = Property(name="technology",  type=carrier_enum)
carrier: Class = Class(name="DataCarrier", attributes={carrier_code, carrier_type})

# Enviromental Impact Parameter
value: Property = Property(name="value",  type=int)
parameter: Class = Class(name="Parameter", attributes={value})

# Metric
metric_name: Property = Property(name="name",  type=str)
metric_unit: Property = Property(name="unit",  type=str)
metric: Class = Class(name="Metric", attributes={metric_name, metric_unit})

# Lifecycle Stage
stage_name: Property = Property(name="name",  type=str)
start_date: Property = Property(name="start_date",  type=datetime)
end_date: Property = Property(name="end_date",  type=datetime, multiplicity=zero_one)
lifecycle_stage: Class = Class(name="LifecycleStage", attributes={stage_name, start_date, end_date}, is_abstract=True)

# Person
person_name: Property = Property(name="name",  type=str)
function: Property = Property(name="function",  type=str)
email: Property = Property(name="email",  type=str)
telephone: Property = Property(name="telephone",  type=int, multiplicity=zero_one)
person: Class = Class(name="Person", attributes={person_name, function, email, telephone})

# Design Stage
design: Class = Class(name="Design", attributes=set())

# Manufacture Stage
p_site: Property = Property(name="production_site",  type=str)
p_address: Property = Property(name="address",  type=str)
p_city: Property = Property(name="city",  type=str)
p_postal_code: Property = Property(name="postal_code",  type=int)
p_country: Property = Property(name="country",  type=str)
manufacture: Class = Class(name="Manufacture", attributes={p_site, p_address, p_city, p_postal_code, p_country})

# Distribution Stage
distr_source: Property = Property(name="source",  type=str)
distr_dest: Property = Property(name="destination",  type=str)
distribution: Class = Class(name="Distribution", attributes={distr_source, distr_dest})
# Use Stage
use: Class = Class(name="Use", attributes=set())
# Collect Stage
collect: Class = Class(name="Collect", attributes=set())
# Recycle Stage
recycle: Class = Class(name="Recycle", attributes=set())

# Reparation
rep_name: Property = Property(name="name",  type=str)
description: Property = Property(name="description",  type=str)
reparation_date: Property = Property(name="date",  type=datetime)
reparation: Class = Class(name="Reparation", attributes={rep_name, description, reparation_date})

# Company
company_name: Property = Property(name="name",  type=str)
address: Property = Property(name="address",  type=str)
country: Property = Property(name="country",  type=str)
postal_code: Property = Property(name="postal_code",  type=int)
gln: Property = Property(name="GLN",  type=int, multiplicity=zero_one)
company: Class = Class(name="Company", attributes={company_name, address, country, postal_code, gln})

classes: set[Type] = {product_passport, material_use, material, carrier, parameter, metric, lifecycle_stage, person,
                      design, manufacture, distribution, use, collect, recycle, reparation, company, chemical, recycled,
                      hazard, guideline}

# Associations
a_product_carrier: BinaryAssociation = BinaryAssociation(name="rel_product_carrier", ends={
    Property(name="data_carrier",  type=carrier, multiplicity=one_many, is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=one, is_navigable=False)})
a_product_lifecycle: BinaryAssociation = BinaryAssociation(name="rel_product_lifecycle", ends={
    Property(name="stages",  type=lifecycle_stage, multiplicity=zero_many, is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=one, is_navigable=False, is_composite=True)})
a_product_hazard: BinaryAssociation = BinaryAssociation(name="rel_product_hazard", ends={
    Property(name="hazard",  type=hazard, multiplicity=one, is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=zero_many, is_navigable=False)})
a_product_recycled: BinaryAssociation = BinaryAssociation(name="rel_product_recycled", ends={
    Property(name="recycled_material",  type=recycled, multiplicity=one, is_navigable=True),
    Property(name="product",  type=product_passport, multiplicity=zero_many, is_navigable=False)})
a_product_chemical: BinaryAssociation = BinaryAssociation(name="rel_product_chemical", ends={
    Property(name="chemical",  type=chemical, multiplicity=one),
    Property(name="product",  type=product_passport, multiplicity=zero_many)})
a_material_stage: BinaryAssociation = BinaryAssociation(name="rel_material_stage", ends={
    Property(name="materials",  type=material_use, multiplicity=zero_many, is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=one, is_navigable=False)})
a_material_raw: BinaryAssociation = BinaryAssociation(name="rel_material_raw", ends={
    Property(name="material",  type=material, multiplicity=one, is_navigable=True),
    Property(name="material_use",  type=material_use, multiplicity=zero_many, is_navigable=False)})
a_lifecycle_parameter: BinaryAssociation = BinaryAssociation(name="rel_lifecycle_parameter", ends={
    Property(name="enviromental_impacts",  type=parameter, multiplicity=zero_many, is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=one, is_navigable=False, is_composite=True)})
a_lifecycle_peson: BinaryAssociation = BinaryAssociation(name="rel_lifecycle_person", ends={
    Property(name="issuer",  type=person, multiplicity=one, is_navigable=True),
    Property(name="issue",  type=lifecycle_stage, multiplicity=zero_many, is_navigable=False)})
a_parameter_metric: BinaryAssociation = BinaryAssociation(name="rel_parameter_metric", ends={
    Property(name="metric",  type=metric, multiplicity=one, is_navigable=True),
    Property(name="value",  type=parameter, multiplicity=zero_many, is_navigable=False)})
a_use_reparation: BinaryAssociation = BinaryAssociation(name="rel_use_reparation", ends={
    Property(name="reparations",  type=reparation, multiplicity=zero_many, is_navigable=True),
    Property(name="use_stage",  type=use, multiplicity=one, is_navigable=False)})
a_reparation_material: BinaryAssociation = BinaryAssociation(name="rel_reparation_material", ends={
    Property(name="materials",  type=material_use, multiplicity=zero_many, is_navigable=True),
    Property(name="reparation",  type=reparation, multiplicity=zero_one, is_navigable=False)})
a_manufacture_company: BinaryAssociation = BinaryAssociation(name="rel_manufacture_company", ends={
    Property(name="companies",  type=company, multiplicity=one_many, is_navigable=True),
    Property(name="stage",  type=lifecycle_stage, multiplicity=zero_many, is_navigable=False)})
a_person_company: BinaryAssociation = BinaryAssociation(name="rel_person_company", ends={
    Property(name="company",  type=company, multiplicity=one, is_navigable=True),
    Property(name="employee",  type=person, multiplicity=zero_many, is_navigable=False)})

# Associations
associations: set[Association] = {a_person_company, a_product_carrier, a_product_lifecycle, a_material_raw, a_product_hazard,
                                  a_material_stage, a_manufacture_company, a_lifecycle_parameter, a_parameter_metric, a_use_reparation, 
                                  a_reparation_material, a_product_recycled, a_product_chemical, a_lifecycle_peson}

# Generalizations
gen_lf_design: Generalization = Generalization(general=lifecycle_stage, specific=design)
gen_lf_manufacture: Generalization = Generalization(general=lifecycle_stage, specific=manufacture)
gen_lf_distribution: Generalization = Generalization(general=lifecycle_stage, specific=distribution)
gen_lf_use: Generalization = Generalization(general=lifecycle_stage, specific=use)
gen_lf_collect: Generalization = Generalization(general=lifecycle_stage, specific=collect)
gen_lf_recycle: Generalization = Generalization(general=lifecycle_stage, specific=recycle)

generalizations: set[Generalization] = {gen_lf_design, gen_lf_manufacture, gen_lf_distribution, gen_lf_use, gen_lf_collect, 
                                        gen_lf_recycle}

# Enumerations
enumerations: set[Enumeration] = {manualtype_enum, source_enum, carrier_enum}

# Domain Model
dpp_domain: DomainModel = DomainModel(name="Digital Product Passport", 
                                      types=classes, 
                                      associations=associations, 
                                      generalizations=generalizations,
                                      enumerations= enumerations
                                      )

# Django code generation
django_generator: DjangoGenerator = DjangoGenerator(model=dpp_domain, output_dir="django_code")
django_generator.generate()

# RDF vocabulary generation
rdf_generator: RDFGenerator = RDFGenerator(model=dpp_domain, output_dir="rdf_code")
rdf_generator.generate()
