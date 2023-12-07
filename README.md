# GitHubRepoManager
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)



```GitHubRepoManager``` is a Python script designed to simplify the management and deletion of GitHub repositories within an organization. This tool leverages the GitHub API to retrieve a list of repositories, allowing users to review and selectively delete repositories with ease.

## Features
- Retrieve a list of repositories within a GitHub organization.
- Display repository names for user review.
- Prompt user for confirmation before deleting each repository.
- Provide feedback on successful deletions or errors.

## Usage
1. Clone the repository:
    ```bash
    git clone https://github.com/Lasith-Niro/GitHubRepoManager.git
    cd GitHubRepoManager
    ```
2. Install required dependencies:
    ```bash
    pip install requests
    ```

3. Configure the script:
   - Replace `organization_name` with your GitHub organization name.
   - Add your GitHub personal access token to `github_token`.

4. Run the script
    ```bash
    python repomanager.py
    ```

## Contributions
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](https://github.com/Lasith-Niro/GitHubRepoManager/blob/main/LICENSE) file for details.

