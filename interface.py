from flask import Flask,render_template,jsonify,request
import utils
import config
import traceback


app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')



@app.route('/predict',methods=['GET','POST'])
def prediction():
    try: 
        if request.method == "GET":

            data = request.args.get

            print("Data :::",data)
            seniorcitizen = data(('SeniorCitizen'))
            partner =  data(('Partner'))
            dependents =  data(('Dependents'))
            tenure =  data(('tenure'))
            internetservice =  data(('InternetService'))
            onlinesecurity =  data(('OnlineSecurity'))
            onlinebackup =  data(('OnlineBackup'))
            deviceprotection =  data(('DeviceProtection'))
            techsupport =  data(('TechSupport'))
            streamingTV =  data(('StreamingTV'))
            streamingmovies =  data(('StreamingMovies'))
            contract =  data(('Contract'))
            paperlessbilling =  data(('PaperlessBilling'))
            monthlycharges =  data(('MonthlyCharges'))
            totalcharges =  data(('TotalCharges'))
            paymentmethod =  data(('PaymentMethod'))


            model = utils.Model()

            result = model.result(seniorcitizen,partner,dependents,
                        tenure,internetservice,onlinesecurity,
                        onlinebackup,deviceprotection,techsupport,
                        streamingTV,streamingmovies,contract,
                        paperlessbilling,monthlycharges,
                        totalcharges,paymentmethod)
            outcome = ""
            if result == 0:
                outcome = "Customer will continue with the services"
            else:
                outcome = "Churn Detected"

            return render_template('index.html',prediction=outcome)
        else:
            data = request.form.get

            print("Data :::",data)
            seniorcitizen = data(('SeniorCitizen'))
            partner =  data(('Partner'))
            dependents =  data(('Dependents'))
            tenure =  data(('tenure'))
            internetservice =  data(('InternetService'))
            onlinesecurity =  data(('OnlineSecurity'))
            onlinebackup =  data(('OnlineBackup'))
            deviceprotection =  data(('DeviceProtection'))
            techsupport =  data(('TechSupport'))
            streamingTV =  data(('StreamingTV'))
            streamingmovies =  data(('StreamingMovies'))
            contract =  data(('Contract'))
            paperlessbilling =  data(('PaperlessBilling'))
            monthlycharges =  data(('MonthlyCharges'))
            totalcharges =  data(('TotalCharges'))
            paymentmethod =  data(('PaymentMethod'))


            model = utils.Model()

            result = model.result(seniorcitizen,partner,dependents,
                        tenure,internetservice,onlinesecurity,
                        onlinebackup,deviceprotection,techsupport,
                        streamingTV,streamingmovies,contract,
                        paperlessbilling,monthlycharges,
                        totalcharges,paymentmethod)
            outcome = ""
            if result == 0:
                outcome = "Customer will continue with the services"
            else:
                outcome = "Churn Detected"

            return render_template('index.html',prediction=outcome)
    except:
        
        print("Error occured: ",traceback.print_exc())    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT,debug=True)