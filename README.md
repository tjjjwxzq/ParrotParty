# ParrotParty
Also the most obnoxiously exploitable website that you never wanted to exploit.


## System requirements

You should have Python 3.x with pip and PostgreSQL 9.4 or above

## Setting up

Get virtualenv and autoenv

```
sudo pip install virtualenv
sudo pip install autoenv
```

Set up the virtual environment. In your project directory:

```
virtualenv venv
```

Activate the virtual environment and set necessary environment variables (autoenv will run whatever is in the project's `.env` file)

```
cd ..
source `which activate.sh`
cd parrot_party
```

Ensure all required packages are installed

```
pip install -r requirements.txt
```

Create the database

```
psql
# create database database_parrot_party
\l
```

Run migrations and seed data

```
python manage.py db upgrade
python manage.py seed
```

Run the server

```
flask run
```

## Contributing

Follow the GitHub workflow. Push your work to a separate branch, and let others know that your code is awaiting review. Once your code has passed review, squash merge it into master and delete the branch.

Name your branch meaningfully, according to what you are implementing in the branch.
Let's follow the following naming conventions:

```
featuer/some-feature
bugfix/some-bug
enhance/some-enhancement
```

Remember to always to pull the latest updated version of master before starting on a new branch, and checkout your new branch from the latest master. Try not to push straight to master.

**Done by Jun Qi, Christabella, Zhao Juan, Hazel, Shaun**
_Kopi-CTF for SUTD module Security 50.020_

**Category:**

**Challenge Name:** The Parrot Party

**Short Introdution:**

**Summary of solution:**

**Running code:**