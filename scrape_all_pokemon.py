import json

import requests
from bs4 import BeautifulSoup
from lxml import etree, html


formats = ["uber"] #, "ou", "uubl", "uu", "rubl", "ru", "publ", "pu", "nu", "zu"]



if __name__ == '__main__':
    r = requests.get(f"https://www.smogon.com/dex/sv/formats/uber/")
    tree = html.fromstring(r.content.decode(r.encoding))
    #root = tree.xpath("//div[@class='PokemonAltRow']")[0]
    root = tree.xpath("/html/head/script[@type='text/javascript']")

    almost_json = etree.tostring(root[1]).decode()
    first_bracket = almost_json.find("{")
    last_index = almost_json.find("</script")
    almost_json = almost_json[first_bracket:last_index]
    poke_json = json.loads(almost_json)
    print(json.dumps(poke_json, indent=4))
    with open("pokejson.json", "w") as f:
        json.dump(poke_json, f, indent=4)

