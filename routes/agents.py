from flask import request, redirect, url_for, flash, session, render_template
from app import app, mail
from controller.agent_controllers import AgentController
from controller.user_controllers import UserController
from routes.session_utils import is_logged_in, auth_handler, is_agent, is_admin
from mysql.connector.errors import IntegrityError

# @app.route('/add_agent', methods=['GET', 'POST'])
# def add_agent():
#     if request.method == 'POST':
        # # Extract form data
        # first_name = request.form.get('name')
        # last_name = request.form.get('last_name')
        # email = request.form.get('email')
        # phone = request.form.get('phone')
        # wechat = request.form.get('wechat')
        # agency_name = request.form.get('agency_name')
#         # Add other fields as required

#         # Call controller method to add agent
#         if AgentController.add_agent(first_name, last_name, email, phone, wechat, agency_name):
#             flash('Agent added successfully.')
#             return redirect(url_for('agent_list'))  # Redirect to agent list page
#         else:
#             flash('Failed to add agent.')

#     return render_template('agents/add_agent.html')


@app.route('/add_agent', methods=['GET', 'POST'])
def add_agent():
    if not is_logged_in():
        flash('Please login as admin to view this page.')
        return redirect(url_for('login'))
    elif not is_admin():
        flash('Only admins are authorised to view this page.')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        # Extract form data
        username=request.form.get('username')
        password=request.form.get('password')
        confirm_password=request.form.get('confirm_password')
        first_name = request.form.get('name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        agency_name = request.form.get('agency_name')
    
        
        # Validate password confirmation
        if password != confirm_password:
            flash("Passwords do not match.")
            return redirect(url_for('add_agent'))
        try:
            
            user_id=UserController.add_user(username,password,"Agent")
           
            agent=AgentController.add_agent(user_id, first_name, last_name, email, phone, wechat,agency_name)
                
            if user_id and agent:
                flash("Agent added and credentials created successfully.")
                
                return redirect(url_for("agents"))
            else:
                flash("Failed to create agent details.")
        except IntegrityError as e:
            flash("Username already taken. Please choose a different username.")


    return render_template('agents/add_agent.html')



@app.route('/agent_list')
def agents():
    if not (is_agent() or is_admin()):
        return redirect(url_for('login'))
    agents=AgentController.get_all_agents()
    return render_template('agents/agents.html', agents=agents)



# @app.route('/edit_agent/<int:agent_id>', methods=['GET', 'POST'])
# def edit_agent(agent_id):
#     if not is_logged_in():
#         flash('Please login as admin to view this page.')
#         return redirect(url_for('login'))
#     elif not is_admin():
#         flash('Only admins are authorised to view this page.')
#         return redirect(url_for('dashboard'))
    
#     user_id=session.get('UserID')
#     agent_id=AgentController.get_agent_id_by_user_id(user_id)

#     if request.method == 'POST':
#         # Extract form data
#         first_name = request.form.get('name')
#         last_name = request.form.get('last_name')
#         email = request.form.get('email')
#         phone = request.form.get('phone')
#         wechat = request.form.get('wechat')
#         agency_name = request.form.get('agency_name')
#         # Add other fields as required
        
        

#         # Call controller method to update agent
#         success=AgentController.update_agent(agent_id, first_name, last_name, email, phone, wechat, agency_name)
#         if success:
#             flash('Agent updated successfully.')
#             agent=AgentController.get_agent_details(agent_id)
            
#         else:
            
#             flash('Failed to update agent.')
#             agent=AgentController.get_agent_details(agent_id)
#     else:
#         agent=AgentController.get_agent_details(agent_id)
#         if not agent:
#             flash('Agent not found.')
#             return redirect(url_for('agents'))
        
#         return render_template('agents/edit_agent.html', agent=agent)

@app.route('/edit_agent/<int:agent_id>', methods=['GET', 'POST'])
def edit_agent(agent_id):
    if not is_logged_in():
        flash('Please login as admin to view this page.')
        return redirect(url_for('login'))
    elif not is_admin():
        flash('Only admins are authorised to view this page.')
        return redirect(url_for('dashboard'))
    
    # user_id = session.get('UserID')
    # # This line might not be needed if you're already getting agent_id from the URL parameter
    # agent_id = AgentController.get_agent_id_by_user_id(user_id)
    
    if request.method == 'POST':
        # Extract form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        wechat = request.form.get('wechat')
        agency_name = request.form.get('agency_name')
        # Add other fields as required
        
        # Call controller method to update agent
        success = AgentController.update_agent(agent_id, first_name, last_name, email, phone, wechat, agency_name)
        agent = AgentController.get_agent_details(agent_id)  # Fetch updated agent details
        
        if success:
            flash('Agent updated successfully.')
        else:
            flash('Failed to update agent.')
            
        # Render the same edit page with the updated agent details or show the error message
        # return render_template('agents/edit_agent.html', agent=agent)
        return redirect(url_for('agents'))
    else:
        agent = AgentController.get_agent_details(agent_id)
        if not agent:
            flash('Agent not found.')
            return redirect(url_for('agents'))
        
        return render_template('agents/edit_agent.html', agent=agent)

            


