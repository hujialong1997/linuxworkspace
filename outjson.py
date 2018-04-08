import web
import json
class index:
    def GET(self):
        pyDict={'one':1,'two':2}
        web.header('Content-Type','text/json',unique=False)
        return json.dump(pyDict)
