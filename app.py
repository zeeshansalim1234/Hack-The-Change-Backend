from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)

key = "AIzaSyB9f1GCOB0WSYtPzqceTq8Q_OwCp5tA2oc"

#comment

@app.route('/', methods = ['GET'])
def input():
    url = "https://www.google.com/maps/embed/v1/search?key="+key+"&q=recycle+depot+in+calgary"
    return render_template('index.html', url= url)

@app.route('/test', methods = ['GET'])
def test():
    #url = "https://www.google.com/maps/embed/v1/search?key=key&q=recycle+depot+in+calgary"
    return jsonify(key)

@app.route('/getSample', methods = ['GET'])
def sample():

    test = {"name": "Zeeshan"}
    return jsonify(test)

@app.route('/isRecyclable', methods = ['GET'])
def isRecyclable():
    
    barcode = request.args.get('barcode')
    val = calculateRebateOnAnItem(barcode)
    return jsonify({'result':val})

@app.route('/checkFoodData', methods = ['GET'])
def checkFoodData():
    return jsonify({'result':'YO'})


def calculateRebateOnAnItem(barcode):
    pass
    # loc = 'Products.csv'
    # df = pd.read_csv(loc)

    # cols = ['Brand','Alcoholic?','Container code','Size (ml)','UPC']

    # df.pop('Alcoholic?')
    # df.pop('Flavour')
    # df.pop('Container Code')

    # # Addition of rebate values

    # # Add Rebate Val as Column to the dataframe 
    # thresHold = 1000

    # lowVal_AL = 0.9
    # highVal_AL = 0.25-0.09

    # lowVal_PET = 0.10-0.03
    # highVal_PET = 0.25-0.07

    # lowVal_Plastic = lowVal_PET
    # highVal_Plastic = highVal_PET

    # lowVal_Gl = 0.10-0.08
    # highVal_Gl = 0.25-0.08

    # lowVal_Met = 0.10-0.09
    # highVal_Met = 0.25-0.09

    # lowVal_Pouche = 0.10-0.04
    # highVal_Pouche = 0.25-0.04

    # # Looping through the dataframe 

    # rebateList = []

    # MaterialList = ['Glass','Aluminum','Bag In a Box','PET', 'Non-refillable',
    #                 'Plastic - One-Way Keg','Tetra Brik','Drink-Pouch']

    # idx = 0
    # for i in range(0,len(df)):
    #     if (df['Size (ml)'][i] <thresHold):
    #         if(df['Material'][i] == MaterialList[0]):
    #             rebateList.append(lowVal_Gl)
    #         elif df['Material'][i] == MaterialList[1]:
    #             rebateList.append(lowVal_AL)
    #         elif df['Material'][i] == MaterialList[2]:
    #             rebateList.append(lowVal_Pouche)
    #         elif df['Material'][i] == MaterialList[3]:
    #             rebateList.append(lowVal_PET)
    #         elif df['Material'][i] == MaterialList[4]:
    #             rebateList.append(lowVal_PET)
    #         elif df['Material'][i] == MaterialList[5]:
    #             rebateList.append(lowVal_Plastic)
    #         elif df['Material'][i] == MaterialList[6]:
    #             rebateList.append(lowVal_PET)
    #         else:
    #             rebateList.append(lowVal_Pouche)
    #     else:
    #         if df['Material'][i] == MaterialList[2]:
    #             rebateList.append(highVal_Pouche)
    #         elif df['Material'][i] == MaterialList[3]:
    #             rebateList.append(highVal_PET)
    #         elif df['Material'][i] == MaterialList[4]:
    #             rebateList.append(highVal_PET)
    #         elif df['Material'][i] == MaterialList[5]:
    #             rebateList.append(highVal_Plastic)
    #         elif df['Material'][i] == MaterialList[6]:
    #             rebateList.append(highVal_PET)
    #         else :
    #             rebateList.append(highVal_Pouche)


    # df['RebateValue'] = rebateList
    # df = df[df['UPC'].notna()]
    # UPC = barcode

    # UPC.strip()
    # UPC.replace(" ","")

    # if df['UPC'].str.contains(UPC).any():
    #     idx = df.index.values[df['UPC'].str.contains(UPC)]
    #     index = idx[0]
    #     rebateVal = df['RebateValue'][index]
    #     result = round(rebateVal, 3)
    #     try:
    #         all_users = [doc.to_dict() for doc in user_Ref.stream()]
    #         for user in all_users:
    #             if 'Name' in user and user['Name']=="Sarthak":
    #                 user_Ref.document(str(8972342342)).update({"Rebate": firestore.Increment(float(result))})
    #     except Exception as e:
    #         return f"An Error Occured: {e}"
    #     return True

    # else:
    #     return False



if __name__ == "__main__":
    app.run(debug=True)
    