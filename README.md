# ParrotParty
Also the most obnoxiously exploitable website that you never wanted to exploit.


## System requirements

You should have Python 3.x with pip and sqlite3.

## Setting up the Flask server

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
cd ParrotParty
```

Ensure all required packages are installed

```
pip install -r requirements.txt
```
Run the server

```
flask run
```

## Setting up the PhantomJS bot

Cd into the `parrot-bot` directory and run init.sh
```
cd parrot-bot
./init.sh
```

## Deploy PhantomJS bot on EC2 instance

`ssh` into the Ubuntu EC2 instance and build PhantomJS:

```
sudo apt-get install libstdc++ fontconfig
sudo apt-get install freetype-devel fontconfig-devel
wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
sudo mkdir -p /opt/phantomjs
bzip2 -d phantomjs-2.1.1-linux-x86_64.tar.bz2 
sudo tar -xvf phantomjs-2.1.1-linux-x86_64.tar  --directory /opt/phantomjs/ --strip-components 1
sudo ln -s /opt/phantomjs/bin/phantomjs /usr/bin/phantomjs
```

Set up a cron job to run the PhantomJS script every minute:

```
* * * * * /usr/bin/phantomjs /home/ec2-user/parrot-bot.js >> /tmp/log
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
