from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.agent_controllers import AgentController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin

@app.route('/add_agent', methods=['GET', 'POST'])
def add_agent():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        agency_name = request.form.get('agency_name')
        # Add other fields as required

        # Call controller method to add agent
        if AgentController.add_agent(first_name, last_name, email, phone, wechat, agency_name):
            flash('Agent added successfully.')
            return redirect(url_for('agent_list'))  # Redirect to agent list page
        else:
            flash('Failed to add agent.')

    return render_template('agents/add_agent.html')
