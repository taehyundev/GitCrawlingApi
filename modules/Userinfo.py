import json
import MakeJson
def UserInfo():
    u_info = {0:{"name":"강태현", "url":"https://github.com/taehyundev"},
              1:{"name":"이수진", "url":"https://github.com/leeejin"}
    }
    return MakeJson.m_json("data/userinfo.json",u_info ) #Path와 User
UserInfo()