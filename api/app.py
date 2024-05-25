from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS
import traceback

app = Flask(__name__)
CORS(app, origins='*')

@app.route('/upload-excel', methods=['POST'])
def upload_excel():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    try:
        df = pd.read_excel(file)
        
        # Extrair e processar apenas a coluna AnotaÃ§Ãµes de resoluÃ§Ã£o
        resolution_notes = df['AnotaÃ§Ãµes de resoluÃ§Ã£o'].fillna('')  # Substituir NaN por string vazia
        other_data = df.drop('AnotaÃ§Ãµes de resoluÃ§Ã£o', axis=1)  # Preservar os outros dados
        
        # Tratar todos os possÃ­veis valores NaN do DataFrame
        other_data = other_data.applymap(lambda x: '' if pd.isna(x) else x)
        
        # Convertendo os dados relevantes para um formato JSON serializÃ¡vel
        data = {
            'resolution_notes': resolution_notes.tolist(),
            'other_data': other_data.to_dict(orient='records')
        }
        return jsonify(data), 200
    except Exception as e:
        traceback.print_exc()  # Imprime a stack trace para o console
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)
