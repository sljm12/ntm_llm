from geojson import Feature, Polygon, MultiPolygon, FeatureCollection, Point
from pathlib import Path
import json
from glob import glob

def get_geojson(obj):
    geo_type = obj["type"]
    if geo_type == "Polygon":
        return Polygon(obj["coordinates"])
    elif geo_type == "Point":
        return Point(obj["coordinates"])

def get_properties(ntm_obj):
    keys = ["ntm_number", "notice_date", "event", "date_from", "date_to", "other information"]
    r_obj = {}
    for k in keys:
        r_obj[k] = ntm_obj[k]
    return r_obj

def process_file(filename):
    text = Path(filename).read_text()
    j_obj = json.loads(text)

    locations = j_obj["locations"]
    t = type(locations)
    
    feature_list = []
    if t == list:        
        for l in locations:
            obj = get_geojson(l)
            f = Feature(geometry=obj, properties=get_properties(j_obj))
            print(f.is_valid)
            print(f.errors())
            feature_list.append(f)            
        return  feature_list
    else:
        obj = get_geojson(locations)
        f = Feature(geometry=obj, properties=get_properties(j_obj))
        feature_list.append(f)            
        return  feature_list
        
        
if __name__ == "__main__":
    files = glob(".//googleai/*.txt")    
    total_features = []
    
    for f in files:
        print(f)
        filename = f.replace(".txt", ".geojson")
        
        with open(filename,'w') as fp:
            fc = FeatureCollection(process_file(f))
            fp.write(fc.__str__())
    
    #print(FeatureCollection(total_features))
        