from flask import Flask
from flask import render_template #import render_template
 
app = Flask(__name__)
 
#newsapi = NewsApiClient(api_key=yourAPIKEY)
  
#print(top_headlines['articles'])
 
#head_lines=[]
 
#for news in top_headlines['articles']:
 #   head_lines.append(news['title'])
 
 
@app.route('/')
def home():
    #news =head_lines
    return render_template('index.html',news='')
    return "<h1>TRABALHO DE CLOUD 44BDT</h1><h3>AWS CODE PIPELINE - ELASTIC BEANSTALK</h3><p>Esta aplicacao lista os Trending Topics do Twitter cada reload da pagina</p>"+ '\n'
 
     
@app.route('/results/',methods=['POST']) 
def get_results():
    keyword = request.form['keyword']  #getting input from user
 
    news = newsapi.get_top_headlines(q=keyword,
                                     #sources='bbc-news,the-verge',#optional and you can change
                                     #category='business', #optional and you can change also
                                     language='en', #optional and you can change also
                                     country='in')
    #print(news['articles'])
    #return render_template('index.html',news=news['articles'])
    return news
 
 
if __name__ == "__main__":
    app.run(debug=True)   
