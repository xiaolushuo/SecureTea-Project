# -*- coding: utf-8 -*-
u"""Arguments module for SecureTea.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴

    Author: Rejah Rehim <rejah@appfabs.com> , Aug 31 2018
    Version: 1.1
    Module: SecureTea

"""
import argparse


def get_args():
    """Docstring.

    Returns:
        Args: total arguments
    """
    parser = argparse.ArgumentParser(description='Arguments of SecureTea')

    parser.add_argument(
        '--conf',
        type=str,
        required=False,
        help='Path of configuration file. default:- "~/.securetea/securetea.conf" '
    )

    parser.add_argument(
        '--debug',
        default=False,
        action="store_true",
        help='Degug true or false'
    )

    parser.add_argument(
        '--twitter_api_key',
        '-tak',
        type=str,
        required=False,
        help='Twitter api key'
    )

    parser.add_argument(
        '--twitter_api_secret_key',
        '-tas',
        type=str,
        required=False,
        help='Twitter api secret'
    )

    parser.add_argument(
        '--twitter_access_token',
        '-tat',
        type=str,
        required=False,
        help='Twitter access token'
    )

    parser.add_argument(
        '--twitter_access_token_secret',
        '-tats',
        type=str,
        required=False,
        help='Twitter access token secret'
    )

    args = parser.parse_args()
    return args
