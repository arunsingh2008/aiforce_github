# Do not modify any function names or parameters. 

from jira import JIRA, JIRAError
import requests
import json
import base64 # Added for Basic Auth

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'amit_sahu@hcl-software.com'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    # Use jira_token as the password for the email
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_comments(ids=[]):
    """
    Fetch comments from JIRA using the provided comment IDs.

    Parameters:
    ids (list): List of comment IDs to fetch.

    Returns:
    dict: Response from the JIRA API.
    """
    # Using _get_auth_headers for direct requests
    headers = _get_auth_headers()
    payload = {
        "ids": ids
    }
    url = f"{base_url}/rest/api/3/comment/list"
    
    try:
        # verify=False is generally unsafe; consider using a proper certificate store.
        response = requests.post(url, headers=headers, json=payload, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# ---

from jira import JIRA, JIRAError
import base64 # Ensure import is here if snippets are separate

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr5ML1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def update_custom_fields(updates):
    """
    Update custom fields in JIRA issues.

    :param updates: List of dictionaries containing issueIds and value to update.
    :type updates: list
    :return: Response from the JIRA API.
    :rtype: dict
    """
    try:
        options = {'server': base_url, 'verify': False}
        # Use basic_auth=(email, jira_token) for JIRA client initialization
        jira = JIRA(options, basic_auth=(email, jira_token))
        payload = {"updates": updates}
        
        # Using basic auth headers for direct session call
        headers = _get_auth_headers()
        response = jira._session.put(f"{base_url}/rest/api/3/app/field/value", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except JIRAError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}

# ---

from jira import JIRA, JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
base_url = 'https://erx-products.atlassian.net'
email = 'amit_sahu@hcl-software.com'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def expand_attachment(id):
    """
    Fetches the raw expanded attachment data from JIRA.

    Parameters:
        id (str): The ID of the attachment to expand.

    Returns:
        dict: The response containing the expanded attachment data.
    """
    try:
        # Using _get_auth_headers for direct requests
        headers = _get_auth_headers()
        url = f'{base_url}/rest/api/3/attachment/{id}/expand/raw'
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

# ---

from jira import JIRA, JIRAError
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'amit_sahu@hcl-software.com'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_issue(issueIdOrKey):
    """
    Retrieve issue details from Jira.

    Parameters:
    - issueIdOrKey (str): The ID or key of the issue.

    Returns:
    - dict: The issue details.
    """
    try:
        options = {'server': base_url, 'verify': False}
        # Updated to use basic_auth=(email, jira_token)
        jira = JIRA(options=options, basic_auth=(email, jira_token))
        issue = jira.issue(issueIdOrKey)
        return issue.raw
    except JIRAError as e:
        return {'error': str(e)}

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def expand_attachment(id):
    """
    Fetch the human-readable expanded attachment metadata from JIRA.

    Parameters:
    id (str): The ID of the attachment to expand.

    Returns:
    dict: The expanded attachment metadata in a human-readable format.
    """
    try:
        # Initialize JIRA client with Basic Authentication
        options = {'server': base_url, 'verify': False}
        headers = _get_auth_headers()
        # Initialize JIRA with basic_auth, no need for headers here unless for direct session call
        jira = JIRA(options=options, basic_auth=(email, jira_token))

        # Construct the endpoint URL
        endpoint = f'/rest/api/3/attachment/{id}/expand/human'

        # Perform the GET request using the session and Basic Auth headers
        response = jira._session.get(base_url + endpoint, headers=headers)

        # Check for HTTP errors
        response.raise_for_status()

        # Return the JSON response
        return response.json()

    except JIRAError as e:
        print(f"JIRA error occurred: {e}")
        raise
    except requests.exceptions.RequestException as e:
        print(f"Request error occurred: {e}")
        raise

# ---

from jira import JIRA, JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_issue_types():
    """
    Fetches issue types from the JIRA API.

    Returns:
        dict: A dictionary containing the list of issue types.
    """
    try:
        options = {
            'server': base_url,
            'verify': False  # Disable SSL verification
        }
        # Updated to use basic_auth=(email, jira_token)
        jira = JIRA(options=options, basic_auth=(email, jira_token))
        issue_types = jira.issue_types()
        return {"list": [issue_type.raw for issue_type in issue_types]}
    except JIRAError as e:
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        return {"error": "Network error: " + str(e)}
    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}

# ---

from jira import JIRA, JIRAError
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication and base URL (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_default_values(fieldId):
    """
    Fetch the default values for a given field context in Jira.

    Parameters:
    - fieldId (str): The ID of the field to fetch default values for.

    Returns:
    - dict: The response containing the default values.
    """
    try:
        # Initialize JIRA client with Basic Authentication
        options = {'server': base_url, 'verify': False}
        jira = JIRA(options=options, basic_auth=(email, jira_token))

        # Construct the endpoint URL
        endpoint = f'/rest/api/3/field/{fieldId}/context/defaultValue'
        
        # Use basic auth headers for direct session call
        headers = _get_auth_headers()

        # Send the GET request
        response = jira._session.get(base_url + endpoint, headers=headers)

        # Check for successful response
        response.raise_for_status()

        # Return the JSON response
        return response.json()
    except JIRAError as e:
        # Handle JIRA-specific errors
        return {'error': str(e)}
    except Exception as e:
        # Handle general errors
        return {'error': str(e)}

# ---

from jira import JIRA, JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_attachment(id):
    """
    Fetch attachment metadata from Jira.

    Parameters:
    id (str): The ID of the attachment to retrieve.

    Returns:
    dict: Attachment metadata.
    """
    try:
        # Using _get_auth_headers for direct requests
        headers = _get_auth_headers()
        
        # Construct the URL for the attachment endpoint
        url = f"{base_url}/rest/api/3/attachment/{id}"

        # Send GET request to fetch attachment metadata
        response = requests.get(url, headers=headers, verify=False)

        # Check for successful response
        response.raise_for_status()

        # Return the attachment metadata
        return response.json()

    except JIRAError as e:
        # Handle JIRA-specific errors
        raise Exception(f"JIRAError: {e.text}")
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise Exception(f"RequestException: {e}")

# Example usage:
# attachment_metadata = get_attachment('10000')
# print(attachment_metadata)

# ---

from jira import JIRA, JIRAError
import base64 # Ensure import is here if snippets are separate

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def search_issues(jql="", startAt=0, maxResults=50, fields=None):
    """
    Search issues in JIRA using JQL.

    Parameters:
    - jql (str): JQL query string.
    - startAt (int): The index of the first issue to return (0-based).
    - maxResults (int): The maximum number of issues to return.
    - fields (list): List of fields to return for each issue.

    Returns:
    - dict: Response containing the list of issues.
    """
    try:
        options = {'server': base_url, 'verify': False}
        # Updated to use basic_auth=(email, jira_token)
        jira = JIRA(options=options, basic_auth=(email, jira_token))
        
        payload = {
            "jql": jql,
            "startAt": startAt,
            "maxResults": maxResults,
            "fields": fields or []
        }
        
        response = jira.search_issues(**payload)
        return {"issues": response}
    except JIRAError as e:
        return {"error": str(e)}

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
BASE_URL = 'https://erx-products.atlassian.net'
email = 'YOUR_JIRA_EMAIL'
API_KEY = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B' # Renamed to API_KEY in this snippet
HEADER_NAME = 'Authorization'

def _get_auth_headers():
    """Generate basic auth headers for email:API_KEY"""
    credentials = base64.b64encode(f'{email}:{API_KEY}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_all_projects():
    """
    Fetch all projects from the JIRA instance.

    Uses the JIRA library to interact with the JIRA API endpoint /rest/api/3/project.

    Returns:
        dict: A dictionary with a key 'values' containing a list of projects.
    """
    try:
        # Initialize JIRA client with Basic Authentication
        options = {
            'server': BASE_URL,
            'verify': False  # Disable SSL verification
        }
        # Updated to use basic_auth=(email, API_KEY)
        jira = JIRA(options=options, basic_auth=(email, API_KEY))

        # Fetch all projects
        projects = jira.projects()

        # Format the response
        response = {'values': [project.raw for project in projects]}
        return response

    except JIRAError as e:
        raise Exception(f"JIRAError: {e.text}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"RequestException: {str(e)}")
    except Exception as e:
        raise Exception(f"Unexpected error: {str(e)}")

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import base64 # Ensure import is here if snippets are separate

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_project(projectIdOrKey):
    """
    Fetches the project details from JIRA.

    :param projectIdOrKey: The project ID or key to fetch details for.
    :return: A dictionary containing the project details.
    """
    try:
        options = {'server': base_url, 'verify': False}
        # Updated to use basic_auth=(email, jira_token)
        jira = JIRA(options=options, basic_auth=(email, jira_token))
        project = jira.project(projectIdOrKey)
        return {"project": project.raw}
    except JIRAError as e:
        raise Exception(f"Failed to fetch project: {e.text}")
    except Exception as e:
        raise Exception(f"An error occurred: {str(e)}")

# ---

from jira import JIRA, JIRAError
import base64 # Ensure import is here if snippets are separate

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_users():
    """
    Fetches users from the Jira instance.

    Returns:
        dict: A dictionary with a list of users.
    """
    try:
        options = {'server': base_url, 'verify': False}
        # Updated to use basic_auth=(email, jira_token)
        jira = JIRA(options, basic_auth=(email, jira_token))
        users = jira.search_users('')
        return {"users": users}
    except JIRAError as e:
        return {"error": str(e)}

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Global constants for authentication (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
BASE_URL = 'https://erx-products.atlassian.net'
email = 'YOUR_JIRA_EMAIL'
API_KEY = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B' # Renamed to API_KEY in this snippet
HEADER_NAME = 'Authorization'

def _get_auth_headers():
    """Generate basic auth headers for email:API_KEY"""
    credentials = base64.b64encode(f'{email}:{API_KEY}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_all_users():
    """
    Fetch all users from JIRA using the /rest/api/3/user endpoint.

    Returns:
        dict: A dictionary containing the list of users.
    """
    try:
        # Initialize JIRA client with Basic Authentication
        options = {'server': BASE_URL, 'verify': False}
        headers = _get_auth_headers()
        # Initializing JIRA client for session access, using basic_auth
        jira = JIRA(options=options, basic_auth=(email, API_KEY))

        # Make the request to the /rest/api/3/user endpoint
        response = jira._session.get(f'{BASE_URL}/rest/api/3/user', headers=headers)

        # Check for successful response
        response.raise_for_status()

        # Return the response in the expected format
        return {"items": response.json()}

    except JIRAError as e:
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Authentication variables (assumed to be globally available) (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_tasks():
    """
    Fetches tasks from the JIRA API endpoint /rest/api/2/task.

    Returns:
        dict: A dictionary containing the list of tasks.
    """
    try:
        options = {
            'server': base_url,
            'verify': False  # Disable SSL verification
        }
        headers = _get_auth_headers()
        # Initializing JIRA client for session access, using basic_auth
        jira = JIRA(options=options, basic_auth=(email, jira_token))
        
        # Using the jira session for the GET request with basic auth headers
        response = jira._session.get(f'{base_url}/rest/api/2/task', headers=headers)

        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
    except JIRAError as e:
        return {'error': str(e)}
    except Exception as e:
        return {'error': str(e)}

# ---

from jira import JIRA
from jira.exceptions import JIRAError
import requests
import base64 # Ensure import is here if snippets are separate

# Disable SSL warnings
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

# Global authentication variables (Placeholders - REPLACE WITH YOUR ACTUAL VALUES)
email = 'YOUR_JIRA_EMAIL'
jira_token = 'ATATT3xFfGF0YXKMfbvCsiGsNtusSrKW1AwKrln57mb8iPzRTmvUwZvK4T5rXJa2qA3ujFOnuqfPjZ6uKxc_fZCcMx7CLjeTYS0VrVqZ2y6NbiDolT2mewB0vxGWAFdLjbT-1yPhpo0PGJFMXkA3mS-8JrNX9rfaEcdbr5MLr1T4DMkvwvUTkjU=B10AB94B'
base_url = 'https://erx-products.atlassian.net'

def _get_auth_headers():
    """Generate basic auth headers for email:jira_token"""
    credentials = base64.b64encode(f'{email}:{jira_token}'.encode()).decode()
    return {
        'Authorization': f'Basic {credentials}',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

def get_all_users_default():
    """
    Fetch all users from the Jira instance.

    Uses the `jira` library to interact with the Jira API.

    Returns:
        dict: A dictionary containing the list of users.
    """
    try:
        # Initialize the JIRA client with Basic Authentication
        jira = JIRA(
            server=base_url,
            options={'server': base_url, 'verify': False},
            basic_auth=(email, jira_token)
        )
        
        headers = _get_auth_headers()

        # Send the GET request to fetch users using basic auth headers
        users = jira._session.get(f'{base_url}/rest/api/3/users', headers=headers, verify=False)

        # Check if the request was successful
        users.raise_for_status()

        # Return the response in the expected format
        return {"User": users.json()}

    except JIRAError as e:
        return {"error": str(e)}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
