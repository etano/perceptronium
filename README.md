Perceptronium
=============

Get API info here: https://dev.twitter.com/app

Install requirements:

    sudo pip install -r requirements.txt

To get running:

    python run.py

For crontab (every few hours):

    0 */3 * * * /usr/bin/python /root/src/perceptronium/run.py >> /root/src/perceptronium/run.log 2>&1
