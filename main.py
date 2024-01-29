import os
import threading

import requests


def get_cookie_variables_from_file():
    cookie_file = os.path.join(os.path.dirname(__file__), 'cookie.txt')
    if os.path.exists(cookie_file) and os.stat(cookie_file).st_size != 0:
        with open(cookie_file, 'r') as file:
            cookie_variables = {'sessionid': file.readline().strip()}
        return cookie_variables
    else:
        print("File cookie.txt kosong!")
        sessionid = input("Masukkan sessionid secara manual: ")
        return {'sessionid': sessionid}


def fetch_data(url, headers, cookie_variables, query_params, response_json_list):
    while True:
        response = requests.get(url, headers=headers, cookies=cookie_variables, params=query_params)
        if response.status_code == 200:
            response_json = response.json()
            response_json_list.append(response_json)
            next_max_id = response_json.get('next_max_id')
            if not next_max_id:
                break
            query_params['max_id'] = next_max_id
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break


headers = {
    "method": "GET",
    "x-ig-app-id": "936619743392459"
}
query_params = {
    "max_id": "",
    "search_surface": "follow_list_page"
}

userId = "34163661741"
followers_url = f"https://www.instagram.com/api/v1/friendships/{userId}/followers/"
following_url = f"https://www.instagram.com/api/v1/friendships/{userId}/following/"
cookie_variables = get_cookie_variables_from_file()

followers_response_json_list = []
following_response_json_list = []

threads = []
for url, response_json_list in [(followers_url, followers_response_json_list),
                                (following_url, following_response_json_list)]:
    thread = threading.Thread(target=fetch_data,
                              args=(url, headers, cookie_variables, query_params, response_json_list))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

followers = {user['username'] for response_json in followers_response_json_list for user in
             response_json.get('users', [])}
following = {user['username'] for response_json in following_response_json_list for user in
             response_json.get('users', [])}

print(f"Total followers: {len(followers)}")
print(f"Total following: {len(following)}")

for username in following - followers:
    print(f"{username} tidak follow back")

input('Press ENTER to exit')
