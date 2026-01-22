# user_profile.py example from book

def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
# my details
user_profile = build_profile('bidemi', 'muibudeen',
                             location='california', field='education and finance')
print(user_profile)