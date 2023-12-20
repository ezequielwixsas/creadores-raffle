import json 

class json:
    def write(file_name,save_json):
        with open(file_name,"w") as outfile: 
           
              json.dump(save_json,outfile)
         

