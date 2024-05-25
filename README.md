# Service Upload Api

This project combines a Next.js front-end with a Flask back-end. The Flask back-end provides an API endpoint for uploading and processing Excel files, while the Next.js front-end can interact with this API.

# Features

- Upload and process Excel files via a RESTful API.
- Handle missing date/time values in Excel files.
- Convert Excel data to JSON format for easy - consumption by front-end applications.
- Full CORS support to allow cross-origin requests from any domain.

# Technologies Used

## Front-end

- [Next.js](https://nextjs.org/)
- [React](https://reactjs.org/)
## Back-end

- [Flask](https://flask.palletsprojects.com/en/latest/)
- [pandas](https://pandas.pydata.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)

# Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Node.js
- npm (Node Package Manager)

## Instalation

**1. Clone the repository:**

```bash

git clone <repository_url>
cd my-nextjs-flask-app

```
**2. Set up the Flask back-end:**
```bash

cd backend
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```
**3. Set up the Next.js front-end:**

```bash

cd ../frontend
npm install
```

## Running the Application

**1. Start the Flask back-end:**
```bash

cd backend
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
flask run

```
**2. Start the Next.js front-end:**

```bash

cd ../frontend
npm run dev

```

The application should now be running. Open http://localhost:3000 in your browser to see the front-end, and the Flask API will be available at http://localhost:5000.

# API Endpoint

### Upload Excel File

- URL: `/upload-excel`
- Method: `POST`
- Content-Type: `multipart/form-data`
- Parameters: `file` - The Excel file to be uploaded.
- Response:
    - `200 OK` on success with the JSON representation of the Excel data.
    - `400 Bad Request` if no file is provided.
    - `500 Internal Server Error` on server error.

### Example Request

```bash

curl -X POST http://localhost:5000/upload-excel \
  -F 'file=@path_to_your_file.xlsx'

```
### Example Response

```bash

{
  "data": [
    {
      "column1": "value1",
      "column2": "value2",
      ...
    },
    ...
  ]
}

```

## Project Structure

```bash

ServiceUploadApi/
│
├── api/
│   └── app.py                # Main Flask application
│
├── .eslintrc.json
├── jsconfig.json
├── LICENSE
├── next.config.js        # Next.js configuration
├── package.json          # Node.js dependencies
├── README.md                 # This file
├── requirements.txt      # Python dependencies
├── vercel.json
│
└── ...

```

# Dependencies

### Python (backend)

- Flask==3.0.3
- pandas==1.3.4
- Flask-Cors==4.0.0

### Node.js (frontend)

- next==14.2.3
- react==18
- react-dom==18
- eslint==8
- eslint-config-next==14.2.3

### License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- Flask and its extensions for providing a simple yet powerful web framework.
- pandas for its powerful data manipulation capabilities.
- Next.js for its seamless integration of React with server-side rendering and static site generation.
