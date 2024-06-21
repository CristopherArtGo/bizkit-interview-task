import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    fave_numbers_1 = set(sorted(fave_numbers_1))
    fave_numbers_2 = set(sorted(fave_numbers_2))

    if (len(fave_numbers_1) > len(fave_numbers_2)):
        longer_list = fave_numbers_1
        shorter_list = fave_numbers_2
    else:
        longer_list = fave_numbers_2
        shorter_list = fave_numbers_1

    length = len(longer_list) 
    for number in range(length):
        if number in shorter_list:
            return True

    return False