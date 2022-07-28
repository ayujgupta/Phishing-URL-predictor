import uvicorn # ASGI Server implementation
from fastapi import FastAPI #ultra fast web framework for building api
import joblib


app = FastAPI()

#pkl
phish_model = open('phishing.pkl','rb')
phish_model_ls = joblib.load(phish_model)

# ML Aspect
@app.get("/predict/{feature}")
async def predict(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return (features, result)
if __name__ == '__main__':
	uvicorn.run(app='prediction_app',host="127.0.0.1",port=8000,reload=True, debug=True)