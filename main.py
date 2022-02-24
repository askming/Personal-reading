# -*- coding: utf-8 -*-
import argparse
import os
from datetime import date
from github import Github


TOP_MD_DIR = 'book'


def get_me(user):
    return user.get_user().login

def isMe(issue, me):
    return issue.user.login == me

def format_time(time):
    return str(time)[:10]

def login(token):
    return Github(token)

def get_repo(user: Github, repo: str):
    return user.get_repo(repo)


def get_repo_labels(repo):
    return [l for l in repo.get_labels()]

def get_issues_from_label(repo, label):
    return repo.get_issues(labels=(label,))


def get_save_to_dir(issue):
    year = str(issue.created_at)[:4]
    save_to_dir = os.path.join(TOP_MD_DIR, year)

    if not os.path.exists(save_to_dir):
        os.mkdir(save_to_dir)
    
    return save_to_dir


def get_to_generate_issues(repo, issue_number=None):
    # md file will only be updated when there is any change to an issue (i.e. issue_number is not NULL)
    # so we don't need to check if this issue already exists or not
    to_generate_issues = []
    if issue_number:
        to_generate_issues.append(repo.get_issue(int(issue_number)))
    return to_generate_issues


def save_issue(issue, me):
    dir_name = get_save_to_dir(issue)

    md_name = os.path.join(
        dir_name, f"{issue.title}.md"
    )
    with open(md_name, "w") as f:
        f.write(f"# [{issue.title}]({issue.html_url})\n\n")
        f.write(issue.body)
        if issue.comments:
            for c in issue.get_comments():
                if isMe(c, me):
                    f.write("\n\n---\n\n")
                    f.write(f"_{format_time(c.updated_at)}_\n\n")
                    f.write(c.body)


def main(token, repo_name, issue_number=None):
    user = login(token)
    me = get_me(user)
    repo = get_repo(user, repo_name)

    # identify issue(s) to be generated/updated
    to_generate_issues = get_to_generate_issues(repo, issue_number)

    # save md files to the to_save_dir
    for issue in to_generate_issues:
        save_issue(issue, me)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("--issue_number", help="issue_number", default=None, required=False)
    options = parser.parse_args()
    main(options.github_token, options.repo_name, options.issue_number)