# -*- coding: utf-8 -*-
import argparse
import os
from github import Github


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


def get_to_save_dir(issue):
    year = str(issue.created_at)[:4]
    return os.path.join('book', year)


def get_to_generate_issues(repo, dir_name, issue_number=None):
    md_files = os.listdir(dir_name)
    generated_issues_names = md_files
    dir_year = os.path.normpath(dir_name).split(os.path.sep)[-1]

    to_generate_issues = [
        i
        for i in list(repo.get_issues())
        if i.title + '.md' not in generated_issues_names and str(i.created_at)[:4] == dir_year
    ]
    if issue_number:
        to_generate_issues.append(repo.get_issue(int(issue_number))) # single issue not issues! when an existing issue gets updated (e.g. with comments)
    return to_generate_issues


def save_issue(issue, me, dir_name):
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
                    f.write("*" + format_time(c.created_at) + "*\n\n")
                    f.write(c.body)


def main(token, repo_name, issue_number=None):
    user = login(token)
    me = get_me(user)
    repo = get_repo(user, repo_name)

    issues = repo.get_issues() 
    for i in issues:
        to_save_dir = get_to_save_dir(i)
        if not os.path.exists(to_save_dir):
            os.mkdir(to_save_dir)

        # identify issues to be generated under current to_save_dir
        to_generate_issues = get_to_generate_issues(repo, to_save_dir, issue_number)

        # save md files to the to_save_dir
        for issue in to_generate_issues:
            save_issue(issue, me, to_save_dir)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("github_token", help="github_token")
    parser.add_argument("repo_name", help="repo_name")
    parser.add_argument("--issue_number", help="issue_number", default=None, required=False)
    options = parser.parse_args()
    main(options.github_token, options.repo_name, options.issue_number)