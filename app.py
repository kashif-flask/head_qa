from flask import Flask, render_template, request

from transformers import pipeline

app = Flask(__name__)

@app.route('/')
def index():
    topics = ["biology", "nursery", "psychology", "chemistry", "pharmacology"]
    return render_template('index.html', topics=topics)

@app.route('/generate', methods=['POST'])
def generate_qa():
    selected_topic = request.form['topic']
    top_p = float(request.form['top_p'])
    top_k = int(request.form['top_k'])
    prompt = f"{selected_topic.capitalize()}:"
    pipe = pipeline("text-generation", model="kashif09/gpt_head_qa",
                    device=-1,
                    max_length=180,
                    do_sample=True,
                    top_p=top_p,
                    top_k=top_k,
                    num_return_sequences=1)
    result = pipe(prompt)
    try:
        question = result[0]["generated_text"].split("Correct")[0].strip().replace('\n', '<br>')
        print(question)
        correct_answer = result[0]["generated_text"].split("Correct")[1].split("\n")[0].strip().replace('\n', '<br>')
        print(correct_answer)
        return render_template('qa.html', question=question, correct_answer=correct_answer)
    except:
        error_message = "Oops! Unable to generate QA for this topic. Please try again."
        return render_template('qa.html', question=error_message, correct_answer="", error=True)
    

if __name__ == '__main__':
    app.run(debug=True,port=3000)
