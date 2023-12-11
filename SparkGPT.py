# ！/usr/bin env python3
# -*- coding: utf-8 -*-
# author: yangyunlong time:2023/12/1
import SparkApi
from abc import ABC, abstractmethod

appid = ""  # 填写控制台中获取的 APPID 信息
api_secret = ""  # 填写控制台中获取的 APISecret 信息
api_key = ""  # 填写控制台中获取的 APIKey 信息


class BaseLLM(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def initialize_message(self):
        pass

    @abstractmethod
    def ai_message(self, payload):
        pass

    @abstractmethod
    def system_message(self, payload):
        pass

    @abstractmethod
    def user_message(self, payload):
        pass

    @abstractmethod
    def get_response(self):
        pass

    @abstractmethod
    def print_prompt(self):
        pass


class SparkGPT(BaseLLM):

    def __init__(self, model="Spark3.0"):
        super(SparkGPT, self).__init__()
        if model == "Spark2.0":
            self.domain = "generalv2"  # v2.0版本
            self.Spark_url = "ws://spark-api.xf-yun.com/v2.1/chat"  # v2.0环境的地址
        elif model == "Spark1.5":
            self.domain = "general"  # v1.5版本
            self.Spark_url = "ws://spark-api.xf-yun.com/v1.1/chat"  # v1.5环境的地址
        elif model == "Spark3.0":
            self.domain = "generalv3"
            self.Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"
        else:
            raise Exception("Unknown Spark model")
        # SparkApi.answer =""
        self.messages = ''

    def initialize_message(self):
        self.messages = ''

    def ai_message(self, payload):
        self.messages = self.messages + payload

    def system_message(self, payload):
        self.messages = self.messages + payload

    def user_message(self, payload):
        self.messages = self.messages + payload

    def get_response(self):
        # question = checklen(getText("user",Input))

        message_json = [{"role": "user", "content": self.messages}]
        SparkApi.answer = ""
        SparkApi.main(appid, api_key, api_secret, self.Spark_url, self.domain, message_json)
        return SparkApi.answer

    def print_prompt(self):
        print(type(self.messages))
        print(self.messages)
