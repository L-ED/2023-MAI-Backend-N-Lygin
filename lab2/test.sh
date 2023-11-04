sudo cp /home/led/MAI/2023-MAI-Backend-N-Lygin/lab2/backend/nginx/nginx.conf /etc/nginx/nginx.conf
sudo service nginx start 
nohup sh run_wsgi.sh
wrk -t12 -c400 -d30s http://127.0.0.1:80/index.html