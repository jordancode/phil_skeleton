# phil_skeleton
## scaffolding for a project built with Phil

### Usage:

1. Checkout the code
```bash
git clone --depth 1 https://github.com/jordancode/phil_skeleton.git [My new app directory]
```

2. Point to a new repository
```bash
cd [My new app directory] (or whatever checkout directory you picked)
rm -rf .git/
git init
git remote add origin [new repo url]
```

3. Rename phil_skeleton directory -> [your app name]
```bash
mv phil_skeleton [your app name]
```

4. Initialize phil submodule
```bash
git submodule init
git submodule update
```
5. Commit and push
```bash
git add .
git commit -m "First Commit"
git push origin master
```
