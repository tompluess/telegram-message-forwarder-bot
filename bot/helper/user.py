def username_long(user):
    sender_name_parts = []
    if user.first_name:
        sender_name_parts.append(user.first_name)
    if user.last_name:
        sender_name_parts.append(user.last_name)
    if user.username:
        sender_name_parts.append("@"+user.username)
    sender_name = " ".join(sender_name_parts)
    return sender_name
