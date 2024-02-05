import json, requests
from PIL import Image
from io import BytesIO
from datetime import datetime 
import os, shutil


class File:

    def get_request(self):
        r = requests.get("https://fortnite-api.com/v2/shop/br")
        code = r.status_code
        if code != 200:
            raise Exception("idk some random code (its not 200!!!)")
        
        data = r.json()      
        with open("api_data.json","w") as f:
            json.dump(data,f,indent=3)
            print("json updated")
            
    def get_objects(self):
        with open("api_data.json","r") as f:
            print("json loaded")
            return json.load(f)
        
    def write_date(self, date):
        with open("dates.txt","r+") as f:
            copy = f.read()
            f.seek(0)
            f.write(date+"\n"+copy)
            
    def already_updated(self, date):
        with open("dates.txt","r") as f:
            old_date = f.readline()[:-1]
            if date != old_date:
                print(date,f.readline())
                return True
            return False

class ItemShop:

    def all_items():
        for item in items:
            print(item["id"],":\n",item["name"],"\n",item["type"]["value"],"\n")
            
    def save_image(self,image_url,name):
        if image_url == None:
            print("image is None")
            return
        
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = BytesIO(response.content)
            image = Image.open(image_data)
            name = name
            
            image.save(f"{self.path}/{name}.png")
            print(f"Image saved as {name}")
        else:
            print("Failed to fetch image")
      
    def check_empty_files(self):
        dir = os.listdir("./bundle") 
        for folder in dir:
            file = os.listdir("./bundle/"+folder)
            print(file)  
            if len(file) == 0:
                os.rmdir("./bundle/"+folder)
        
        dir = os.listdir("./bundle") 
        index = 1
        for folder_name in dir:
            print("folder name",folder_name)
            folder = folder_name.split()
            if folder[1] == index:
                continue
            temp = folder_name
            os.rename(folder_name,)
                
        

    #---------------------------------- the used method-------------------
    def daily_items(self,data):  
        #print(data["data"]["daily"].keys())
        print(data["data"]["featured"]["entries"][0]["bundle"]["name"])
        weekend_bundle = (data["data"]["featured"]["entries"])
        
        if os.path.exists("bundle"):
            shutil.rmtree("bundle")
        os.mkdir("./bundle")
        
        count = 1
        for item in weekend_bundle:
            items_data = item["items"]
            name = item["devName"].split()
            name = name[2]+" "+name[3]
            name = f"bundle {count} {name}"
            self.path = f"./bundle/{name}"
            os.mkdir(self.path)
            
            print(item["finalPrice"],name,"deal No.",count)
            print(item["layout"]["background"])#backgorund
            bundle = item["newDisplayAsset"]["materialInstances"]# all skin style_nos
            item_types = item["items"]

            
            style_no = 1
            for (content, item_type) in zip(bundle, item_types):
                if item_type["type"]["value"] != "outfit" and style_no == 1:
                    continue
                item_type["type"]["value"]
                image = content["images"]["Background"]
                print("style_no",style_no,image)
                print("-----------------\n\n")
                name_temp = name+"style"+str(style_no)
                self.save_image(image,name_temp)
                style_no += 1
            count += 1
        self.check_empty_files()
            
f = File()
#f.get_request()
time = datetime.now()        
'''
date = time.strftime("%x")
print("today",date,"now",time.now())
f.write_date(date)
print(f.already_updated(date))
'''

data = f.get_objects()
#print(data["data"]["daily"].keys())

items = ItemShop()
print(items.check_empty_files())
x = x+2

items.daily_items(data)


