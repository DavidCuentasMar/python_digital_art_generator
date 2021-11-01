# Python Digital Art Generator

The main goal of this repository is to generate all possible layers permutations 
given by the user in order to get unique images

## User Guide
Steps:
- Put all your images inside "resources" folder
- Use config.js file to specify order or hierarchy of the images
- Run this command once you are inside docker image: python run.py main

This script will save all unique images inside collections/images folder and the metadata
will be under collections/metadata folder

## Configuration of config.js file

config.js file has the following structure. 
```JSON
{
    "layers":{
        "layer_0":[
            "img_a",
            "img_b"
        ],
        "layer_1":[
            "img_c",
            "img_c_2",
            "img_c_3"
        ],
        "layer_2":[
            "img_d"
        ],
        "layer_3":[
            "img_e"
        ]    
    }
}
```
- The order of the layers are specified with the number associated. Example: layer_0 is the bottom and layer_3 is the top.
- Layer_x is a list of the file names (excluding the extension file) that can be used as main image in that layer. Example: for layer_0 the script only will use img_a or img_b when it's creating the first layer
- If you want to have more layers you can easily add them as another layer_x json array attribute
- If you want a specific output name instead of "digital_art" for your collections you can run this command: python run.py main --output_name MY_CUSTOM_NAME
- Note: :hearts: For now please use png images :pray: :sweat_smile: