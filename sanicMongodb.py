from sanic import Sanic
from sanic.response import json
from sanic.response import text
from sanic_session import Session
import databseOperation as dop

app = Sanic("hello_example")
Session(app)

@app.route("/")
async def test(request):
  return json({"hello": "world"})
  
  
@app.route("/printsingle/<name>")
async def test(request,name):
  return json(dop.get_single_data(name))

@app.route("/insert/<data>")
async def test(request,data):
	split=data.split(',')
	if not request.ctx.session.get('id'):
		request.ctx.session['id'] = 0
	request.ctx.session['id'] += 1
	dop.insert_data({'_id':request.ctx.session['id'],"Name":split[0],"Regno":split[1]})
	return text("Inserted Successfully......")


@app.route("/printmultiple")
async def test(request):
  return json(dop.get_multiple_data())
  
@app.route("/deletebyname/<name>")
async def test(request,name):
  return json(dop.remove_data(name))
  
@app.route("/updateregnobyname/<data>")
async def test(request,data):
	split=data.split(',')	
	return json(dop.update_or_create(split[0], split[1]))

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8000,debug = True,workers=4)
