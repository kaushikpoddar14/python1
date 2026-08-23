from flask import Flask

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My Python Web App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #0f172a;
            color: #f1f5f9;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: #1e293b;
            padding: 2rem 3rem;
            border-radius: 12px;
            text-align: center;
        }
        h1 { color: #38bdf8; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Hello, World! 👋</h1>
        <p>My first Python web app, ready for GitHub.</p>
    </div>
</body>
</html>
"""


@app.route("/")
def home():
    return HTML_PAGE


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
