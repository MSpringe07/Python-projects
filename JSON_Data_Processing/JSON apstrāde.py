import json

data = {"key1": "value1", "key2": "value2"}
json_data = json.dumps(data)
print("1.uzd:", json_data, "\n")


JSON_given = """{"key1": "value1", "key2": "value2"}"""
data_dict = json.loads(JSON_given)
value_of_key2 = data_dict["key2"]
print("2.uzd:", value_of_key2, "\n")


JSON_given = {"key1": "value1", "key2": "value2", "key3": "value3"}
formatted_json = json.dumps(JSON_given, indent=2, separators=(",", " = "))
print("3.uzd:", formatted_json, "\n")


JSON_given = {"id": 1, "name": "value2", "age": 29}
sorted_json = json.dumps(JSON_given, sort_keys=True)
with open('sorted_data.json', 'w') as file:
    file.write(sorted_json)


JSON_given = """{
   "company":{
      "employee":{
         "name":"emma",
         "payable":{
            "salary": 7000,
            "bonus": 800
         }
      }
   }
}"""
data_dict = json.loads(JSON_given)
salary = data_dict["company"]["employee"]["payable"]["salary"]
print("5.uzd:", salary, "\n")
