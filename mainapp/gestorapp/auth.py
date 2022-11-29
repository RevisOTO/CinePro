from gestorapp.models import User
from django.shortcuts import render,get_object_or_404,redirect
import jsonify
import bcrypt

def makeToken(password):
    token = bcrypt.hashpw(password, bcrypt.gensalt(rounds=10))
    return token

def checkToken(id,passw):
    if passw:
        user = get_object_or_404(User,pk=id)
        if bcrypt.checkpw(passw,user.password):
            return jsonify({"status":"Accesible","user":user})
        else:
            return jsonify({"status":"Inaccesible"})