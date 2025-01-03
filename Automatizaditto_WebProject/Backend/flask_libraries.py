import bcrypt
import ipaddress
from Database.db_connection import db_connection_func
from flask import Flask, render_template, url_for, session, request, jsonify, redirect, Response, flash
from flask_session import Session
from psycopg2.extras import RealDictCursor