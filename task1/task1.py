import json

data = "file_for_json.txt"
my_file = open(data, mode='w')


my_data = {

    'last_name': "Kaiduev",
    'name': "Baktygul",
    'age': "19",

    'phone': {
        'main_phone': +996999925927,
        'second_phone': +996709202111,
    },
    'skills': {
        'education': {
            'school':"Dmitrievskaya",
            'University': {
                'University':"Kyrgyz State Technical University",
                'descriptions':'Cyber Security',
            },
            'course': 2,
        },
        'language': "Python",
        'databases': {
            1: "SQL",
            2: "MySQL",
            3: "sqlite3"},
        'other': "HTML5,CSS,Git,Django",
    }

}

all_data = []
all_data.append(my_data)
json.dump(all_data, my_file)
my_file.close()



