# coding=UTF-8
""" FAKE_USER
# INFO:    创建虚拟测试用户信息
# VERSION: 2.0
# EDITOR:  thomas
# TIMER:   2021-03-09
"""

import random
import string
from faker import Faker
from faker.providers import BaseProvider
import hashlib


Faker.seed(2025)
location = ["en-US", "zh_CN"]

class SystemRole(BaseProvider):
    # create new provider class for apulis ai platform user roles
    Role = ["System Admin", "User", "Annotation Person" ]
    def role(self):
        return random.choice(self.Role)

class ChinesePhone(BaseProvider):
    # create new provider class for chinese mainland cellphone numbers 
    PhoneChinaPrefix = [
    '130', '131', '132', '133', '134', '135', '136', '137', '138', '139',
    '145', '147', '149', '150', '151', '152', '153', '155', '156', '157',
    '158', '159', '165', '171', '172', '173', '174', '175', '176', '177',
    '178', '180', '181', '182', '183', '184', '185', '186', '187', '188',
    '189', '191'
    ]
    def MainlandCellPhone(self):
        
        return ''.join([self.PhoneChinaPrefix[random.randint(0, len(self.PhoneChinaPrefix) - 1)],''.join(random.sample(string.digits, 8))])


def new_fake_user():
    DataFactory = Faker(location=["en-US", "zh_CN"])
    Nickname = DataFactory.name()
    DataFactory = Faker(location=["en-US"])
    Username = DataFactory.first_name_nonbinary()
    Firstname = DataFactory.first_name()
    Lastname = DataFactory.last_name()
    Passwd = "1234567890"
    Md5Passwd = hashlib.md5()
    Md5Passwd.update(Passwd.encode("utf-8"))
    SecurityPasswd = (Md5Passwd.hexdigest()).lower()
    DataFactory.add_provider(ChinesePhone)
    Phone = DataFactory.MainlandCellPhone()
    Email = DataFactory.ascii_free_email()
    Description = DataFactory.job()
    DataFactory.add_provider(SystemRole)
    Role = DataFactory.role()  
    return {"Nickname":Nickname,
            "Username":Username,
            "Firstname":Firstname,
            "Lastname":Lastname,
            "passwd":SecurityPasswd,
            "Phone":Phone,
            "Email":Email,
            "Description":Description,
            "Role":Role
            }


if __name__ == "__main__":
    print(new_fake_user())