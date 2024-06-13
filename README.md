# QuadDB API Wrapper

Python wrapper for the Quadrium-DB API.

# Installation - Easy Way
### Install the Package:
Use pip to install the package. This command tells pip to install the package defined by the setup.py file in the current directory.
```
pip install git+https://github.com/CyberDefenseEd/quaddb.py
```
# Installation - Manual
### Clone or Download the Repository:
You can clone the repository or download the package and extract it to your desired location.
```bash
https://github.com/CyberDefenseEd/quaddb.py
```
### Navigate to the Package Directory:
Change to the directory containing the setup.py file.
```
cd quaddb.py
```
### Install the Package:
Use pip to install the package. This command tells pip to install the package defined by the setup.py file in the current directory.
```
pip install git+https://github.com/CyberDefenseEd/quaddb.py
```
## Usage
```py
from quaddb import QuadDBClient

client = QuadDBClient(base_url="http://localhost:9010")

# Get documents
documents = client.get_documents(db="mydb")
print(documents)

# Create documents
new_docs = [
    {"data": {"field1": "value1"}},
    {"id": "custom-id", "data": {"field2": "value2"}}
]
response = client.create_documents(db="mydb", documents=new_docs)
print(response)

# Search documents
search_results = client.search_documents(db="mydb", field="field1", value="value1")
print(search_results)

# Get a single document
document = client.get_document(db="mydb", key="custom-id")
print(document)

# Update a document
update_data = {"field1": "new_value"}
update_response = client.update_document(db="mydb", key="custom-id", data=update_data)
print(update_response)

# Delete a document
delete_response = client.delete_document(db="mydb", key="custom-id")
print(delete_response)

# Get updates
updates = client.get_updates()
print(updates)

# Get collections
collections = client.get_collections()
print(collections)
```
