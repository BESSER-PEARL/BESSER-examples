# Digital Product Passport (DPP) Example

[Digital Product Passport (DPP)](https://hadea.ec.europa.eu/calls-proposals/digital-product-passport_en) is a European initiative that seeks to improve the circular economy by optimizing the design, manufacture, and use of products. This initiative consists of collecting and disseminating information on products during the different stages of their life cycle.

In this example, we show how from a [plantUML](https://plantuml.com/class-diagram) model (which describes a reduced DPP domain) it is possible to obtain a B-UML model, serialize it, and use it as input to our [Django](https://www.djangoproject.com/) code generator to produce the model layer code of a Django web application.

The PlantUML class model that describes the domain is as follows (you can find the code in `dpp.plantuml` file).

<p align="center">
<img src="/examples/dpp/dpp_model.png" alt="WWTP" style="height: 60%; width:60%;"/>
</p>

Run the script `dpp.py`.

```sh
python dpp.py
```

The generated code for the model layer of the Django application will be stored in the `output/models.py` file. Additionally, the code to define the B-UML model is generated in `buml/buml_model` (this code can be used if you want to modify your model directly from the base code).

Now you can create your Django application and use the generated code. Below is the admin panel of a Django web application that uses the code generated for the data layer or model layer.

<p align="center">
<img src="/examples/dpp/django.png" alt="Django App" style="height: 70%; width:70%;"/>
</p>
