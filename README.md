# head_qa
this app allow you to choose topics from different fields of science like "biology", "nursery", "psychology", "chemistry" and "pharmacology".Then you can get multiple chocie QA text generated, with correct answer. I have fine-tuned a gpt3 type model on head_qa dataset for this, i have taken the head_qa dataset and preprocessed in such a way that each question will have multiple possible answer and aslo the correct option mentioned. The code for fine-tuning the model is in notebooks/head_qa_notebook.ipynb, you can fine-tune your own model by using a different huggingface model.

## How to run the app

1. git clone https://github.com/kashif-flask/head_qa.git
2. Install all dependencies given in requirements.txt file in cmd using  pip install -r requirements.txt
3. run the file app.py in cmd , you will get local host http://127.0.0.1:5000/ 
4. Now open the url in web browser.
5. You can also create docker image by writing command in cmd:"docker build -t head_qa . " and then just run the image cmd:docker run -p 5000:3000 head_qa, now you can run the app on localhost:5000
6. Then you will see the home page
7. If you want to run just the app and don't need code, then pull image from my docker hub , write in cmd: docker pull kashif09/head_qa:latest and then just run as in step 5 but instead head_qa write kashif09/head_qa:latest

## How to use app
1. Once you see the home page
   ![alt text](https://github.com/kashif-flask/head_qa/blob/main/front.PNG)

2. Now choose here the topic about which you want the text generated, then choose parameters like top_p and top_k:
   
   * top_p (Nucleus Sampling): This parameter influences the diversity of the generated text. A higher top_p value (closer to 1) leads to more varied and creative 
   responses. If you want the generated text to be more diverse, you can increase the top_p value.

   * top_k (Top-K Sampling): This parameter controls the focus of the generated text. A higher top_k value limits the output to a smaller set of more probable tokens, 
   resulting in a more focused and deterministic response. If you want the generated text to be more focused and coherent, you can decrease the top_k value.

4. Then click on 'Generate QA' button to get the generate text:
   ![alt text](https://github.com/kashif-flask/head_qa/blob/main/generated.PNG)

4.Click on 'Show Correct Answer' to see the correct option

## Problems
some time the model returns empty text , so i have tried to solve this by displaying to user "Oops! Unable to generate QA for this topic. Please try again." text instead on generation page. Also model can be improved more, some times its hallucinates, if had bigger GPU i would have fine tuned it with better models and longer time to get better results.
When you first run the app, it will take time when you click 'Generate QA' bcoz it will be downloading all the models and tokenizers used in the model, but once it start running you can generate text in 20 to 30 seconds, problably i should make changes to overcome this first run problem.










