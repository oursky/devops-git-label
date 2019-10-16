import sys
from arguments import Arguments
from github_label_creator import GithubIssueCreator


def main():
    print("== DevOps: git-label ==\nCreate common label upon project setup.\n")

    args = Arguments()
    if not args.load(sys.argv[1:]):
        exit(0)
    if args.help:
        args.print_help()
        exit(0)

    github = GithubIssueCreator(args.github_token, args.slug, verbose=args.verbose)
    github.create_labels(args.labels)
    print("OK")


if __name__ == "__main__":
    main()
