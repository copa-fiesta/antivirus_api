from flask import Flask, request, jsonify

app = Flask(__name__)


# Define the File model
class File:
    def __init__(self, name, content):
        self.name = name
        self.content = content


# Sample data for scan history and quarantined files
scan_history = [{"fileId": "123", "status": "clean"}, {"fileId": "456", "status": "infected"}]
quarantined_files = [{"fileId": "789", "name": "quarantined_file.txt"}]


@app.route('/scans/scan', methods=['POST'])
def scan_file():
    data = request.get_json()
    file = File(data['name'], data['content'])

    # Perform virus scan logic here
    if 'virus' in file.content.lower():
        return jsonify({"status": "infected", "details": "Virus found"}), 404
    else:
        return jsonify({"status": "clean"})


@app.route('/scans/update', methods=['PUT'])
def update_definitions():
    return jsonify({"message": "Definitions updated successfully"})


@app.route('/scans/history', methods=['GET'])
def get_scan_history():
    return jsonify(scan_history)


@app.route('/quarantine/quarantine', methods=['GET'])
def get_quarantined_files():
    return jsonify(quarantined_files)


@app.route('/quarantine/delete', methods=['DELETE'])
def delete_from_quarantine():
    # Perform deletion logic here
    return jsonify({"message": "File deleted from quarantine"})


if __name__ == '__main__':
    app.run(debug=True)