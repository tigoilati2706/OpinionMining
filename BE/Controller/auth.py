from flask import request, jsonify
from flask_cors import cross_origin
# from flask_bcrypt import bcrypt
import bcrypt

from init import app

from Models import Users



@app.route('/api/register', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def register():
    json_data = request.json

    dateOfBirth =json_data['dateOfBirth']
    address=json_data['address']
    userName=json_data['userName']
    password=json_data['password']
    email=json_data['email']
    gender=json_data['gender']

    try:
        status = Users.Insert_Users(dateOfBirth,address,userName,password,email,gender)
    except:
        status = 'User is already registered'
    return jsonify({'result': status})


@app.route('/api/login', methods=['POST'])
@cross_origin(allow_headers=['Content-Type'])
def login():
    if request.method == "POST":
        json_data = request.json
        
        user = Users.User_Login(json_data['email'], json_data['password'])
        
        if user is True:
            status = True
        else:
            status = False

        return jsonify({'result': 'Login Successfully !!!'})


@app.route('/api/logout')
@cross_origin(allow_headers=['Content-Type'])
def logout():
    return jsonify({'result': 'Logout Successfully !!!'})




# @app.route('/api/register', methods=['POST'])
# @cross_origin(allow_headers=['Content-Type'])
# def register():
#     json_data = request.json
    
#     dateOfBirth =json_data['dateOfBirth']
#     address=json_data['address']
#     userName=json_data['userName']
#     password=json_data['password']
#     email=json_data['email']
#     gender=json_data['gender']
#     # hashedpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
#     password = bcrypt.hashpw(password, bcrypt.gensalt())
#         if isinstance(password, str):
#             return password
#         else:
#             return password.decode("UTF-8") 

#     try:
#         status = Users.Insert_Users(dateOfBirth,address,userName,email,gender,password)
#     except Exception as e:
#         print(e)
#         status = 'User is already registered'
#     return jsonify({'result': status})


# @app.route('/api/login', methods=['POST'])
# @cross_origin(allow_headers=['Content-Type'])
# def login():
#     if request.method == "POST":
#         json_data = request.json
        
#         user = Users.User_Login(json_data['email'], json_data['password'])
        
#         if user is True:
#             status = True
#         else:
#             status = False

#         return jsonify({'result': 'Login Successfully !!!'})




















# class Auth:

#     @staticmethod
#     def login_user(data):
#         try:
#             # fetch the user data
#             user = Users.query.filter_by(email=data.get('email')).first()
#             if user and user.check_password(data.get('password')):
#                 auth_token = user.encode_auth_token(user.id)
#                 if auth_token:
#                     response_object = {
#                         'status': 'success',
#                         'message': 'Successfully logged in.',
#                         'Authorization': auth_token.decode()
#                     }
#                     return response_object, 200
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': 'email or password does not match.'
#                 }
#                 return response_object, 401

#         except Exception as e:
#             print(e)
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Try again'
#             }
#             return response_object, 500



#     @staticmethod
#     def logout_user(data):
#         if data:
#             auth_token = data.split(" ")[1]
#         else:
#             auth_token = ''
#         if auth_token:
#             resp = Users.decode_auth_token(auth_token)
#             if not isinstance(resp, str):
#                 # mark the token as blacklisted
#                 return save_token(token=auth_token)
#             else:
#                 response_object = {
#                     'status': 'fail',
#                     'message': resp
#                 }
#                 return response_object, 401
#         else:
#             response_object = {
#                 'status': 'fail',
#                 'message': 'Provide a valid auth token.'
#             }
#             return response_object, 403



# # @auth.route('/signup', methods=['POST'])
# # def signup_post():

# #     dateOfBirth = request.form.get('dateOfBirth')
# #     address = request.form.get('address')
# #     userName = request.form.get('userName')
# #     password = request.form.get('password')
# #     fullName = request.form.get('fullName')
# #     email = request.form.get('email')
# #     gender = request.form.get('gender')


# #     user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

# #     if user: # if a user is found, we want to redirect back to signup page so user can try again
# #         flash('Email address already exists')
# #         # return redirect(url_for('auth.signup'))

# #     # create a new user with the form data. Hash the password so the plaintext version isn't saved.
# #     new_user = Users(dateOfBirth=dateOfBirth,
# #                     address = address ,
# #                     userName = userName, 
# #                     fullName = fullName, 
# #                     gender = gender ,
# #                     email=email, 
# #                     password=generate_password_hash(password, method='sha256'))

# #     # add the new user to the database
# #     db.session.add(new_user)
# #     db.session.commit()

# #     # return redirect(url_for('auth.login'))

# # @auth.route('/login', methods=['POST'])
# # def login_post():
# #     email = request.form.get('email')
# #     password = request.form.get('password')
# #     remember = True if request.form.get('remember') else False

# #     user = Users.query.filter_by(email=email).first()

# #     # check if the user actually exists
# #     # take the user-supplied password, hash it, and compare it to the hashed password in the database
# #     if not user or not check_password_hash(user.password, password):
# #         flash('Please check your login details and try again.')
# #         # return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page
    
    
# #     # if the above check passes, then we know the user has the right credentials
# #     login_user(user, remember=remember)
# #     # return redirect(url_for('main.profile'))


# # @auth.route('/logout')
# # @login_required
# # def logout():
# #     logout_user()
# #     # return redirect(url_for('main.index'))