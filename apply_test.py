#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from algorithms import ImageProcessing
from files import FileOperations
from collections import defaultdict
from dict_operations import DictOperations

class Repeat:
    repeat_no = ""
    mean_o = 0.0
    mean_s = 0.0
    rate = 0.0 #((öncesi-sonrası)/öncesi)*100

class Test:
    test_name = ""
    test_list = list()

class ApplyTest:
    
    def rec_dd(self):
        return defaultdict(self.rec_dd())

    def createRepeatMap(self, test_data_rootpath):
        dir_list = FileOperations.getDirectoryList(test_data_rootpath)

        resultMap = dict()
        for test_name in dir_list:
            resultMap[test_name] = Repeat()
        
        return resultMap

    def test(self, test_data_rootpath):
        # Get image directories list
        dirs = FileOperations.list_image_directories(test_data_rootpath, debug=False)
        resultMap = self.createRepeatMap(test_data_rootpath)

        # Create nested dictionary map
        test_map = DictOperations.nested_dd()

        plate_areas_std_dev_list = list()
        dirty_areas_std_dev_list = list()
        dirt_plate_rates_std_dev_list = list()

        i = 0
        for dir in dirs:
            i = i + 1
            # if i > 2:
            #     break
            plate_areas = list()
            dirty_areas = list()
            dirt_plate_rates = list()

            print("-"*50)
            print(dir)

            images = FileOperations.list_files(dir, debug=False)
            for im_path in images:
                plate_area, dirty_area, dirt_plate_rate = ImageProcessing.calculateDirtyInfo(im_path)

                plate_areas.append(plate_area)
                dirty_areas.append(dirty_area)
                dirt_plate_rates.append(dirt_plate_rate)
            
            std_plate_areas = np.std(plate_areas)
            std_dirty_areas = np.std(dirty_areas)
            std_dirt_plate_rates = np.std(dirt_plate_rates)
            mean_dirt_plate_rates = np.mean(dirt_plate_rates)
            print("Plate area std: {}\tDirty area std: {}\tStd of dirty/plate: {}\tMean of dirty/plate: {}".format(std_plate_areas, std_dirty_areas, std_dirt_plate_rates, mean_dirt_plate_rates))
            
            test_name =  dir.split("/")[5]
            repeat_number = dir[-4]
            # resultMap[test_name].repeat_no = repeat_number
            test_time = dir[-2] # o or s
            test_map[test_name][repeat_number][test_time] = mean_dirt_plate_rates
            # if dir[-2] == "s":
            #     resultMap[test_name].mean_s = mean_dirt_plate_rates
            # else:
            #     resultMap[test_name].mean_o = mean_dirt_plate_rates

            plate_areas_std_dev_list.append(std_plate_areas)
            dirty_areas_std_dev_list.append(std_dirty_areas)
            dirt_plate_rates_std_dev_list.append(std_dirt_plate_rates)

            print("{}:\t {}\t {}\t {}".format(test_name, repeat_number, test_time, mean_dirt_plate_rates))
        
        test_map = DictOperations.calc_result(test_map)

        print("="*50)
        DictOperations.printResult(test_map)

        print("="*50)
        DictOperations.printTable(test_map)
        
        print("="*50)
        print("Plate Area standart deviation's mean: {}".format(np.mean(plate_areas_std_dev_list, dtype=np.float64)))
        print("Dirty Area standart deviation's mean: {}".format(np.mean(dirty_areas_std_dev_list, dtype=np.float64)))
        print("Dirt/Plate Rate standart deviation's mean: {}".format(np.mean(dirt_plate_rates_std_dev_list, dtype=np.float64)))


def main():
    validator = ApplyTest() 
    test_path = "/media/sf_shared/image_processing/test"
    # test_path = "/media/sf_shared/image_processing/validation"
    validator.test(test_path)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print("Error: " + err.message)