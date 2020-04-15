#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from algorithms import ImageProcessing
from files import FileOperations

class AlgorithmValidation:
    
    def validate(self, validation_data_rootpath):
        # Get image directories list
        dirs = FileOperations.list_image_directories(validation_data_rootpath, debug=False)

        #images = ["1.jpg", "2.jpg", "3.jpg"]
        
        plate_areas_std_dev_list = list()
        dirty_areas_std_dev_list = list()
        dirt_plate_rates_std_dev_list = list()

        for dir in dirs:
            plate_areas = list()
            dirty_areas = list()
            dirt_plate_rates = list()

            print("-"*50)
            print(dir)

            images = FileOperations.list_files(dir, debug=False)
            for im_path in images:
                # im_path = dir + image
                plate_area, dirty_area, dirt_plate_rate = ImageProcessing.calculateDirtyInfo(im_path)

                plate_areas.append(plate_area)
                dirty_areas.append(dirty_area)
                dirt_plate_rates.append(dirt_plate_rate)
            
            std_plate_areas = np.std(plate_areas)
            std_dirty_areas = np.std(dirty_areas)
            std_dirt_plate_rates = np.std(dirt_plate_rates)
            print("Plate area std: {}\tDirty area std: {}\tRate of dirty/plate std: {}".format(std_plate_areas, std_dirty_areas, std_dirt_plate_rates))
            
            plate_areas_std_dev_list.append(std_plate_areas)
            dirty_areas_std_dev_list.append(std_dirty_areas)
            dirt_plate_rates_std_dev_list.append(std_dirt_plate_rates)
        
        print("="*50)
        print("Plate Area standart deviation's mean: {}".format(np.mean(plate_areas_std_dev_list, dtype=np.float64)))
        print("Dirty Area standart deviation's mean: {}".format(np.mean(dirty_areas_std_dev_list, dtype=np.float64)))
        print("Dirt/Plate Rate standart deviation's mean: {}".format(np.mean(dirt_plate_rates_std_dev_list, dtype=np.float64)))


def main():
    validator = AlgorithmValidation() 
    validation_path = "/media/sf_shared/image_processing/validation"
    validator.validate(validation_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Error: " + err.message)