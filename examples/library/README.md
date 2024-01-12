# Library Example

In this basic example, we will model the Library domain represented in the following class diagram, and then 
run some code generators.

<img src="/examples/library/library_class_diagram.jpg" alt="WWTP" style="height: 70%; width:70%;"/>

Let's look at three different ways to create this model in BESSER using the B-UML language.

### 1. Build the B-UML model using Python code and run the code generators.

In `library.py` you can find the code that defines the B-UML model (classes, attributes, and relationships) and the instructions to implement the code generators. Run the script:

```sh
python library.py
```

And you will get the generated code in the `output/` folder.

### 2. Build the B-UML model from a PlantUML model and run the code generators

In `plantuml2buml.py` you will find the code to transform the `library.plantuml` model to a B-UML model and execute the code generators.

```sh
python plantuml2buml.py
```

You will get the generated code in the `output/` folder. Additionally, the source code to build the B-UML model will be stored in the `buml/` folder.

### 3. Build the B-UML model from an image and run the code generators

In `image2buml.py` you can check the code to transform the image `library_hand_draw.png` to a B-UML model. For this we use [OpenAI's GPT4](https://openai.com/gpt-4), so you must provide an OpenAI token to implement this BESSER functionality. Update the `opneai_token` parameter of the `image_to_buml` function and execute the code.

```sh
python image2buml.py
```

The code produced by the generators will be stored in the `output/` folder and the source code to build the B-UML model in the `buml/` folder.