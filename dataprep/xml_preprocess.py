import json
import os
import xml.etree.ElementTree as ET

def xml_to_jsons(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    json_data = {}
    
    file_name = root.find("filename").text
    json_data["file_name"] = file_name
    
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    depth = int(size.find("depth").text)
    json_data["size"] = {"width": width, "height": height, "depth": depth}
        
    objects = root.findall("object")
    if len(objects) == 0:
        print("do not have any objects")
        return None
    
    classes = []
    bboxes = []
    for obj in objects:
        name = obj.find("name").text
        classes.append(name)
        
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)
        bboxes.append({"xmin": xmin, "ymin": ymin, "xmax": xmax, "ymax": ymax})
        
    json_data["classes"] = classes
    json_data["bboxes"] = bboxes
    
    return json_data

    
    
    
if __name__ == "__main__":
    annos = os.listdir("annotations") 
    os.makedirs("json_annotations", exist_ok=True)
    for anno in annos:
        json_data = xml_to_jsons(f"annotations/{anno}")
        
        if json_data == None:
            continue
        
        with open(f'json_annotations/{anno}.json', 'w') as file:
            json.dump(json_data, file)