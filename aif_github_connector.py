import requests

# Replace 'your_github_token' with your actual GitHub token
GITHUB_TOKEN = 'your_github_token'
GITHUB_API_URL = 'https://api.github.com'

# Function to get user details
def get_user_details(username):
    url = f'{GITHUB_API_URL}/users/{username}'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to list repositories of a user
def list_user_repos(username):
    url = f'{GITHUB_API_URL}/users/{username}/repos'
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    username = 'octocat'  # Replace with the GitHub username you want to query
    user_details = get_user_details(username)
    if user_details:
        print(f"User Details for {username}:")
        print(user_details)
    else:
        print(f"Failed to fetch user details for {username}")

    user_repos = list_user_repos(username)
    if user_repos:
        print(f"\nRepositories for {username}:")
        for repo in user_repos:
            print(repo['name'])
    else:
        print(f"Failed to fetch repositories for {username}")