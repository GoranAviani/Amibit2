#!/bin/sh
ssh root@104.248.28.51 <<EOF
    source ./amibit2env/bin/activate
    cd amibit2
    git pull
    pip install -r requirements.txt
    ./manage.py migrate
    systemctl restart gunicorn
    systemctl daemon-reload
    systemctl restart gunicorn.socket gunicorn.service
    nginx -t && sudo systemctl restart nginx
    exit
EOF

