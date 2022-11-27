from flask import Flask, request
import inference

app = Flask(__name__)

@app.route("/")
def home():
    str_to_return = "Please navigate to '/predictions?num=' followed by an int to get predictions <br>"
    str_to_return += "For example: <a href='/predictions?num=6'>/predictions?num=6</a>"
    return str_to_return

@app.route("/predictions", methods=["GET"])
def get_predictions():
    num = int(request.args.get("num"))
    if num > 0:
        actuals, preds, errs = inference.get_inference(num_to_predict=num)
        if len(actuals) == 0:
            str = "Oops... Can't find model! <br>"
            str += f"Err: {errs[0]}"
        else:
            str = f'Actual number(s): {actuals} <br>'
            str += f'Predicted number(s): {preds}'
    else:
        str = "Please pass a 'num' query string: /predictions?num=6 <br>"
        str += "For example: <a href='/predictions?num=6'>/predictions?num=6</a>"
    return str

if __name__ == "__main__":
    app.run(host='0.0.0.0')
