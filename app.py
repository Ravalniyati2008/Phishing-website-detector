from flask import Flask, render_template, request

app = Flask(__name__)

def detect_phishing(url):
    score = 0

    # Basic phishing checks
    if '@' in url:
        score += 1

    if len(url) > 75:
        score += 1

    if url.count('-') > 2:
        score += 1

    if not url.startswith("https://"):
        score += 1

    if score >= 2:
        return "⚠️ Phishing Website Detected"
    else:
        return "✅ Legitimate Website"

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""

    if request.method == 'POST':
        url = request.form['url']
        result = detect_phishing(url)

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)