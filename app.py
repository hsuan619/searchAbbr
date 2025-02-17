from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
# 讀取CSV檔案
def read_csv():
    return pd.read_csv("wordSearch.csv")

# 寫入CSV檔案
def write_csv(data):
    df = pd.DataFrame([data])
    df.to_csv('wordSearch.csv', mode='a', header=False, index=False)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search'].strip().upper()
    df = read_csv()
    
    # 搜尋結果
    results = df[df['abbr'] == search_term]
    
    if not results.empty:
        # 將所有符合的結果轉換成列表
        results_list = []
        for _, row in results.iterrows():
            results_list.append({
                'abbr': row['abbr'],
                'fullname': row['full-name'],
                'chinese': row['chinese'],
                'note': row['note']
            })
        return render_template('result.html', results=results_list)
    else:
        return redirect(url_for('add', abbr=search_term))

@app.route('/add')
def add():
    abbr = request.args.get('abbr', '')
    return render_template('add.html', abbr=abbr)

@app.route('/add', methods=['POST'])
def add_submit():
    data = {
        'abbr': request.form['abbr'],
        'full-name': request.form['fullname'],
        'chinese': request.form['chinese'],
        'note': request.form['note']
    }
    write_csv(data)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
