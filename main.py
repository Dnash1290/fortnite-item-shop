import json, requests
from PIL import Image
from io import BytesIO
from datetime import datetime 

class File:

    def get_request(self):
        r = requests.get("https://fortnite-api.com/v2/shop/br")
        code = r.status_code
        if code != 200:
            raise Exception("idk some random code (its not 200!!!)")
        
        data = r.json()      
        with open("api_data.json","w") as f:
            json.dump(data,f,indent=3)
            
    def get_objects(self):
        with open("api_data.json","r") as f:
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

def all_items():
    for item in items:
        print(item["id"],":\n",item["name"],"\n",item["type"]["value"],"\n")
        
def save_image(image_url,name):
    if image_url == None:
        print("image is None")
        return
    
    response = requests.get(image_url)
    if response.status_code == 200:
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        name = name
        image.save(f"bundle/{name}.png")
        print(f"Image saved as {name}")
    else:
        print("Failed to fetch image")

def skins():         
    for item in items:
        if item["type"]["value"] == "outfit":
            print(item["id"],":\n",item["images"]["icon"],":\n",item["images"]["featured"])
            
            save_image(item["images"]["icon"],item["id"]+"icon")
            save_image(item["images"]["featured"],item["id"])
            print(item["images"]["other"],"\n\n")
    
    
def other_item_pic():
    for item_info in items_data: #items >images> have not explores variants
        print(item_info["type"]["value"],":",item_info["name"])
        print(item_info["images"]["featured"])
        print(item_info["images"]["other"],"\n")
        image_url = item_info["images"]["featured"]
        name = item_info["name"]
        print(name)
        input()      
f = File()
time = datetime.now()        

date = time.strftime("%x")
print("today",date,"now",time.now())
f.write_date(date)
print(f.already_updated(date))

raise Exception ("balls ")
    

data = f.get_objects()
print(data["data"]["daily"].keys())
print(data["data"]["featured"]["entries"][0]["bundle"]["name"])
weekend_bundle = (data["data"]["featured"]["entries"])

count = 1
for item in weekend_bundle:
    items_data = item["items"]
    name = item["devName"].split()
    name = name[2]+" "+name[3]
    name = f"bundle {count} {name}"
    
    print(item["finalPrice"],name,"deal No.",count)
    print(item["layout"]["background"])#backgorund
    bundle = item["newDisplayAsset"]["materialInstances"]# all skin style_nos
    style_no = 1
    for content in bundle:
        image = content["images"]["Background"]
        print("style_no",style_no,image)
        print("-----------------\n\n")
        name_temp = name+"style"+str(style_no)
        save_image(image,name_temp)
        style_no += 1
    count += 1

