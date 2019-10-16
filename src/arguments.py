from typing import List
from environs import Env
import getopt
import json
from label import Label


class Arguments():
    help: bool
    verbose: bool
    github_token: str
    slug: str
    labels: List[Label]

    def __init__(self):
        self.help = False
        self.verbose = False
        self.github_token = None
        self.slug = None
        self.labels = []

    def load(self, args):
        env = Env()
        env.read_env()
        self.verbose = env.bool("VERBOSE", False)
        self.github_token = env.str('GITHUB_TOKEN', None)
        self.slug = env.str('SLUG', None)
        # command line arg override
        try:
            opts, args = getopt.getopt(args,
                                       "hv",
                                       ["help",
                                        "verbose",
                                        "github-token=",
                                        "slug="])
            for o, a in opts:
                if o in ("-v", "--verbose"):
                    self.verbose = True
                elif o in ("-h", "--help"):
                    self.help = True
                elif o in ("--github-token"):
                    self.github_token = a
                elif o in ("--slug"):
                    self.slug = a
        except getopt.GetoptError:
            pass

        if not self.github_token:
            print("GITHUB_TOKEN not configured, please set it on .env")
            return False
        if not self.slug:
            print("SLUG not configured, please set it on .env")
            return False
        return self._load_labels("labels.json")

    def _load_labels(self, filename: str) -> bool:
        self.labels = []
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
                for jlabel in data["labels"]:
                    label = Label(
                        name=jlabel["name"],
                        description=jlabel["description"],
                        color=jlabel["color"].replace("#", "")
                    )
                    self.labels.append(label)
            return True
        except Exception as e:
            print(str(e))
            return False

    def print_help(self):
        print("usage: python main.py [-h] -[v] [--github-token=XXXX] [--slug=owner/repo]")
        print("  -h              Show this help")
        print("  -v              Verbose")
        print("  --github-token Github personal access token with repo permission")
        print("  --slug         Specify github project slug")
