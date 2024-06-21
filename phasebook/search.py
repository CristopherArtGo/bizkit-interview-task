from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    if not args:
        return USERS
    
    id_match = []
    name_match = []
    age_match = []
    occupation_match = []
    

    for user in USERS:
        max_age = None
        min_age = None

        if "age" in args:
            max_age = int(args["age"]) + 1
            min_age = int(args["age"]) - 1
        
        if "id" in args:
            if len(id_match) == 0:
                if int(user["id"]) == int(args["id"]):
                    id_match.append(user)
                    continue

        if "name" in args:
            if args["name"].lower() in user["name"].lower():
                name_match.append(user)

        if "age" in args:
            if (int(user["age"]) >= min_age and int(user["age"]) <= max_age):
                age_match.append(user)

        if "occupation" in args:
            if args["occupation"] in user["occupation"]:
                occupation_match.append(user)

    all_matches = id_match + name_match + age_match + occupation_match
    result = []

    # clean duplicates 
    for item in all_matches:
        if item not in result:
            result.append(item)

    return result