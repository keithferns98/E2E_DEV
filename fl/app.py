from flask import Flask,request,jsonify,render_template

app=Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/math',methods=["POST"])
def math_operations():
    if(request.method=='POST'):
        operation=request.form['operation']
        num1=int(request.form['num1'])
        num2=int(request.form['num2'])
        if(operation=='add'):
            r=num1+num2
            result='the sum of ' + str(num1) + ' and ' + str(num2) +' is ' + str(r)
        if(operation=='sub'):
            r=num1-num2
            result='the sum of '+ str(num1) + 'and ' +str(num2) + ' is ' + str(r)
        if (operation == 'mul'):
            r = num1 * num2
            result = 'the sum of ' + str(num1) + ' and ' + str(num2) + ' is ' + str(r)
        if (operation == 'divide'):
            r = num1 /num2
            result = 'the sum of ' + str(num1) + 'and ' + str(num2) + ' is ' + str(r)
        return render_template('result.html',result=result)

@app.route("/via_postman",methods=['Post'])
def math_ops():
    if (request.method=='POST'):
        operation=request.json['operation']
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        if(operation=='add'):
            r=num1+num2
            result='the sum of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if(operation=='sub'):
            r=num1-num2
            result='the sub of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if (operation=='mul'):
            r=num1+num2
            result='the mul of ' + str(num1) + ' and ' + str(num2) + 'is' + str(r)
        if(operation=='divide'):
            r=num1/num2
            result='the division of ' + str(num1) + ' and ' + str(num2) + 'is' +str(r)
    return  jsonify(result)






if __name__=='__main__':
    print('The app is working')
    app.run(debug=True)