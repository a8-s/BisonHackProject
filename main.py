from __future__ import print_function
from flask import Flask, render_template, request, jsonify, send_from_directory
import clicksend_client
from clicksend_client import SmsMessage
from clicksend_client.rest import ApiException





app = Flask(__name__)

def textSender():

    configuration = clicksend_client.Configuration()
    configuration.username = ''
    configuration.password = ''


    # create an instance of the API class
    api_instance = clicksend_client.SMSApi(clicksend_client.ApiClient(configuration))

    # If you want to explictly set from, add the key _from to the message.
    sms_message = SmsMessage(source="sdk",
                        body="Delivery Driver needed for Cake's Bakery. Contact at 214-557-4834",
                        to=""
                       )

    sms_messages = clicksend_client.SmsMessageCollection(messages=[sms_message])

    try:
        # Send sms message(s)
        api_response = api_instance.sms_send_post(sms_messages)
        print(api_response)
        return(jsonify(api_response))
    except ApiException as e:
        print("Exception when calling SMSApi->sms_send_post: %s\n" % e)
        return("error")
        
                

#def textHandler():
   # return 5

#def checkPOS():

@app.route("/")
def home():
    #return "Hello, World!"
    return render_template('home.html')

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)
    
@app.route("/send-help", methods=['POST','GET'])
def text():
    print(request)
    return textSender()

    



if __name__ == "__main__":
    app.run(debug=True)