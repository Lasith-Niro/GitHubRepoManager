import requests

# Replace 'org_name' with the actual organization name
organization_name = "org_name"
# Replace 'your_access_token' with your GitHub personal access token
github_token = ""


def get_repo_names(org_name, token=None):
    base_url = f"https://api.github.com/orgs/{org_name}/repos"
    headers = {"Authorization": f"token {token}"} if token else {}

    try:
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()
        repo_data = response.json()
        repo_names = [repo["name"] for repo in repo_data]
        return repo_names
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def delete_repo(org_name, repo_name, token=None):
    base_url = f"https://api.github.com/repos/{org_name}/{repo_name}"
    headers = {"Authorization": f"token {token}"} if token else {}

    try:
        response = requests.delete(base_url, headers=headers)
        response.raise_for_status()
        print(f"Repository {repo_name} deleted successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to delete repository {repo_name}. Error: {e}")

if __name__ == "__main__":
    repo_names = get_repo_names(organization_name, github_token)
    print(f"{len(repo_names)} are found!")
    if repo_names:
        for repo in repo_names:
            print(f"***{repo}***")
            
            delete_confirmation = input(f"Do you want to delete {repo} repository? (yes/no): ").lower()
            
            if delete_confirmation == "yes":
                delete_repo(organization_name, repo, github_token)
                print()
            else:
                print("Repositories will not be deleted.")
                print()
                
    else:
        print("Failed to retrieve repository names.")
