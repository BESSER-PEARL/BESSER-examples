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

The generated code for the Django web application will be stored in the `dpp_project` folder.

Now you can deploy your Django application using the generated code. Below is the admin panel of the Django web application generated. The steps to run the web application are detailed in the [BESSER documentation](https://besser.readthedocs.io/en/latest/generators/django.html).

<p align="center">
<img src="/examples/dpp/django.png" alt="Django App" style="height: 70%; width:70%;"/>
</p>
