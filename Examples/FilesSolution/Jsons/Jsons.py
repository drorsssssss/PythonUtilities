import json

def example():
    file_path='/Users/dsivan/GitRepos/PythonUtilities/Examples/FilesSolution/Jsons/example.json'
    output_file='/Users/dsivan/GitRepos/PythonUtilities/Examples/FilesSolution/Jsons/output.json'

    with open(file_path) as file_obj:
        file=json.load(file_obj)

    file['name']='Dror'
    for keys,values in file.items():
        print(f"{keys} -> {values}")
    print(json.dumps(file,indent=1))


    # with open(output_file,'w') as  output_file:
    #     output_file.write(json.dumps(file))

example()




