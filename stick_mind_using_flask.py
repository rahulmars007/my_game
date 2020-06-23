from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    total=21
    s="START ANY ONE PLAYER"
    return render_template("game2.html",m=s,t=total)

@app.route("/run/", methods=['POST'])
def run():
    coin=request.form["coin"]
    r=request.form["r"]
    total=int(request.form['total'])
    coin=int(coin)
    if(coin>total):
        if(r=="bt A"):
         s="ENTER NUMBER LESS THAN TOTAL STICK ||TURN A||"
         db="disabled"
         da=""
        if(r=="bt B"):
         s="ENTER NUMBER LESS THAN TOTAL STICK ||TURN B||"
         da="disabled"
         db=""
        return render_template("game2.html",t=total,m=s,da=da,db=db)
    if(1>coin or coin>4):  
        if(r=="bt A"):
          s="PLEASE ENTER NUMBER B/W 1 to 4 ||TURN A||"
          db="disabled"
          da=""
        if(r=="bt B"): 
          s="PLEASE ENTER NUMBER B/W 1 to 4 ||TURN B||"
          da="disabled"
          db=""
        return render_template("game2.html",m=s,t=total,da=da,db=db)
    
    if(r=="bt A"):
      
      if(1<=coin<=4):
        total=total-coin
        s="NOW TURN IS ||PLAYER B||"
        da="disabled"
        db=""  
        if(total==0):
           s="PLAYER A LOSS AND PLAYER B WIN"
    if(r=="bt B"):
      
      if(1<=coin<=4):
        total=total-coin
        s="NOW TURN IS ||PLAYER A||"
        db="disabled"
        da=""
        if(total==0):
           s="PLAYER B LOSS AND PLAYER A WIN"
         
         
    return render_template("game2.html",t=total,m=s,da=da,db=db)
        
                 
if __name__ =="__main__":
       app.run(host="localhost",port=int("777"))
          
       
       