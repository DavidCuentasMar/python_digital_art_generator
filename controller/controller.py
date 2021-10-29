import os
import logging
import json
import itertools
from PIL import Image

class Controller:
    """Object controller."""

    @classmethod
    def worker(cls):
        logging.info(f'[INIT] python_ntf_generator worker')
        
        try:
            f = open('config.json',)
        except Exception as e:
            logging.error(e)
            return
        
        config_json = json.load(f)
        layers_json_list = config_json.get('layers')
        no_of_layers = len(layers_json_list)

        logging.info(f'[INIT] No. of layers = {no_of_layers}')
        f = ['img_a','img_b','img_c','img_c_2','img_c_3','img_d','img_e']
        combinations = itertools.combinations(f, 4)

        collections = []
        for x in combinations:
            if cls.check_hierarchy(x, layers_json_list):
                collections.append(x)
        print(len(collections))
        cls.build_images(collections)

    @classmethod
    def check_hierarchy(cls, possible_collection, layers_json_list):
        last_level = cls.get_image_level(possible_collection[0], layers_json_list)
        for x in range(1, len(possible_collection)):
            current_level = cls.get_image_level(possible_collection[x], layers_json_list)
            if last_level >= current_level:
                return False
            last_level = current_level
        return True

    @classmethod
    def get_image_level(cls, image, layers_json_list):
       for layer in layers_json_list:
           if image in layers_json_list.get(layer):
               return int(layer.split("_")[1])
    
    @classmethod
    def build_images(cls, collections):
        resources_extension = 'png'
        for index, collection in enumerate(collections):
            nft_collection_image = Image.new('RGBA', (250,250),'WHITE')
            for img in collection:
                image_to_merge = Image.open(f'resources/{img}.{resources_extension}')
                nft_collection_image  = Image.alpha_composite(nft_collection_image,image_to_merge)
                #nft_collection_image .paste(image_to_merge,(0,0),image_to_merge)
            nft_collection_image.save(f'collections/ntf_no_{index}.png',"PNG")