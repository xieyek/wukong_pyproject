# -*- encoding:utf-8 -*-
# 请求方式封装

import requests


class Http:
    @staticmethod
    def get(url, data, token, ant_action=None):
        data = requests.get(url, data, headers={'Authorization': token, 'Content-Type': 'application/json',
                                                'accept': 'application/psr.ant.v1+json', "Ant-Action": ant_action},verify=False,)
        return data

    @staticmethod
    def post(url, data, token, ant_action=None):
        data = requests.post(url,data,headers={'Authorization': token, 'Content-Type': 'application/json',
                                                 'accept': 'application/psr.ant.v1+json', "Ant-Action": ant_action},verify=False,)
        return data

    @staticmethod
    def put(url, data, token, ant_action=None):
        data = requests.put(url, data, headers={'Authorization': token, 'Content-Type': 'application/json',
                                                'accept': 'application/json', "Ant-Action": ant_action})
        return data

    @staticmethod
    def delete(url, token, data1=None, ant_action=None):
        data = requests.delete(url, headers={'Authorization': token, 'Content-Type': 'application/json',
                                             'accept': 'application/json', "Ant-Action": ant_action}, data=data1)
        return data

    @staticmethod
    def patch(url, data, token, ant_action=None):
        data = requests.patch(url, data, headers={'Authorization': token, 'Content-Type': 'application/json',
                                                 'accept': 'application/psr.ant.v1+json', "Ant-Action": ant_action})
        return data
