""" 常量的配置 """

from enum import Enum


class UserStatus(Enum):     #用户的状态
    USER_ACTIVE  = 1    #用户可以登录
    USER_IN_ACTIVE = 0      #如果是0则表示用户不能登录


class UserRole(Enum):
    """ 用户的角色：是否是管理员 """
    COMMON = 0   #普通用户，只能使用前台功能
    ADMIN = 1     #管理员，可以修改用户的信息
    SUPER_ADMIN = 2   #超级管理员，可以删除敏感的信息