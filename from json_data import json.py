import json

from json import json
from types import new_class
json_file = "participants.json"

class lottery: 
    def register(): 
        card = input ("Escribe tu cedula para participar:")
        new_participant ={"card":card}
        print( new_participant)
    
    try:
         data = json.read(json_file)
         data.append(new_participant)
         
         json.write(json_file,data)
    
    except:
        json.write(json_file, [new_participant])

lottery.register()      