#!/usr/bin/env python
# encoding: utf-8

"""
@author: anly_jun
@file: github
@time: 16/10/17 下午2:24
"""
from flask import Blueprint, jsonify, request
from api import github_trending

github_view = Blueprint('github', __name__)


@github_view.route("/")
def index():
    return "Hello Github"


@github_view.route("/trending")
@github_view.route("/trending/<lang>")
def trending(lang=None):

    since = request.args.get('since', None)

    opts = {
        'language': lang,
        'since': since,
    }

    return jsonify(github_trending.get_trending_repos(opts))


@github_view.route("/trending/developers")
@github_view.route("/trending/developers/<lang>")
def trending_developers(lang=None):

    since = request.args.get('since', None)

    opts = {
        'language': lang,
        'since': since,
    }

    return jsonify(github_trending.get_trending_developers(opts))
