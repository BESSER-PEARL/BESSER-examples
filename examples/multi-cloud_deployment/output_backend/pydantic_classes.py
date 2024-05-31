from datetime import datetime, date
from typing import List, Optional, Union,Set
from pydantic import BaseModel

############################################
#
# The classes are defined here
#
############################################

class LifecycleStageCreate(BaseModel):
    end: date
    start: date

    rawmaterials_id: List[int]

            

    productpassports_id: List[int]

            

 

class DesignCreate(LifecycleStageCreate):

    pass
 

class UseCreate(LifecycleStageCreate):

            

    pass
 

class ManufactureCreate(LifecycleStageCreate):

    pass
 

class DistributionCreate(LifecycleStageCreate):

    pass
 

class RawMaterialCreate(BaseModel):
    name: str

    lifecyclestages_id: List[int]

            

 

class ProductPassportCreate(BaseModel):
    brand: str
    code: str
    product_name: str

    lifecyclestages_id: List[int]

            

 

class ReparationCreate(BaseModel):
    description: str
    date_set: date

    use_id: int

            

 

