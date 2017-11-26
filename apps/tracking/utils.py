def get_current_user_filter(user):
    if user.is_authenticated():
        return {'user_id': user.id}

    return {}
