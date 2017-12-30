from crud import csv
from utility import login_required
from config import current_user, iran_delta, csvs
from flask import render_template, jsonify
from crud.csv.uart import thread
import datetime
from tinydb import Query


@csv.route('/track')
@login_required
def track():
    thread.is_alive = True
    return '{} we are observing you'.format(current_user['name'])


@csv.route('/utrack')
@login_required
def utrack():
    thread.is_alive = False
    return '{} we are stopped observing you'.format(current_user['name'])


@csv.route('/now-<int:flashback>', methods=['GET', 'POST'])
@csv.route('/now', methods=['GET', 'POST'])
@login_required
def now(flashback=1, jump=1):
    future = datetime.datetime.utcnow() + iran_delta + datetime.timedelta(seconds=1)
    future = str(future)
    flashback = datetime.datetime.utcnow() + iran_delta - datetime.timedelta(seconds=flashback)
    flashback = str(flashback)
    CSV = Query()
    segment = csvs.search((flashback <= CSV.date) & (CSV.user_id == current_user['_id']))
    return jsonify(segment)


@csv.route('/segment[<head>:<tail>:<int:jump>]')  # tail = inf
@csv.route('/segment[<head>:<tail>]')
@csv.route('/segment[<head>::<int:jump>]')  # tail = inf
@csv.route('/segment[<head>:]')
@csv.route('/segment[:<tail>:<int:jump>]')  # tail = inf
@csv.route('/segment[:<tail>]')
@csv.route('/segment[::<int:jump>]')  # tail = inf
@csv.route('/segment[:]')
@login_required
def segment(head=0, tail=-0, jump=1):
    return

