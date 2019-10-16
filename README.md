# devops-git-label
> Create common git labels on project setup.

## Github Token
1. Go to https://github.com/settings/apps
2. Personal access tokens
3. Generate new token
4. Tick `repo` section
5. Give it a name, e.g. `devops-git-label`
6. `Generate token` button


## Usage
```
docker build -t devops-git-label https://github.com/oursky/devops-git-label.git
docker run -it --rm devops-git-label --github-token=XXXX --slug=owner/repo
```

#### Run with stored access token
```
echo 'GITHUB_TOKEB=XXXX' > .env
docker run -it --rm --env-file .env devops-git-label --slug=owner/repo
```
