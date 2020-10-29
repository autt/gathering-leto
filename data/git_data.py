from github import Github


def get_issues(repo_addr):
    g = Github()
    repo = g.get_repo(repo_addr)
    return repo.get_issues()
