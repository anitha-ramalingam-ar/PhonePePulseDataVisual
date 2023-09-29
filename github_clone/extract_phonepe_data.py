import subprocess


def clone_github_repo(repo_url, destination_folder=None):
    cmd = ["git", "clone", repo_url]

    if destination_folder:
        cmd.append(destination_folder)

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"Error cloning the repository:\n{stderr.decode()}")
        return False
    else:
        print(
            f"Successfully cloned the repository to {destination_folder if destination_folder else 'current directory'}")
        return True
