#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import defaultdict
import numpy as np

class DictOperations:

    # creates nested dict
    @staticmethod
    def nested_dd():
        return defaultdict(DictOperations.nested_dd)

    @staticmethod
    def calc_result(t):
        for i, (k, v)in enumerate(dict(t).items()):
            print(k)
            for j, (kk, vv) in enumerate(dict(t[k]).items()):
                print(kk)
                r = dict(vv)
                print(r)
                t[k][kk]['result'] = ((r['o'] - r['s']) / r['o']) * 100  #((öncesi-sonrası)/öncesi)*100
                

        # for i, (k, v)in enumerate(dict(t).items()):
        #     print(k)
        #     for j, (kk, vv) in enumerate(dict(t[k]).items()):
        #         print(dict(vv))
        return t

    @staticmethod
    def printResult(t):
        print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format('Test Name','Tekrar', 'Oncesi','Sonrasi','Sonuc'))
        for i, (k_testname, v)in enumerate(dict(t).items()):
            for j, (k_repeatno, vv) in enumerate(dict(t[k_testname]).items()):
                d = dict(vv)
                print ("{:<20} {:<20} {:<20} {:<20} {:<20}".format(k_testname, k_repeatno, d['o'], d['s'], d['result']))

    @staticmethod
    def printTable(test_map):
        template = "{:<20} {:<20} {:<20} {:<20}"
        print (template.format('Test Name','1. Tekrar', '2. Tekrar', 'Ortalama'))
        for i, (k_testname, v)in enumerate(dict(test_map).items()):
            t_rates = list()

            for i in v.keys():
                t_rates.append(v[i]['result'])
            t_mean = np.mean(t_rates)
            print (template.format(k_testname, v['1']['result'], v['2']['result'], t_mean))

    @staticmethod
    def printTableVal(test_map):
        template = "{:<20} {:<20} {:<20} {:<20} {:<20}"
        print(template.format('Test Name','1. Tekrar', '2. Tekrar', '3. Tekrar', 'Ortalama'))
        for i, (k_testname, v)in enumerate(dict(test_map).items()):
            t_rates = list()
            for i in v.keys():
                t_rates.append(v[i]['result'])
            t_mean = np.mean(t_rates)
            print(template.format(k_testname, v['1']['result'], v['2']['result'], v['3']['result'], t_mean))


# t = DictOperations.nested_dd()

# t['a']['1']['o'] = 1.45
# t['a']['1']['s'] = 2.34


# t['a']['2']['o'] = 3.3
# t['a']['2']['s'] = 4.5


# t = DictOperations.calc_result(t)
# DictOperations.printResult(t)
# DictOperations.printTable(t)




