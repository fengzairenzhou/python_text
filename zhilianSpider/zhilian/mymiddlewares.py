#coding:utf8

from settings import USER_AGENTS
import random

# 随机换 USER_AGENT
class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault('User_Agent',user_agent)