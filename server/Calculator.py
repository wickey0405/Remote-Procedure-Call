from function_folder import myFunctions
import math

class Calculator:
    def __init__(self):
        self.info = {}
        self.function_tables = {}
        self.createFunctionTable()

    def createFunctionTable(self):
        self.function_tables["floor"] = myFunctions.floor
        self.function_tables["nroot"] = myFunctions.nroot
        self.function_tables["reverse"] = myFunctions.reverse
        self.function_tables["validAnagram"] = myFunctions.validAnagram
        self.function_tables["sort"] = myFunctions.sort

    def checkPOST(self, json_data):
        if json_data.get("method") == None: return False
        if json_data.get("params") == None: return False
        if json_data.get("param_types") == None: return False
        if json_data.get("id") == None: return False
        return True
    
    def setInfo(self, json_data):
        if self.checkPOST(json_data):
            method = json_data.get("method")
            params = json_data.get("params")
            param_types = json_data.get("param_types")
            id = json_data.get("id")
            self.info[id] = {
                "method": method,
                "params": params,
                "param_types": param_types,
                "result": 0,
                "result_types": ""
            }

    def createResopnseJSON(self, json_data):
        id = json_data.get("id")
        res = {
            "result": self.info.get(id)["result"],
            "result_types": self.info.get(id)["result_types"],
            "id": id
        }
        return res

    def runFunc(self, json_data):
        id = json_data.get("id")
        if not id in self.info:
            self.info.get(id)["result"] = "this id doesn't exist"
        else:
            self.info.get(id)["result"], self.info.get(id)["result_types"] = self.function_tables.get(self.info.get(id)["method"])(self.info.get(id)["params"], self.info.get(id)["param_types"])

        return self.createResopnseJSON(json_data)