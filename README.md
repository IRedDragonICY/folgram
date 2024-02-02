# 🚀 Folgram

## 🔴 **WARNING!**

This script uses your Instagram sessionID which can contain _sensitive information_. Please be careful when sharing or
storing your sessionID. It is recommended to run this script in a secure environment.

## ⚠️ **Important Notice Before Running the Script**

1. 🚫 **Rate Limiting and Potential Ban**: This script uses multi-threading to fetch the followers and following lists
   concurrently. This can result in a large number of requests being sent to Instagram in a short period of time. If you
   make too many requests, Instagram might detect the activity as bot-like and limit your API usage, or even ban your
   account temporarily or permanently. To avoid this, please use the script responsibly and avoid making excessive
   requests.

2. 🔄 **Unexpected Logout**: If you find yourself unexpectedly logged out of your Instagram account after using this
   script, do not panic. This is a security measure by Instagram when it detects unusual activity such as excessive use
   of their API. It does not mean that your account has been hacked. Simply log back in to continue using Instagram.

## 📖 **Overview**

The `folgram` project is a Python script to analyze Instagram followers and followings. It fetches the list of followers
and following of a specific user and identifies users who do not follow back.

## 📚 **Project Structure**

The main file in this project is `main.py`. This script performs the following operations:

- Reads the Instagram sessionID from a file named `cookie.txt`. If the file is empty or does not exist, it asks the user
  to input the sessionID manually.
- Fetches the list of followers and following of a specific user using Instagram's private API endpoints.
- Compares the list of followers and following, and prints out the usernames of people who do not follow back.

## 🚀 **How to Run the Script**

1. Make sure you have Python installed on your machine. This script requires Python 3.6 or later.
2. Install the `requests` library if you haven't already. You can install it using pip:
   ```
   pip install requests
   ```
3. Clone this repository to your local machine.
4. Obtain your Instagram sessionID and save it in a file named `cookie.txt` in the same directory as `main.py`.
5. Run the script using Python:
   ```
   python main.py
   ```

## 📝 **Note**

Please b~~e~~ aware that this script uses private Instagram API endpoints. These are not officially supported by
Instagram and may change or stop working at any time. Use this script