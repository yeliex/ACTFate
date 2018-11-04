import json
import codecs
def json_loads_comment(json_file):
	res = ""
	with codecs.open(json_file,"r","utf-8-sig") as f:
		for l in f:
			if(l.strip().find('//')!=0):
				res += l
	return json.loads(res)

def DFA2ACT(DFA_data):
	languages = {
				"en": "English",
				"ko": "한국어",
				"ja": "日本語",
				"fr": "Français",
				"zh": "中文"
				}
	instances = {}
	areas = {}
	fates = {}
	roulettes = {}
	for lang in languages.keys():
		for (id_, info_) in DFA_data[lang]["instances"].items():
			if(id_ not in instances.keys()):
				instances[id_] = {
					"name":{lang_:"null" for lang_ in languages.keys()},
					"t":"0",
					"h":"0",
					"d":"0",
				}
			instances[id_]["name"][lang] = info_["name"]
			instances[id_]["t"] = info_["tank"]
			instances[id_]["h"] = info_["healer"]
			instances[id_]["d"] = info_["dps"]

		for (id_, info_) in DFA_data[lang]["areas"].items():
			if(id_ not in areas.keys()):
				areas[id_] = {lang_:"null" for lang_ in languages.keys()}
			areas[id_][lang] = info_["name"]
			for (fate_id, fate_name) in info_["fates"].items():
				if(fate_id not in fates.keys()):
					fates[fate_id] = {
										"name":{lang_:"null" for lang_ in languages.keys()},
										"area_code":{lang_:"null" for lang_ in languages.keys()},
									}
				fates[fate_id]["name"][lang] = fate_name
				fates[fate_id]["area_code"][lang] = id_

		for (id_, info_) in DFA_data[lang]["roulettes"].items():
			if(id_ not in roulettes.keys()):
				roulettes[id_] = {lang_:"null" for lang_ in languages.keys()}
			roulettes[id_][lang] = info_
	data = {
		"languages":languages,
		"instances":instances,
		"areas":areas,
		"fates":fates,
		"roulettes":roulettes,
	}
	return data





if __name__=="__main__":
	DFA_data = {}
	DFA_data["zh"] = json_loads_comment("zh-cn.json")
	DFA_data["en"] = json_loads_comment("en-us.json")
	DFA_data["ko"] = json_loads_comment("ko-kr.json")
	DFA_data["ja"] = json_loads_comment("ja-jp.json")
	DFA_data["fr"] = json_loads_comment("fr-fr.json")
	ACTFATE_data = DFA2ACT(DFA_data)
	with codecs.open("data_output.json","w","utf8") as f:
		f.write(json.dumps(ACTFATE_data))
