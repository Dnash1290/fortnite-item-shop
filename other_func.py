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