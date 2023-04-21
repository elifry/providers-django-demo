# Django Providers demo

This is a flexible template meant as a playground (lots of non-functional code) built as a hybrid app with Django and React. You can easily add static pages with Django written in python, and dynamic views with React. It uses a SQLite database. Python 3 is required.

## **Development**

### General principles
- **[important]** Keep build scripts GUI-independent. Use the Django API to run the scripts, don't bake the scripts into the API so much that they are inseparable. In fact, use an entirely different service/microservice if possible.
- Use Django for static views. Python is easier to maintain and reason about than javascript. It is also server-side, so it is safer.
- When you do use React views, use them as granularly as you can within Django templates.
- Make use of Tailwind CSS instead of styling your own CSS. This will save lots of time and headache. If you aren't familiar, take the time to learn it, it is very easy to pick up. Note: create functions in js that represent reuseable tailwind-styled objects. That way you only create it once with a particular style, and reuse over and over.

### Branching guidelines

> This section is meant to be used for when you copy this repo as a template. Most of it does not apply to this repo. 

This repo follows Trunk Based Development. If you are unfamiliar with the concept, please read the information in https://trunkbaseddevelopment.com/

In summary:
- The main branch has the latest code.
- Releases will happen as-needed.
- Versioning will be based on the Calendar Versioning spec: https://calver.org/ (please make a section for implementation details when the first release is made)
- Code does not go into the main branch without passing the tests. (currently you must run those locally)
- Keep commits and merge requests **SMALL**. Integrate often with other developers working on this repo.
- Feature branches should not be in development for longer than 2 days. If it is longer than that, it is a sign that the feature/issue is too large and should be broken up.
- Committing straight to the trunk is okay if everyone is following the process and the amount of changes is small.
- If any of the following are true, use a feature branch instead of committing directly to the trunk:
  - There are lots of lines changed
  - Recently the trunk has had bugs merged into it and it got broken for other developers
  - There are more than 3 developers working on this at once
  - You want someone to review your change before it goes in
  - You have a lot of commits you would like to automatically squash instead of using git rebase locally
- Squash commits before merging to main, this will keep the trunk cleaner to look at
- Set feature branches to be deleted after merging
- If a commit or merge request closes an issue, you can reference the issue number and [it will automatically close it](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically).
- Do everyone a favor and write some tests for your feature. It is really easy to add more tests in Django.

### Code structure
The structure was designed in such a way to give maximum flexibility down the line for using new frameworks and tools, as well as giving easy ways to create new static pages without having to dip into React or a similar framework.

`dashboard` is the central django project. The `urls.py` in that folder is the starting point for all the urls. All other submodules are included into this.

`demo`, `errorpages`, `settings`, and `theme`, etc are all submodules.
    - `demo` houses demo code for various views, with tailwind examples. There is a nav structure that can be expanded on. Proof of concepts and in-progress views go here.
    - `errorpages` - self explanatory
    - `settings` - self explanatory
    - `theme` is a special case submodule, created for [Django-Tailwind](https://django-tailwind.readthedocs.io/en/latest/installation.html) to make it easy to integrate tailwind into the app and have live refresh during development.

`static` is a generated folder by the build that houses the static javascript, css, and markdown that the app needs to render quickly.

`templates` are where html templates are stored - note that these are organized by submodules as well.

### Setup
Instructions for setting up, for each platform.

#### *Windows*
- Make sure python and SQLite is installed
    - Check python version `py --version` >> Python above 3.9 // GOOD
    - Check SQLite database
        - `py`
        - `import sqlite3`
        - `sqlite3.sqlite_version` >> above 3.25 // GOOD
- Install Django `pip3 install Django`
- Verify you have it `django --version` >> above 4 // GOOD
- (In the /src folder)
  - Verify npm `npm --version` >> above 8 // GOOD
  - Verify node `node --version` >> above v16 // GOOD
  - If you don't have node, install it from https://nodejs.org/en/download/
  - Install dependencies `npm install`
- `pip install markdown`
- set up https://revealjs.com/installation/#basic-setup
- `C:\Users\fryja\AppData\Local\Programs\Python\Python311\python.exe manage.py tailwind install`
- Verify that tailwind is installed `npm view tailwindcss version` >> above 2.2.4 // GOOD
- Create folder `static` in `src`
- Create folder `images` in `static`
- Copy image to `images` folder and replace the refererence in login.html

#### *Other*
- This project can be run in a Linux or Mac environment as well, but some of the setup and commands will be different.
- For Mac, the command is `python3` instead of `py`
- If you do a setup on another platform not already listed, please add your setups steps to this document for future reference.

### Running the app

#### *VSCode - automatic*
Open the project folder in VSCode, and from the Run and Debug, you can select "Run dev" to run everything.  
You can also select individual configurations for building piece by piece.

#### *Manual Steps*
You need 3 running services if you want everything to auto-update. Make sure you are in `build-dashboard/src`.
1. Pack JS `npm run dev`
2. Pack CSS `python manage.py tailwind start`
3. Run the webserver `py manage.py runserver`

If running for the first time or anytime you update models, you will need to setup the database
- Create migrations `py manage.py makemigrations`
- Create tables `py manage.py migrate`

### Viewing the page
- Go to `http://localhost:8000/`

### Before you do a merge request
Before you do a merge request, make sure to do all the following steps:

#### *1. Run the tests*
- `py manage.py test`
- Make sure you have no failed tests before you do a merge request

#### *2. Run the linters*
- Django templates (html): Use [djlint](https://github.com/Riverside-Healthcare/djlint). This tool is a bit finnicky, as of v1.7.0 it did not want to respect exclude paths, so you can't run it at the top level because it picks up a bunch of issues inside node_modules. Instead, you need to run it directly in the templates folder, where the `.djlintrc` is also stored.
    - In your terminal in `/src/templates`, run  `djlint . --lint`
        - In VSCode, this would look like this inside of a powershell instance: `PS <PATH>\build-dashboard\src\templates> djlint . --lint`
    - Make sure you have no errors before you do a merge request (e.x. `Linted 28 files, found 0 errors.`)
    - If you have other locations of html files, such as in other apps, you will have to run it there as well. You can look at the `.djlintrc` for any codes you can ignore in those other locations.
- Python: Use pylint
    - At the top level, run `pylint $(git ls-files '*.py')`
        - This will go through all the python code in the project, and only ones git cares about, meaning it honors the .gitignore and automatically ignores node_modules
    - pylint will also run any time you save a .py file, where it will add any problems to your problems tab in VSCode.
    - Make sure there are no issues in source files. You can ignore things in database migrations.
- Javascript linter (WANTED)

#### *3. Update any documentation needed*
- In the code itself
- In README files

#### *4. Go over code and refactor if necessary*
- Make sure there is no temporary code (commented out or not)
- Make sure variables, classes, etc are named well
- Think about long term maintainability and future improvements and generalize things as needed

### Updating packages
When you add a new package or update a package version using pip, be sure to update the requirements.txt. This file is stored at the top level.
- In the top level folder (one level higher than src) run the following: `pip3 freeze > requirements.txt`

## **Possible future improvements**
- Integrated webex spaces with the [space widget](https://developer.webex.com/docs/widgets)


## **Attribution**
- The initial setup and architecture image largely uses / is based on [this guide from saaspegasus.com](https://www.saaspegasus.com/guides/modern-javascript-for-django-developers/)