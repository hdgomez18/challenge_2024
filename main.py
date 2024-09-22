from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def root():
    return "Hello world"

@app.route("/uploadfiles", methods=['POST'])
def create_new_file():
  file_name = 'C:\Users\Acer\Downloads\challenge_2024\files\deparments.csv'

  headers = {
    'x-api-key': **REST_API_KEY**,
    'x-api-token': **REST_API_TOKEN**,
    'accept': 'application/json'
  }

files = {'file': (file_name, open(file_name, 'rb'), 'text/csv')}
url = "http://uploadfiles"
response = requests.post(url +'/api/v2/core/workspaces/import/validate',
                        files=files, verify=False, headers=headers)
print("Created")
print(response)
print(response.text)

if __name__ == '__main__':
    app.run(debug=True)
