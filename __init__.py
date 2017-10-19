from flask import Flask, request, Response
from twilio.rest import Client

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC190046e06b0612f0f1be5beab91f7030"
auth_token  = "{a0e68c354c1a4d54021a99800a031040}"
workspace_sid = "{WS7049aaac0bb91a16bda876a28d16a4a7}"
workflow_sid = "{WW25179b77ce4678c8d7a30f2c35a35f15}"

client = Client(username=account_sid, password=auth_token)

@app.route("/assignment_callback", methods=['GET', 'POST'])
def assignment_callback():
    """Respond to assignment callbacks with empty 200 response"""

    resp = Response({}, status=200, mimetype='application/json')
    return resp

@app.route("/create_task", methods=['GET', 'POST'])
def create_task():
    """Creating a Task"""
    task = client.taskrouter.workspaces(sid=workspace_sid)\
                 .tasks.create(workflow_sid=workflow_sid,
                               attributes='{"selected_language":"es"}')

    print(task.attributes)
    resp = Response({}, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run()

