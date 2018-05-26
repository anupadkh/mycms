import urllib.request, json
# with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:




class myjson(object):
    district = ""
    muns =""
    id=""
    def __init__(self, district, muns, localid):
        self.district = district
        self.muns = muns
        self.id = localid

class finaljson(object):
    json_array =[]
    parent_field_id = 0
    child_field_id = 0
    child_option_value = ''
    child_option_text = ''
    parent_option_value = ''
    parent_option_text = ''

a =[]

district = {
0:"नखुलेको",
1:"ताप्लेजुङ",
10:"सुनसरी",
11:"सोलुखुम्बु",
12:"खोटाङ",
13:"ओखलढुङ्गा",
14:"उदयपुर",
15:"सप्तरी",
16:"सिराहा",
17:"दोलखा",
18:"रामेछाप",
19:"सिन्धुली",
2:"पाँचथर",
20:"धनुषा",
21:"महोत्तरी",
22:"सर्लाही",
23:"रसुवा",
24:"धादिङ",
25:"नुवाकोट",
26:"काठमाण्डौ",
27:"भक्तपुर",
28:"ललितपुर",
29:"काभ्रेपलान्चोक",
3:"ईलाम",
30:"सिन्धुपाल्चोक",
31:"मकवानपुर",
32:"रौतहट",
33:"बारा",
34:"पर्सा",
35:"चितवन",
36:"गोरखा",
37:"मनाङ्ग",
38:"लम्जुङ्ग",
39:"कास्की",
4:"झापा",
40:"तनहुँ",
41:"स्याङ्जा",
42:"गुल्मी",
43:"पाल्पा",
44:"अर्घाखाँची",
45:"नवलपरासी",
46:"रुपन्देही",
47:"कपिलवस्तु",
48:"मुस्ताङ्ग",
49:"म्याग्दी",
5:"स‌खुवासभा",
50:"बाग्लुङ",
51:"पर्वत",
52:"रुकुम",
53:"रोल्पा",
54:"प्युठान",
55:"सल्यान",
56:"दाङ",
57:"डोल्पा",
58:"मुगु",
59:"जुम्ला",
6:"तेह्रथुम",
60:"कालिकोट",
61:"हुम्ला",
62:"जाजरकोट",
63:"दैलेख",
64:"सुर्खेत",
65:"बाँके",
66:"बर्दिया",
67:"बाजुरा",
68:"अछाम",
69:"बझाङ्ग",
7:"भोजपुर",
70:"डोटी",
71:"कैलाली",
72:"दार्चुला",
73:"बैतडी",
74:"डडेलधुरा",
75:"कन्चनपुर",
76:"नवलपरासी (बर्दघाट सुस्ता पूर्व)",
77:"रुकुम (पूर्व भाग)",
8:"धनकुटा",
9:"मोरङ",
}


for i in range(0,77):
    with urllib.request.urlopen("http://103.69.124.222:804/Common/FillVDCMun?isPopup=false&districtDefCd="+str(i)) as url:
        temp = json.loads(url.read().decode())
        a.append(myjson(i,temp, district[i]))



for j in a:
    print ("District No: ")
    print (j.id)
    print ("Municipalities:")
    print (j.muns)

postjson = finaljson()
postjson.json_array = a
postjson.child_option_text = 'Text'
postjson.child_option_value = 'Value'
postjson.child_field_id = 40
postjson.parent_option_value = 'id'
postjson.parent_option_text = 'district'
postjson.parent_field_id = 36

print(json.dumps(postjson, default=lambda o: o.__dict__))
