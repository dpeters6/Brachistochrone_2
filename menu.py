import base64
import json
import logging
import os
import pandas as pd
import requests
from flask import Flask, render_template, request
from mysql import connector

@app.route('/')
def menu():