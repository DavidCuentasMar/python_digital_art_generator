import os
import logging
import json
import itertools
from PIL import Image, ImageDraw

class Controller:
    """Object controller."""

    @classmethod    
    def worker(cls, output_name):
        logging.info(f'[INIT] python_digital_art_generator worker')
        
        try:
            f = open('config.json')
        except Exception as e:
            logging.error(e)
            return
        
        config_json = json.load(f)
        layers_json_list = config_json.get('layers')
        no_of_layers = len(layers_json_list)

        logging.info(f'[INIT] No. of layers = {no_of_layers}')
        
        resources_path = 'resources/'
        filenames_list = os.listdir(resources_path)
        filenames_list = list(map(lambda x: x.split(".")[0], filenames_list))
        collections = []
        permutations = itertools.permutations(filenames_list, 4)
        for x in permutations:
            if cls.check_hierarchy(x, layers_json_list):
                collections.append(x)
        cls.build_images(collections, output_name)

    @classmethod
    def check_hierarchy(cls, possible_collection, layers_json_list):
        last_level = cls.get_image_level(possible_collection[0], layers_json_list)
        print('Current collection: ', possible_collection)
        for x in range(1, len(possible_collection)):
            current_level = cls.get_image_level(possible_collection[x], layers_json_list)
            print(last_level)
            print(current_level)
            print('----')
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
    def build_images(cls, collections, output_name):
        logging.info(f'[STEP] building imagenes')
        resources_extension = 'png'
        for index, collection in enumerate(collections):
            nft_collection_image = Image.new('RGBA', (250,250),(255, 0, 0, 0))
            for img in collection:
                image_to_merge = Image.open(f'resources/{img}.{resources_extension}')
                nft_collection_image  = Image.alpha_composite(nft_collection_image,image_to_merge)
            nft_collection_image.save(f'collections/{output_name}_no_{index}.png',"PNG")
        logging.info(f'[STEP] building imagenes finished')
